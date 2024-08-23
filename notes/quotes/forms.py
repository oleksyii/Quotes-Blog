from django.forms import Form, CharField, TextInput, DateField, DateInput, Textarea


class QuoteForm(Form):
    quote = CharField(min_length=3, required=True, widget=Textarea())
    tags = CharField(min_length=2, required=True, widget=TextInput())


class AuthorForm(Form):
    fullname = CharField(min_length=3, required=True, widget=TextInput())
    born_date = DateField(required=True, widget=DateInput(attrs={"type": "date"}))
    born_location = CharField(min_length=2, required=True, widget=TextInput())
    description = CharField(min_length=2, required=True, widget=Textarea())
