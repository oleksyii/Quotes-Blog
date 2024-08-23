from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .mongo_db import connectme
from .ODM.models import Quote, Author
from bson import ObjectId
from .forms import QuoteForm, AuthorForm
from .utils import regex_utils as re_ut

connectme.run()


# Create your views here.
def main(request):
    qs = Quote.objects()
    return render(request, "quotes/index.html", {"quotes": qs})


@login_required
def add_quote(request):

    if request.method == "POST":
        print(request.POST)
        form = QuoteForm(request.POST)
        if form.is_valid():
            data = request.POST
            tags = re_ut.find_all_tags(data["tags"])
            quote = Quote(
                quote=data["quote"],
                tags=tags,
                author=Author.objects.get(id=ObjectId(data["author"])),
            )
            quote.save()
            print(quote)
            print(f"The quote {quote.id} is succesfully saved")

    # Display the possible authors on the form
    return render(
        request,
        "quotes/add-quote.html",
        {"form": QuoteForm(), "authors": Author.objects()},
    )


@login_required
def add_author(request):

    if request.method == "POST":
        print(request.POST)
        form = AuthorForm(request.POST)
        if form.is_valid():
            data = request.POST
            author = Author(
                fullname=data["fullname"],
                born_date=data["born_date"],
                born_location=data["born_location"],
                description=data["description"],
            )
            author.save()
            print(author)
            print(f"The author {author.id} is succesfully saved")

    return render(request, "quotes/add-author.html", {"form": AuthorForm})
