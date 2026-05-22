import os
import uuid
import qrcode

from fastapi import HTTPException


QR_FOLDER = "app/static/generated_qr"

os.makedirs(
    QR_FOLDER,
    exist_ok=True
)

qr_history = []


def generate_qr(data):

    if not data.text:

        raise HTTPException(

            status_code=400,

            detail="Text required"

        )

    qr_text = data.text.strip()

    # Auto add https

    if (

        "." in qr_text

        and not qr_text.startswith(
            "http://"
        )

        and not qr_text.startswith(
            "https://"
        )

    ):

        qr_text = (
            "https://"
            + qr_text
        )

    filename = f"{uuid.uuid4()}.png"

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

        len(qr_history) + 1,

        "text":
        qr_text,

        "color":
        fill_color,

        "background":
        bg_color,

        # Frontend uses response.data.qr_url

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

        len(qr_history),

        "data":

        qr_history

    }


def delete_qr(
    qr_id: int
):

    global qr_history

    qr_history = [

        qr

        for qr

        in qr_history

        if qr["id"]

        != qr_id

    ]

    return {

        "message":

        "Deleted Successfully"

    }