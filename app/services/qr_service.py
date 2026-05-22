import os
import uuid
import qrcode

from PIL import Image

# QR STORAGE

QR_FOLDER = (
    "app/static/qr_codes"
)

os.makedirs(
    QR_FOLDER,
    exist_ok=True
)


# GENERATE QR

def create_qr(
    text,
    fill_color="#000000",
    back_color="#ffffff"
):

    filename = (
        f"{uuid.uuid4()}.png"
    )

    filepath = os.path.join(
        QR_FOLDER,
        filename
    )

    qr = qrcode.QRCode(

        version=1,

        box_size=10,

        border=4
    )

    qr.add_data(text)

    qr.make(
        fit=True
    )

    image = qr.make_image(

        fill_color=fill_color,

        back_color=back_color
    )

    image.save(
        filepath
    )

    return {

        "filename":
        filename,

        "path":
        filepath
    }


# QR WITH LOGO

def create_logo_qr(

    text,

    logo_path,

    fill_color="#000000",

    back_color="#ffffff"
):

    qr_data = create_qr(

        text,

        fill_color,

        back_color
    )

    qr_image = Image.open(
        qr_data["path"]
    )

    logo = Image.open(
        logo_path
    )

    logo_size = 80

    logo = logo.resize(
        (
            logo_size,
            logo_size
        )
    )

    qr_width,
    qr_height = qr_image.size

    x = (
        qr_width -
        logo_size
    ) // 2

    y = (
        qr_height -
        logo_size
    ) // 2

    qr_image.paste(
        logo,
        (x, y)
    )

    qr_image.save(
        qr_data["path"]
    )

    return qr_data


# DELETE QR

def delete_qr_file(
    file_path
):

    if os.path.exists(
        file_path
    ):

        os.remove(
            file_path
        )

        return True

    return False


# GET QR PATH

def get_qr_path(
    filename
):

    return os.path.join(
        QR_FOLDER,
        filename
    )