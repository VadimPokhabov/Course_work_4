import pytest

from src.get_vacancies_api_hh import GetHeadHunter


@pytest.fixture
def test_get_hh():
    return GetHeadHunter("python", 1)


def test_str(test_get_hh):
    assert str(test_get_hh) == "python"


def test_repr(test_get_hh):
    assert repr(test_get_hh) == 'GetHeadHunter(python, 1)'


def test_url(test_get_hh):
    assert test_get_hh.url == "https://api.hh.ru"


def test_error_connection():
    with pytest.raises(TypeError):
        GetHeadHunter()
