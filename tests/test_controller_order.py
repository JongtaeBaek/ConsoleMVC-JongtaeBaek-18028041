from unittest.mock import patch
from model.sample import Sample
from model.order import Order, OrderStatus
from model.production import ProductionQueue
from controller.order_controller import OrderController


def _setup(stock=10):
    sample = Sample("S001", "SampleA", 2.0, 0.9, stock=stock)
    samples = [sample]
    orders = []
    queue = ProductionQueue()
    ctrl = OrderController(samples, orders, queue)
    return ctrl, sample, orders, queue


def test_reserve():
    ctrl, _, orders, _ = _setup()
    with patch("view.order_view.get_order_input", return_value={
        "sample_id": "S001", "customer_name": "Alice", "quantity": 3,
    }), patch("builtins.print"):
        ctrl.reserve()
    assert len(orders) == 1
    assert orders[0].status == OrderStatus.RESERVED
    assert orders[0].customer_name == "Alice"


def test_list_reserved():
    ctrl, _, orders, _ = _setup()
    o = Order("o1", "S001", "Alice", 3, OrderStatus.RESERVED)
    orders.append(o)
    with patch("view.order_view.show_order_list") as mock_show:
        ctrl.list_reserved()
    mock_show.assert_called_once_with([o])


def test_approve_order_not_found():
    ctrl, _, _, _ = _setup()
    with patch("view.order_view.show_order_list"), \
         patch("view.order_view.get_order_id_input", return_value="notexist"), \
         patch("builtins.print") as mock_print:
        ctrl.approve()
    mock_print.assert_any_call("해당 주문을 찾을 수 없습니다.")


def test_approve_sample_not_found():
    ctrl, _, orders, _ = _setup()
    orders.append(Order("o1", "S999", "Alice", 3, OrderStatus.RESERVED))
    with patch("view.order_view.show_order_list"), \
         patch("view.order_view.get_order_id_input", return_value="o1"), \
         patch("builtins.print") as mock_print:
        ctrl.approve()
    mock_print.assert_any_call("시료 정보를 찾을 수 없습니다.")


def test_approve_stock_sufficient():
    ctrl, sample, orders, _ = _setup(stock=10)
    o = Order("o1", "S001", "Alice", 3, OrderStatus.RESERVED)
    orders.append(o)
    with patch("view.order_view.show_order_list"), \
         patch("view.order_view.get_order_id_input", return_value="o1"), \
         patch("builtins.print"):
        ctrl.approve()
    assert o.status == OrderStatus.CONFIRMED
    assert sample.stock == 7


def test_approve_stock_insufficient():
    ctrl, sample, orders, queue = _setup(stock=2)
    o = Order("o1", "S001", "Alice", 10, OrderStatus.RESERVED)
    orders.append(o)
    with patch("view.order_view.show_order_list"), \
         patch("view.order_view.get_order_id_input", return_value="o1"), \
         patch("builtins.print"):
        ctrl.approve()
    assert o.status == OrderStatus.PRODUCING
    assert not queue.is_empty()
    job = queue.peek()
    assert job.required_quantity == 8  # 10 - 2


def test_reject_order_not_found():
    ctrl, _, _, _ = _setup()
    with patch("view.order_view.show_order_list"), \
         patch("view.order_view.get_order_id_input", return_value="notexist"), \
         patch("builtins.print") as mock_print:
        ctrl.reject()
    mock_print.assert_any_call("해당 주문을 찾을 수 없습니다.")


def test_reject_success():
    ctrl, _, orders, _ = _setup()
    o = Order("o1", "S001", "Alice", 3, OrderStatus.RESERVED)
    orders.append(o)
    with patch("view.order_view.show_order_list"), \
         patch("view.order_view.get_order_id_input", return_value="o1"), \
         patch("builtins.print"):
        ctrl.reject()
    assert o.status == OrderStatus.REJECTED
