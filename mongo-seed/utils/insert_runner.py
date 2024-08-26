from mongoengine import Document
from pymongo.errors import ServerSelectionTimeoutError

RECONNECT_ATTEMPTS = 5


def do_insert(Obj: Document, data: list):
    for _ in range(RECONNECT_ATTEMPTS):
        print("waiting for 20 seconds to connect...")
        try:
            Obj.objects.insert(data)
            return
        except ServerSelectionTimeoutError:
            continue
