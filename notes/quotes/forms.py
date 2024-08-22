from django.forms import Form, CharField, TextInput


class QuoteForm(Form):

    quote = CharField(min_length=3, required=True, widget=TextInput())
    tags = CharField(min_length=2, required=True, widget=TextInput())
