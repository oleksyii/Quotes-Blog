from django.apps import AppConfig
import atexit
from mongoengine import disconnect


class QuotesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "quotes"

    def ready(self):
        # Register the shutdown handler
        atexit.register(self.close_mongo_connection)

    @staticmethod
    def close_mongo_connection():
        disconnect()
        print("MongoDB connection closed on server shutdown.")
