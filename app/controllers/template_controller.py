from fastapi import HTTPException

# TEMP STORAGE
# Later move to MongoDB

templates_db = [

    {
        "id": 1,

        "name":
        "Restaurant Menu",

        "category":
        "Business",

        "description":
        "Digital restaurant menu QR template"
    },

    {
        "id": 2,

        "name":
        "Event QR",

        "category":
        "Events",

        "description":
        "QR template for event registration"
    },

    {
        "id": 3,

        "name":
        "Business Card",

        "category":
        "Professional",

        "description":
        "Smart business card QR"
    }
]


# GET ALL TEMPLATES

def get_templates():

    return {

        "count":
        len(templates_db),

        "templates":
        templates_db
    }


# GET SINGLE TEMPLATE

def get_template(template_id):

    template = next(

        (

            t

            for t in templates_db

            if t["id"] == template_id

        ),

        None
    )

    if not template:

        raise HTTPException(

            status_code=404,

            detail="Template not found"
        )

    return template


# CREATE TEMPLATE

def create_template(template):

    new_template = {

        "id":
        len(templates_db)+1,

        "name":
        template.name,

        "category":
        template.category,

        "description":
        template.description
    }

    templates_db.append(
        new_template
    )

    return {

        "message":
        "Template created successfully",

        "template":
        new_template
    }


# DELETE TEMPLATE

def delete_template(template_id):

    global templates_db

    template = next(

        (

            t

            for t in templates_db

            if t["id"] == template_id

        ),

        None
    )

    if not template:

        raise HTTPException(

            status_code=404,

            detail="Template not found"
        )

    templates_db = [

        t

        for t in templates_db

        if t["id"] != template_id
    ]

    return {

        "message":
        "Template deleted successfully"
    }