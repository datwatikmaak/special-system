from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    base = PYBITES_BORN + timedelta(days=100)
    while True:
        yield base
        base = base + timedelta(days=100)


gen_special_pybites_dates()
