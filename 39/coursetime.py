from datetime import datetime, timedelta
import os
import re
from typing import List
import urllib.request

# getting the data
COURSE_TIMES = os.path.join(os.getenv("TMP", "/tmp"), "course_timings")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/course_timings", COURSE_TIMES
)


def get_all_timestamps() -> List[str]:
    """Read in the COURSE_TIMES and extract all MM:SS timestamps.
    Here is a snippet of the input file:

    Start  What is Practical JavaScript? (3:47)
    Start  The voice in your ear (4:41)
    Start  Is this course right for you? (1:21)
    ...

     Return a list of MM:SS timestamps
    """
    with open(COURSE_TIMES) as file:
        content = " ".join(file.read().splitlines()).split()

    return [line.strip("()") for line in content if line.startswith("(")]


def calc_total_course_duration(timestamps) -> str:
    """Takes timestamps list as returned by get_all_timestamps
    and calculates the total duration as HH:MM:SS"""
    total_time = timedelta()
    for t in timestamps:
        (m, s) = t.split(":")
        d = timedelta(minutes=int(m), seconds=int(s))
        total_time += d

    return str(total_time)
