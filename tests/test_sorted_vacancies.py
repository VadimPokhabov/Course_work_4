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
            [{'city': 'Санкт-Петербург',
              'currency': 'RUR',
              'date': '26.01.2024',
              'name': 'Middle Python Developer',
              'payment_from': 100000,
              'payment_to': 120000,
              'requirement': 'От 2-х лет коммерческого опыта, знаешь что такое SOLID, DRY, '
                             'KISS, интересуешься паттернами проектирования. Знаешь '
                             '<highlighttext>Python</highlighttext> 3.8. ',
              'responsibility': 'Участвовать во всех этапах разработки в составе '
                                'scrum-команды: собирать и анализировать требования, '
                                'декомпозировать и оценивать задачи, писать код, '
                                'релизить...'}])


def test_error_sorted_vacancy():
    with pytest.raises(TypeError):
        SortedVacancy(100)
