import pytest

from springdata.domain.pageable import PageRequest


def test_should_raise_value_error_when_page_index_lower_than_zero():
    with pytest.raises(ValueError):
        PageRequest(page=-1, size=1)


def test_should_raise_value_error_when_page_size_lower_than_one():
    with pytest.raises(ValueError):
        PageRequest(page=0, size=0)


def test_should_create_page_request_of_size():
    result = PageRequest.of_size(10)
    assert result.page_size == 10
    assert result.page_number == 0


def test_should_return_first_page_request():
    result = PageRequest(page=3, size=10).first()
    assert result.page_number == 0
    assert result.page_size == 10


def test_should_return_page_request_offset():
    result = PageRequest(page=3, size=10)
    assert result.offset == 30


def test_should_return_next_page_request():
    result = PageRequest(page=3, size=10).next()
    assert result.page_number == 4
    assert result.page_size == 10


def test_should_return_previous_page_request():
    page_request = PageRequest(page=3, size=10).previous_or_first()
    assert page_request.page_number == 2
    assert page_request.page_size == 10

    page_request = PageRequest(page=0, size=10).previous_or_first()
    assert page_request.page_number == 0
    assert page_request.page_size == 10


def test_should_return_if_page_request_has_previous():
    assert PageRequest(page=3, size=10).has_previous()
    assert not PageRequest(page=0, size=10).has_previous()
