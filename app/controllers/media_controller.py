import os
import uuid

from fastapi import UploadFile


AUDIO_FOLDER = "app/static/audio"
IMAGE_FOLDER = "app/static/images"

os.makedirs(
    AUDIO_FOLDER,
    exist_ok=True
)

os.makedirs(
    IMAGE_FOLDER,
    exist_ok=True
)


async def upload_audio(
    file: UploadFile
):

    filename = (

        f"{uuid.uuid4()}_"

        + file.filename

    )

    filepath = os.path.join(

        AUDIO_FOLDER,

        filename

    )

    with open(

        filepath,

        "wb"

    ) as buffer:

        content = await file.read()

        buffer.write(
            content
        )

    return {

        "url":

        f"/static/audio/{filename}"

    }



async def upload_image(
    file: UploadFile
):

    filename = (

        f"{uuid.uuid4()}_"

        + file.filename

    )

    filepath = os.path.join(

        IMAGE_FOLDER,

        filename

    )

    with open(

        filepath,

        "wb"

    ) as buffer:

        content = await file.read()

        buffer.write(
            content
        )

    return {

        "url":

        f"/static/images/{filename}"

    }