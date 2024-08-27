from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from bson import ObjectId
from mongoengine.queryset.visitor import Q

from .mongo_db import connectme
from .ODM.models import Quote, Author
from .forms import QuoteForm, AuthorForm
from .utils import regex_utils as re_ut

connectme.run()


def get_top_ten_tags():
    # Aggregation pipeline
    pipeline = [
        {"$unwind": "$tags"},  # Unwind the tags list to get individual tags
        {
            "$group": {"_id": "$tags", "count": {"$sum": 1}}
        },  # Group by tag and count occurrences
        {"$sort": {"count": -1}},  # Sort by count in descending order
        {"$limit": 10},  # Limit the results to the top 10
    ]

    # Run the aggregation pipeline
    top_tags = Quote.objects.aggregate(*pipeline)

    # Convert the cursor to a list and print results
    top_tags_list = list(top_tags)
    res = [{"name": tag["_id"], "count": tag["count"]} for tag in top_tags_list]
    return res


# Create your views here.
def main(request):
    qs = Quote.objects()
    return render(
        request, "quotes/index.html", {"quotes": qs, "top_tags": get_top_ten_tags()}
    )


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


def see_tag(request, tag_name):
    qs = Quote.objects(tags__contains=tag_name)
    return render(
        request, "quotes/index.html", {"quotes": qs, "top_tags": get_top_ten_tags()}
    )
