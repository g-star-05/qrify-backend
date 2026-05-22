import os
import uuid
import shutil

from fastapi import UploadFile


# STORAGE PATHS

BASE_STORAGE = "app/static"

QR_STORAGE = os.path.join(
    BASE_STORAGE,
    "generated_qr"
)

TEMPLATE_STORAGE = os.path.join(
    BASE_STORAGE,
    "templates"
)

UPLOAD_STORAGE = os.path.join(
    BASE_STORAGE,
    "uploads"
)


# CREATE FOLDERS

os.makedirs(
    QR_STORAGE,
    exist_ok=True
)

os.makedirs(
    TEMPLATE_STORAGE,
    exist_ok=True
)

os.makedirs(
    UPLOAD_STORAGE,
    exist_ok=True
)


# SAVE FILE

async def save_file(

    file: UploadFile,

    folder=UPLOAD_STORAGE

):

    extension = file.filename.split(
        "."
    )[-1]

    filename = (
        f"{uuid.uuid4()}."
        f"{extension}"
    )

    filepath = os.path.join(
        folder,
        filename
    )

    with open(
        filepath,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    return {

        "filename":
        filename,

        "path":
        filepath
    }


# DELETE FILE

def delete_file(
    filepath
):

    if os.path.exists(
        filepath
    ):

        os.remove(
            filepath

        )

        return True

    return False


# LIST FILES

def list_files(
    folder
):

    if not os.path.exists(
        folder
    ):

        return []

    return os.listdir(
        folder
    )


# CHECK FILE

def file_exists(
    filepath
):

    return os.path.exists(
        filepath
    )