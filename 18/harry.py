import os
import re
import urllib.request
from collections import Counter

# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, "stopwords")
harry_text = os.path.join(tmp, "harry")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt", stopwords_file
)
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/harry.txt", harry_text
)

with open(stopwords_file) as file:
    stopwords = file.read().splitlines()

with open(harry_text, encoding="utf8") as file:
    text = file.read().splitlines()


def get_harry_most_common_word():
    lowercased_text = [line.lower() for line in text]

    stripped_text = [re.sub(r"[^A-Za-z0-9 ]+", "", word) for word in lowercased_text]

    word_lists = [word.split() for word in stripped_text]

    flat_list = [item for sublist in word_lists for item in sublist]

    no_stopwords = [word for word in flat_list if word not in stopwords]

    c = Counter(no_stopwords)
    return c.most_common(1)[0]


get_harry_most_common_word()
