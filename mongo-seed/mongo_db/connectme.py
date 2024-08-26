import os
from mongoengine import connect
from dotenv import load_dotenv


load_dotenv()


def run():
    mongo_string = os.getenv("MONGO_STRING")
    try:
        connect(
            db=os.getenv("MONGO_DB"),
            username=os.getenv("MONGO_LOGIN"),
            password=os.getenv("MONGO_PASSWORD"),
            host=os.getenv("MONGO_HOST"),
            port=int(os.getenv("MONGO_PORT")),
        )
        print("Connected to MongoDB successfully.")

    except ConnectionError as e:
        print(f"Failed to connect to MongoDB: {e}")
