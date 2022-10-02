import pytz
from pytz import timezone

AUSTRALIA = timezone("Australia/Sydney")
SPAIN = timezone("Europe/Madrid")


def what_time_lives_pybites(naive_utc_dt):
    """Receives a naive UTC datetime object and returns a two element
    tuple of Australian and Spanish (timezone aware) datetimes"""
    aware_datetime_utc = naive_utc_dt.replace(tzinfo=pytz.UTC)
    return aware_datetime_utc.astimezone(AUSTRALIA), aware_datetime_utc.astimezone(
        SPAIN
    )
