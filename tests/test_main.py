import sys
from unittest import mock
import pytest


from main import main

import os

os.environ['OPENWEATHER_API_KEY'] = '795942ee82638d94515ea737ff88feb6'


@pytest.mark.parametrize("args", [
    ["--zip", "32216", "--forecast"],
    ["--zip", "32202", "--diag", "--with_data"],
])
def test_main_with_args(args):
    with mock.patch.object(sys, 'argv', ["main.py"] + args):
        main()


def test_main_missing_zip_code():
    with mock.patch.object(sys, 'argv', ["main.py", "--forecast"]):
        with pytest.raises(SystemExit):
            main()


def test_main_invalid_zip_code():
    with mock.patch.object(sys, 'argv', ["main.py", "--zip", "abc"]):
        with pytest.raises(SystemExit):
            main()
