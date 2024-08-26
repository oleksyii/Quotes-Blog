from datetime import datetime


def parse_date(date_in_string: str):
    # Convert the date string to a datetime object
    return datetime.strptime(date_in_string, "%B %d, %Y")
