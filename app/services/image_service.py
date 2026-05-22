import os
import uuid

from PIL import Image

from fastapi import UploadFile


# IMAGE FOLDER

IMAGE_FOLDER = (
    "app/static/images"
)

os.makedirs(
    IMAGE_FOLDER,
    exist_ok=True
)


# SAVE IMAGE

async def save_image(
    file: UploadFile
):

    # UNIQUE NAME

    extension = (
        file.filename
        .split(".")[-1]
    )

    filename = (
        f"{uuid.uuid4()}"
        f".{extension}"
    )

    filepath = os.path.join(
        IMAGE_FOLDER,
        filename
    )

    # SAVE

    with open(
        filepath,
        "wb"
    ) as buffer:

        buffer.write(
            await file.read()
        )

    return {

        "filename":
        filename,

        "path":
        filepath
    }


# RESIZE IMAGE

def resize_image(
    image_path,
    width=500,
    height=500
):

    image = Image.open(
        image_path
    )

    image = image.resize(
        (width, height)
    )

    image.save(
        image_path
    )

    return image_path


# DELETE IMAGE

def delete_image(
    image_path
):

    if os.path.exists(
        image_path
    ):

        os.remove(
            image_path
        )

        return True

    return False