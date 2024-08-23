from django.shortcuts import render
from quotes.ODM.models import Author
from bson import ObjectId


# Create your views here.
def main(request, author_id):
    author = Author.objects.get(id=ObjectId(author_id))
    return render(request, "authors/author.html", {"author": author})
