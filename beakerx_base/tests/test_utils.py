from email import utils
import json
from datetime import date, datetime

import pytest
from pandas import Timestamp

from ..utils import ObjectEncoder, date_to_int

@pytest.mark.parametrize("obj,expected", (
    (date(2021, 10, 22), '{"type": "Date", "timestamp": 1634860800000}'),
    (datetime(2021, 10, 22, 5, 38, 42), '{"type": "Date", "timestamp": 1634881122000}'),
    (Timestamp(datetime(2021, 10, 22, 5, 38, 42)), '{"type": "Date", "timestamp": 1634881122000}'),
))
def test_ObjectEncoder(obj, expected):
    assert json.dumps(obj, cls=ObjectEncoder) == expected
