from typing import Union, Generator, List, Iterable


def filter_query(param: str, data: Union[Generator, List[str]]):
    """Функция фильтрации данных."""
    return filter(lambda x: param in x, data)


def map_query(param: str, data: Iterable[str]):
    """Функция получает номер колонки и выводит данные этой колонки."""
    col_number = int(param)
    return map(lambda x: x. split(' ')[col_number], data)


def unique_query(param: str, data: Iterable[str]):
    """Функция из уникальных позиций."""
    return set(data)


def sort_query(param: str, data: Iterable[str]):
    """ Функция сортировки данных."""
    return sorted(data, reverse=param == 'desc')


def limit_query(param: str, data: Iterable[str]):
    """Функция создает позиции в заданном количестве."""
    limit = int(param)
    return data[:limit]