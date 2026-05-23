from fastapi import APIRouter, UploadFile, File
import os
import uuid

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)

UPLOAD_DIR = "app/static/uploads"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)


@router.post("/")

async def upload_file(

file:UploadFile=File(...)

):

    ext = file.filename.split(".")[-1]

    filename = (

        f"{uuid.uuid4()}.{ext}"

    )

    path = os.path.join(

        UPLOAD_DIR,

        filename

    )

    with open(
        path,
        "wb"
    ) as f:

        f.write(
            await file.read()
        )

    return {

        "url":

f"/static/uploads/{filename}"

    }