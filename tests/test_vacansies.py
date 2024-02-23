import pytest

from src.vacancies import Vacancy

@pytest.fixture
def test_vacancy():
    return Vacancy("python", 1)


def test_str(test_vacancy):
    assert str(test_vacancy) == "python"


def test_repr(test_vacancy):
    assert repr(test_vacancy) == "Vacancy(('python', 1))"


def test_name_error(test_vacancy):
    with pytest.raises(AttributeError):
        test_vacancy.name = "qwe"


def test_page_error(test_vacancy):
    with pytest.raises(AttributeError):
        test_vacancy.page = 1
