import os
from mongoengine import connect
from dotenv import load_dotenv


load_dotenv("/home/oleksii/GoIT/goit-web-10/.env")


def run():
    mongo_string = os.getenv("MONGO_STRING")
    try:
        connect(db="quotes", host=mongo_string, ssl=True)
        print("Connected to MongoDB successfully.")

    except ConnectionError as e:
        print(f"Failed to connect to MongoDB: {e}")
