from fastapi import APIRouter

from app.models.qr_model import (
    QRModel
)

from app.controllers.qr_controller import (
    generate_qr,
    get_qr_history,
    delete_qr
)

router = APIRouter(
    prefix="/qr",
    tags=["QR"]
)


# GENERATE QR

@router.post(
    "/generate"
)

def create_qr(
    data: QRModel
):

    return generate_qr(
        data
    )


# QR HISTORY

@router.get(
    "/history"
)

def history():

    return get_qr_history()


# DELETE QR

@router.delete(
    "/delete/{qr_id}"
)

def remove_qr(
    qr_id: int
):

    return delete_qr(
        qr_id
    )