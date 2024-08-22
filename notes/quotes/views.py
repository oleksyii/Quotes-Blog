from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .mongo_db import connectme
from .ODM.models import Quote, Author
from .forms import QuoteForm

connectme.run()


# Create your views here.
def main(request):
    qs = Quote.objects()
    return render(request, "quotes/index.html", {"quotes": qs})


@login_required
def add_quote(request):

    if request.method == "POST":
        print(request.POST["quote"])

    # Display the possible authors on the form
    return render(
        request,
        "quotes/add-quote.html",
        {"form": QuoteForm(), "authors": Author.objects()},
    )
