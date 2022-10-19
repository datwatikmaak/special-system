import json
import os
from pathlib import Path
from urllib.request import urlretrieve

TMP = Path(os.getenv("TMP", "/tmp"))
S3 = "https://bites-data.s3.us-east-2.amazonaws.com/"
DATA = "omdb_data"

DATA_LOCAL = TMP / DATA
if not Path(DATA_LOCAL).exists():
    urlretrieve(S3 + DATA, DATA_LOCAL)


def movies():
    files = []
    with open(DATA_LOCAL) as f:
        for i, line in enumerate(f.readlines(), 1):
            movie_json = TMP / f"{i}.json"
            with open(movie_json, "w") as f:
                f.write(f"{line}\n")
            files.append(movie_json)

    return files


movies()


def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    data = []
    for file in files:
        with open(file) as f:
            data.append(json.load(f))

    return data


def get_single_comedy(movies: list) -> str:
    """return the movie with Comedy in Genres"""
    for movie in movies:
        if "Comedy" in movie["Genre"]:
            return movie["Title"]


get_single_comedy(get_movie_data(movies()))


def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""
    movie_data = {}
    for movie in movies:
        numbers = movie["Awards"]
        movie_data[movie["Title"]] = [int(s) for s in numbers.split() if s.isdigit()]

    max_nominations = max((max(movie_data[key]) for key in movie_data))

    for key, value in movie_data.items():
        if max_nominations in value:
            return key


get_movie_most_nominations(get_movie_data(movies()))


def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""
    movie_runtime = {}
    for movie in movies:
        numbers = movie["Runtime"]
        movie_runtime[movie["Title"]] = [int(s) for s in numbers.split() if s.isdigit()]

    max_nominations = max((max(movie_runtime[key]) for key in movie_runtime))

    for key, value in movie_runtime.items():
        if max_nominations in value:
            return key


get_movie_longest_runtime(get_movie_data(movies()))
