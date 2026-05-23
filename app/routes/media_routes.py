from fastapi import (

APIRouter,

UploadFile,

File

)

from app.controllers.media_controller import (

upload_audio,

upload_image

)

router = APIRouter(

prefix="/media",

tags=["Media"]

)


@router.post(
"/upload-audio"
)

async def upload_audio_route(

file: UploadFile = File(...)

):

    return await upload_audio(
        file
    )



@router.post(
"/upload-image"
)

async def upload_image_route(

file: UploadFile = File(...)

):

    return await upload_image(
        file
    )