import re

def split_on_empty_lines(s):
    # From: https://stackoverflow.com/a/57097762

    # greedily match 2 or more new-lines
    blank_line_regex = r"(?:\r?\n){2,}"

    return re.split(blank_line_regex, s.strip())