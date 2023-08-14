from dateiter import dateiter


class TestDateiter:
    def test_range(self):
        assert [
            date.strftime("%Y-%m-%d") for date in dateiter("2020-01-01", "2020-01-05")
        ] == [
            "2020-01-01",
            "2020-01-02",
            "2020-01-03",
            "2020-01-04",
        ]
