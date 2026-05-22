import os

from pymongo import MongoClient

from dotenv import load_dotenv

# LOAD ENV VARIABLES

load_dotenv()

# GET URI

MONGO_URI = os.getenv(
    "MONGO_URI"
)

# CONNECTION

client = MongoClient(
    MONGO_URI
)

# DATABASE

db = client["qrify_db"]

# COLLECTIONS

users_collection = db["users"]

qr_collection = db["qr_codes"]

templates_collection = db["templates"]


# TEST CONNECTION

def test_connection():

    try:

        client.admin.command(
            "ping"
        )

        print(
            "MongoDB Connected Successfully 🚀"
        )

    except Exception as e:

        print(
            f"Database Error: {e}"
        )