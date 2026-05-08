from unittest.mock import patch
from model.order import Order, OrderStatus
from view import order_view


def test_get_order_input():
    with patch("builtins.input", side_effect=["S001", "Alice", "10"]):
        result = order_view.get_order_input()
    assert result == {"sample_id": "S001", "customer_name": "Alice", "quantity": 10}


def test_show_order_list_empty(capsys):
    order_view.show_order_list([])
    assert "없습니다" in capsys.readouterr().out


def test_show_order_list_with_items(capsys):
    o = Order("o1234567", "S001", "Alice", 5, OrderStatus.RESERVED)
    order_view.show_order_list([o])
    out = capsys.readouterr().out
    assert "o1234567" in out
    assert "Alice" in out


def test_get_order_id_input_default_prompt():
    with patch("builtins.input", return_value="  abc12345  ") as mock_input:
        result = order_view.get_order_id_input()
    assert result == "abc12345"
    mock_input.assert_called_once_with("주문 ID: ")


def test_get_order_id_input_custom_prompt():
    with patch("builtins.input", return_value="xyz"):
        result = order_view.get_order_id_input("승인할 주문 ID: ")
    assert result == "xyz"
