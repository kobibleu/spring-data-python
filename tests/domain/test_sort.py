import pytest

from springdata.domain.sort import Direction, Order, Sort


def test_direction_should_be_ascending():
    assert Direction.ASC.is_ascending()
    assert not Direction.DESC.is_ascending()


def test_direction_should_be_descending():
    assert Direction.DESC.is_descending()
    assert not Direction.DESC.is_ascending()


def test_should_return_direction_by_specified_name():
    assert Direction.value_of("DESC") == Direction.DESC
    assert Direction.value_of("ASC") == Direction.ASC
    assert Direction.value_of("desc") == Direction.DESC
    assert Direction.value_of("asc") == Direction.ASC


def test_should_raise_value_error_when_wrong_direction_name():
    with pytest.raises(ValueError):
        Direction.value_of("toto")


def test_should_return_direction_values():
    assert len(Direction.values()) == 2
    assert Direction.ASC in Direction.values()
    assert Direction.DESC in Direction.values()


def test_should_raise_value_if_order_miss_property():
    with pytest.raises(ValueError):
        Order("")


def test_should_create_order_by_property():
    result = Order.by("key")
    assert result.property == "key"
    assert result.direction == Direction.ASC


def test_should_create_ascending_order():
    result = Order.asc("key")
    assert result.property == "key"
    assert result.direction == Direction.ASC


def test_should_create_descending_order():
    result = Order.desc("key")
    assert result.property == "key"
    assert result.direction == Direction.DESC


def test_order_should_be_ascending():
    assert Order.asc("key").is_ascending()


def test_order_should_be_descending():
    assert Order.desc("key").is_descending()


def test_create_order_with_new_direction():
    assert Order.desc("key").with_direction(Direction.ASC).is_ascending()


def test_create_order_with_new_property():
    assert Order.desc("key").with_property("new_key").property == "new_key"


def test_should_create_sort_by_properties():
    result = Sort.by("key1", "key2")
    assert len(result.orders) == 2
    assert result.orders[0].property == "key1"
    assert result.orders[0].direction == Direction.ASC
    assert result.orders[1].property == "key2"
    assert result.orders[1].direction == Direction.ASC


def test_should_create_sort_by_properties_and_direction():
    result = Sort.by("key1", "key2", direction=Direction.DESC)
    assert len(result.orders) == 2
    assert result.orders[0].property == "key1"
    assert result.orders[0].direction == Direction.DESC
    assert result.orders[1].property == "key2"
    assert result.orders[1].direction == Direction.DESC


def test_should_create_unsorted():
    result = Sort.unsorted()
    assert len(result.orders) == 0


def test_should_change_sort_direction():
    result = Sort.by("key1", "key2", direction=Direction.DESC).ascending()
    assert result.orders[0].direction == Direction.ASC
    assert result.orders[1].direction == Direction.ASC

    result.descending()
    assert result.orders[0].direction == Direction.DESC
    assert result.orders[1].direction == Direction.DESC


def test_should_combine_sorts():
    result = Sort.by("key1", "key2").and_(Sort.by("key3", "key4"))
    assert len(result.orders) == 4


def test_should_get_order_for_property():
    result = Sort.by("key1", "key2").get_order_for("key1")
    assert result.property == "key1"


def test_should_create_sort_with_new_direction():
    result = Sort.by("key1", "key2", direction=Direction.DESC).with_direction(
        Direction.ASC
    )
    assert result.orders[0].direction == Direction.ASC
    assert result.orders[1].direction == Direction.ASC
