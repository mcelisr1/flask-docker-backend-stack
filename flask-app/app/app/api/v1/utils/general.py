# -*- coding: utf-8 -*-

# Import standard library packages
from datetime import datetime
import pytz


def datetime_now(
    timezone="America/Bogota",
    to_format='%Y-%m-%d %H:%M:%S.%f',
    to_str=False
):
    datetime_str = datetime.now(pytz.timezone(timezone)).strftime(to_format)
    if to_str:
        return datetime_str

    datetime_new = datetime.strptime(datetime_str, to_format)

    return datetime_new
