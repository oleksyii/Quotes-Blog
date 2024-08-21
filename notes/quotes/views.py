from django.shortcuts import render

from .mongo_db import connectme
from .ODM.models import Quote

connectme.run()


# Create your views here.
def main(request):
    qs = Quote.objects()
    return render(request, "quotes/index.html", {"quotes": qs})
