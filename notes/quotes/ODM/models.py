from mongoengine import Document
from mongoengine.fields import (
    BooleanField,
    ListField,
    StringField,
    ReferenceField,
    DateField,
)


class Author(Document):
    fullname = StringField(required=True)
    born_date = DateField()
    born_location = StringField()
    description = StringField(required=True)


class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author)
    quote = StringField(required=True)
