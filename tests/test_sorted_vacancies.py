import pytest
from src.get_vacancies_api_hh import GetHeadHunter
from src.sorted_vacancies import SortedVacancy


@pytest.fixture
def test_get_hh():
    return GetHeadHunter("python", 1)


def test_sorted_vacancy(test_get_hh):
    r = SortedVacancy()
    assert r.head_hunter_sorted == []
    assert r.date_format == None


def test_sorted_vacancies_hh():
    r = SortedVacancy()
    assert (r.sorted_vacancies_hh ==
            [{'city': 'Москва',
              'currency': 'RUR',
              'date': '26.02.2024',
              'name': 'Junior программист Python',
              'payment_from': 60000,
              'payment_to': 80000,
              'requirement': 'Уверенное знание <highlighttext>Python</highlighttext>. '
                             'Уверенное знание SQL(PSQL, MSSQL). Умение работать с '
                             'FastAPI. Умение работать с Git. Знание SQLAlchemy. ',
              'responsibility': 'Поддержка микросервисов. Разработка интеграций с внешними '
                                'и внутренними сервисами. Участие в разработке моделей по '
                                'прогнозированию.',
              'url': 'https://hh.ru/vacancy/93804724'}])


def test_error_sorted_vacancy():
    with pytest.raises(TypeError):
        SortedVacancy(100)
