import pytest
from project import getCountryName, getCountry, additionalInfo, getChoice


def test_get_country():

    result = getCountry("United States")
    result = getCountry("Croatia")
    result = getCountry("Italy")
    result = getCountry('')

    assert result


def test_getCountryName(monkeypatch):
    user_input = "United States\n"


    monkeypatch.setattr('builtins.input', lambda _: user_input)

    result = getCountryName()


    assert result == "united states"


def test_additionalInfo(monkeypatch):

    monkeypatch.setattr('builtins.input', lambda _: '3\n')

    result = additionalInfo()
    assert result == 3

class MockCountry:
    def currencies(self):
        return "Mock currencies"


def test_getChoice():
    country = MockCountry()
    result = getChoice(1, country)
    assert result == "Mock currencies"


