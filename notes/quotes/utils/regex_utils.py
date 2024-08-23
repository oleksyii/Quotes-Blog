import re


pattern = re.compile(r"\w+", re.UNICODE)


def find_all_tags(tags_string: str):
    return pattern.findall(tags_string.lower())
