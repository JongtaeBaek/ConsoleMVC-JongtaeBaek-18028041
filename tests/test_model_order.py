from model.order import Order, OrderStatus


def test_order_status_values():
    assert OrderStatus.RESERVED.value == "RESERVED"
    assert OrderStatus.REJECTED.value == "REJECTED"
    assert OrderStatus.PRODUCING.value == "PRODUCING"
    assert OrderStatus.CONFIRMED.value == "CONFIRMED"
    assert OrderStatus.RELEASE.value == "RELEASE"


def test_order_default_status():
    o = Order("o1", "S001", "Alice", 5)
    assert o.order_id == "o1"
    assert o.sample_id == "S001"
    assert o.customer_name == "Alice"
    assert o.quantity == 5
    assert o.status == OrderStatus.RESERVED


def test_order_custom_status():
    o = Order("o1", "S001", "Alice", 5, status=OrderStatus.CONFIRMED)
    assert o.status == OrderStatus.CONFIRMED
