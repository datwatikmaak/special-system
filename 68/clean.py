PUNCTUATION = list(map(str, "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"))


def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    input_string = list(map(str, input_string))
    return "".join([char for char in input_string if char not in PUNCTUATION])
