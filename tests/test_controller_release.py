from unittest.mock import patch
from model.order import Order, OrderStatus
from controller.release_controller import ReleaseController


def test_list_confirmed():
    o = Order("o1", "S001", "Alice", 3, OrderStatus.CONFIRMED)
    ctrl = ReleaseController([o])
    with patch("view.order_view.show_order_list") as mock_show, \
         patch("builtins.print"):
        ctrl.list_confirmed()
    mock_show.assert_called_once_with([o])


def test_process_release_not_found():
    ctrl = ReleaseController([])
    with patch("view.order_view.show_order_list"), \
         patch("view.order_view.get_order_id_input", return_value="notexist"), \
         patch("builtins.print") as mock_print:
        ctrl.process_release()
    mock_print.assert_any_call("해당 주문을 찾을 수 없습니다.")


def test_process_release_success():
    o = Order("o1", "S001", "Alice", 3, OrderStatus.CONFIRMED)
    ctrl = ReleaseController([o])
    with patch("view.order_view.show_order_list"), \
         patch("view.order_view.get_order_id_input", return_value="o1"), \
         patch("builtins.print"):
        ctrl.process_release()
    assert o.status == OrderStatus.RELEASE
