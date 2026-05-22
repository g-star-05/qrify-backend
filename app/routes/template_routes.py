from fastapi import APIRouter

from app.models.schema import (
    TemplateSchema
)

from app.controllers.template_controller import (
    get_templates,
    get_template,
    create_template,
    delete_template
)

router = APIRouter(
    prefix="/templates",
    tags=["Templates"]
)


# GET ALL TEMPLATES

@router.get(
    "/"
)

def all_templates():

    return get_templates()


# GET SINGLE TEMPLATE

@router.get(
    "/{template_id}"
)

def single_template(
    template_id: int
):

    return get_template(
        template_id
    )


# CREATE TEMPLATE

@router.post(
    "/create"
)

def add_template(
    template: TemplateSchema
):

    return create_template(
        template
    )


# DELETE TEMPLATE

@router.delete(
    "/delete/{template_id}"
)

def remove_template(
    template_id: int
):

    return delete_template(
        template_id
    )