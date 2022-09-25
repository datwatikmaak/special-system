import textwrap
from itertools import groupby

INDENTS = 4


def print_hanging_indents(poem):
    stripped_text = [line.strip() for line in poem.split("\n")]
    grouped_text = [list(sub) for ele, sub in groupby(stripped_text, key=bool) if ele]

    first_lines = [line[0] for line in grouped_text]

    formatted_poem = []
    for line in stripped_text:
        if line in first_lines:
            formatted_poem.append(str(line))
        else:
            formatted_poem.append(textwrap.indent(str(line), INDENTS * " "))

    formatted_poem_string = "\n".join(formatted_poem).lstrip()

    print("\n".join(item for item in formatted_poem_string.split("\n") if item))
