import json
from .models import Author, Quote
from utils import data_parser, insert_runner
from mongoengine.errors import NotUniqueError, ValidationError

BATCH_SIZE = 2


def run(authors_file_path: str, quotes_file_path: str):
    with open(authors_file_path, "r") as file:
        authors = json.load(file)
        author_objs = []
        for idx, author in enumerate(authors):
            print(data_parser.parse_date(author["born_date"]))
            author_objs.append(
                Author(
                    fullname=author["fullname"],
                    born_date=data_parser.parse_date(author["born_date"]),
                    born_location=author["born_location"],
                    description=author["description"],
                )
            )
            # Batch inserting
            if idx % BATCH_SIZE == 0:
                try:
                    insert_runner.do_insert(Author, author_objs)
                    print(f"Inserted authors batch of size {BATCH_SIZE}")
                    author_objs = []
                except (NotUniqueError, ValidationError) as e:
                    print(f"An error occurred: {e}")

        insert_runner.do_insert(Author, author_objs)
        author_objs = []
        print(f"Finished inserting authors. Inserted {len(authors)} authors")

    with open(quotes_file_path, "r") as file:
        quotes = json.load(file)
        quotes_objs = []
        for idx, q in enumerate(quotes):
            quotes_objs.append(
                Quote(
                    tags=q["tags"],
                    author=Author.objects.get(fullname=q["author"]),
                    quote=q["quote"],
                )
            )
            # Batch inserting
            if idx % BATCH_SIZE == 0:
                try:

                    insert_runner.do_insert(Quote, quotes_objs)
                    print(f"Inserted quotes batch of size {BATCH_SIZE}")
                    quotes_objs = []
                except (NotUniqueError, ValidationError) as e:
                    print(f"An error occurred: {e}")

        Quote.objects.insert(quotes_objs)
        print(f"Finished inserting quotes. Inserted {len(quotes)} quotes")
