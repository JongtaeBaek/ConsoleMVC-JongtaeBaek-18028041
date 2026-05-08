from model.order import Order, OrderStatus
from model.sample import Sample
from view import monitoring_view


def test_show_order_status_summary_empty(capsys):
    monitoring_view.show_order_status_summary([])
    assert "주문량 확인" in capsys.readouterr().out


def test_show_order_status_summary_with_orders(capsys):
    orders = [
        Order("o1", "S001", "Alice", 5, OrderStatus.RESERVED),
        Order("o2", "S001", "Bob", 3, OrderStatus.REJECTED),   # counts 미포함
        Order("o3", "S001", "Carol", 2, OrderStatus.CONFIRMED),
    ]
    monitoring_view.show_order_status_summary(orders)
    out = capsys.readouterr().out
    assert "RESERVED" in out
    assert "CONFIRMED" in out


def test_show_stock_status_yuyu(capsys):
    s = Sample("S001", "SampleA", 2.0, 0.9, stock=10)
    o = Order("o1", "S001", "Alice", 3, OrderStatus.RESERVED)
    monitoring_view.show_stock_status([s], [o])
    assert "여유" in capsys.readouterr().out


def test_show_stock_status_bujok(capsys):
    s = Sample("S001", "SampleA", 2.0, 0.9, stock=2)
    o = Order("o1", "S001", "Alice", 5, OrderStatus.RESERVED)
    monitoring_view.show_stock_status([s], [o])
    assert "부족" in capsys.readouterr().out


def test_show_stock_status_gogal(capsys):
    s = Sample("S001", "SampleA", 2.0, 0.9, stock=0)
    monitoring_view.show_stock_status([s], [])
    assert "고갈" in capsys.readouterr().out
