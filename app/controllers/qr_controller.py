import os
import re
import uuid
import qrcode

from fastapi import HTTPException


QR_FOLDER = "app/static/generated_qr"

os.makedirs(
    QR_FOLDER,
    exist_ok=True
)

qr_history = []


# EMAIL

EMAIL_REGEX = re.compile(

r"^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$"

)


MAILTO_REGEX = re.compile(

r"^mailto:[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$",

re.IGNORECASE

)


# PHONE

PHONE_REGEX = re.compile(

r"^\+?[\d\s\-\(\)]{7,15}$"

)


# COLOR

HEX_COLOR_REGEX = re.compile(

r"^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"

)



def format_qr_text(raw:str)->str:

    text = raw.strip()


    # MAILTO

    if MAILTO_REGEX.match(
        text
    ):

        return text


    # EMAIL

    if EMAIL_REGEX.match(
        text
    ):

        return f"mailto:{text}"


    # PHONE

    if (

        text.lower().startswith(
            "tel:"
        )

        or

        text.lower().startswith(
            "sms:"
        )

    ):

        return text


    if PHONE_REGEX.match(
        text
    ):

        digits = re.sub(

            r"[\s\-\(\)]",

            "",

            text

        )

        return f"tel:{digits}"


    # WHATSAPP

    if (

        "wa.me/"

        in text

        and

        not text.startswith(
            "https://"
        )

    ):

        return f"https://{text}"


    # URL

    if (

        text.startswith(
            "http://"
        )

        or

        text.startswith(
            "https://"
        )

    ):

        return text


    # WEBSITE

    if (

        "." in text

        and

        "@" not in text

    ):

        return f"https://{text}"


    return text



def generate_qr(data):

    if (

        not data.text

        or

        not data.text.strip()

    ):

        raise HTTPException(

            status_code=400,

            detail=
            "Text required"

        )


    qr_text = format_qr_text(
        data.text
    )


    fill_color = (

        data.color

        if data.color

        else "#000000"

    )


    bg_color = (

        data.background

        if data.background

        else "#ffffff"

    )


    if not HEX_COLOR_REGEX.match(
        fill_color
    ):

        fill_color = "#000000"


    if not HEX_COLOR_REGEX.match(
        bg_color
    ):

        bg_color = "#ffffff"


    filename = (

        f"{uuid.uuid4()}.png"

    )


    filepath = os.path.join(

        QR_FOLDER,

        filename

    )


    qr = qrcode.QRCode(

        version=1,

        error_correction=
        qrcode.constants.ERROR_CORRECT_H,

        box_size=10,

        border=4

    )


    qr.add_data(
        qr_text
    )

    qr.make(
        fit=True
    )


    image = qr.make_image(

        fill_color=
        fill_color,

        back_color=
        bg_color

    )


    image.save(
        filepath
    )


    qr_data = {

        "id":

        len(
            qr_history
        )+1,

        "text":
        qr_text,

        "color":
        fill_color,

        "background":
        bg_color,

        "qr_url":

        f"/static/generated_qr/{filename}"

    }


    qr_history.append(
        qr_data
    )

    return qr_data



def get_qr_history():

    return {

        "count":

        len(
            qr_history
        ),

        "data":

        qr_history

    }



def delete_qr(
    qr_id:int
):

    global qr_history


    exists = any(

        qr["id"]

        ==

        qr_id

        for qr

        in qr_history

    )


    if not exists:

        raise HTTPException(

            status_code=404,

            detail=
            "QR not found"

        )


    qr_delete = next(

        qr

        for qr

        in qr_history

        if qr["id"]

        ==

        qr_id

    )


    file_path = (

        f"app{qr_delete['qr_url']}"

    )


    if os.path.exists(
        file_path
    ):

        os.remove(
            file_path
        )


    qr_history = [

        qr

        for qr

        in qr_history

        if qr["id"]

        !=

        qr_id

    ]


    return {

        "message":

        "Deleted successfully"

    }