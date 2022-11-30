import pytest

from springdata.domain import Page, PageRequest


@pytest.fixture
def page():
    return Page([1, 2, 3], PageRequest(page=1, size=10), 13)


def test_should_raise_value_error_when_page_content_is_none():
    with pytest.raises(ValueError):
        Page(None)


def test_should_create_page_with_only_content():
    result = Page([1, 2, 3])
    assert result.pageable.is_unpaged()
    assert result.total_elements == 3


def test_should_create_page_with_adapted_total():
    result = Page([1, 2, 3], PageRequest(page=1, size=10), 10)
    assert result.pageable.is_paged()
    assert result.total_elements == 13


def test_should_create_empty_page():
    result = Page.empty()
    assert len(result.content) == 0


def test_should_return_page_number(page):
    assert page.number == 1
    assert Page(content=[1, 2, 3]).number == 0


def test_should_return_number_of_elements(page):
    assert page.number_of_elements == 3


def test_should_return_page_size(page):
    assert page.size == 10
    assert Page(content=[1, 2, 3]).size == 3


def test_should_return_total_pages(page):
    assert page.total_pages == 2
    assert Page.empty().total_pages == 1


def test_should_return_if_page_has_content(page):
    assert page.has_content()
    assert not Page.empty().has_content()


def test_should_return_if_page_has_next(page):
    assert not page.has_next()
    assert not Page.empty().has_next()


def test_should_return_if_page_has_previous(page):
    assert page.has_previous()
    assert not Page.empty().has_previous()


def test_should_return_if_first_page(page):
    assert not page.is_first()
    assert Page.empty().is_first()


def test_should_return_if_last_page(page):
    assert page.is_last()
    assert Page.empty().is_last()


def test_should_return_next_pageable(page):
    assert page.next_pageable().is_unpaged()


def test_should_return_previous_pageable(page):
    assert page.previous_pageable().is_paged()
