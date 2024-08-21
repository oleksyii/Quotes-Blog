from .models import Author, Quote
import re

from mongoengine import DoesNotExist
from mongoengine.queryset.visitor import Q

import redis
from redis_lru import RedisLRU

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)


PARAMS = {"tag": ["tag", "tags"], "name": ["name", "author"], "exit": ["exit"]}

pattern = re.compile(r"\w+", re.UNICODE)


@cache
def request_authors_by_name(search_param: str):
    try:
        # Find the Author document by fullname
        authors = Author.objects(fullname__icontains=search_param)
    except DoesNotExist:
        print("Author not found.")
        authors = None
    return authors


@cache
def request_quotes_by_author(authors_param):
    # Query the Quote documents by the author reference
    return Quote.objects(author__in=authors_param)


@cache
def request_quotes_by_tags(seacrh_params: str):
    tags = find_all_tags(seacrh_params)
    query = Q()

    for tag in tags:
        query |= Q(tags__icontains=tag)

    # Retrieve all quotes where any tag contains one of the substrings in the list
    return Quote.objects(query)


def find_all_tags(tags_string: str):
    return pattern.findall(tags_string.lower())


def is_in_dict(val: str, params: dict):
    for param in PARAMS.values():
        if val in param:
            return True
    return False


def run():
    res = ""
    while True:
        user_input = input("Enter a search request: ")
        if user_input in PARAMS["exit"]:
            print("Bye-Bye!")
            break

        param, val = user_input.split(":")

        val = val.strip()
        param = param.strip().lower()

        if not is_in_dict(param, PARAMS):
            print("Wrong search parameter")
            continue

        if param in PARAMS["name"]:

            authors = request_authors_by_name(val)

            if authors:

                for quote in request_quotes_by_author(authors):
                    print(
                        f"Quote: {quote.quote}\nAuthor: {quote.author.fullname}",
                        end="\n\n",
                    )
            else:
                print("No quotes found for the given author.")

        if param in PARAMS["tag"]:
            for quote in request_quotes_by_tags(val):
                print(f"Quote: {quote.quote}\nTags: {quote.tags}", end="\n\n")

        print()
