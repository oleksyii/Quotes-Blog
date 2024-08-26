from mongo_db import connectme
from ODM import seed
from pathlib import Path
import os


def main():
    # Connect the whole thing to mongo
    connectme.run()

    authors_file = Path("./data/authors.json")
    quotes_file = Path("./data/quotes.json")
    # Run the seeding script
    print("Seeding is in progress")
    seed.run(authors_file.absolute(), quotes_file.absolute())
    print("Seeding is done!")


if __name__ == "__main__":
    main()
