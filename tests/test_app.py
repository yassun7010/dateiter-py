from datetime import datetime

import pytest

from dateiter import DEFAULT_DATE_FORMAT
from dateiter.__main__ import App


class TestApp:
    def test_no_args(self, capsys: pytest.CaptureFixture):
        App.run()

        assert [date for date in capsys.readouterr().out.split("\n") if date != ""] == [
            datetime.today().strftime(DEFAULT_DATE_FORMAT)
        ]

    @pytest.mark.parametrize(
        "args",
        [
            ["2020-01-01", "2020-01-05"],
            ["2020-01-01", "--end-date", "2020-01-05"],
            ["--start-date", "2020-01-01", "--end-date", "2020-01-05"],
        ],
    )
    def test_date_input(self, capsys: pytest.CaptureFixture, args: list[str]):
        App.run(args)

        assert [date for date in capsys.readouterr().out.split("\n") if date != ""] == [
            "2020-01-01",
            "2020-01-02",
            "2020-01-03",
            "2020-01-04",
        ]

    @pytest.mark.parametrize(
        "format",
        ["%Y-%m-%d", "%Y/%m/%d"],
    )
    def test_input_format(self, capsys: pytest.CaptureFixture, format: str):
        today = datetime.today()

        App.run([today.strftime(format), "--input-date-format", format])

        assert [date for date in capsys.readouterr().out.split("\n") if date != ""] == [
            today.strftime(DEFAULT_DATE_FORMAT)
        ]

    @pytest.mark.parametrize(
        "format",
        ["%Y-%m-%d", "%Y/%m/%d"],
    )
    def test_output_format(self, capsys: pytest.CaptureFixture, format: str):
        today = datetime.today()

        App.run([today.strftime(DEFAULT_DATE_FORMAT), "--output-date-format", format])

        assert [date for date in capsys.readouterr().out.split("\n") if date != ""] == [
            datetime.today().strftime(format)
        ]
