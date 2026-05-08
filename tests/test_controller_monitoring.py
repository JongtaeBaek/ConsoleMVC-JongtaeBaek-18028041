from unittest.mock import patch
from controller.monitoring_controller import MonitoringController


def test_show_order_status():
    ctrl = MonitoringController([], [])
    with patch("view.monitoring_view.show_order_status_summary") as mock:
        ctrl.show_order_status()
    mock.assert_called_once_with([])


def test_show_stock_status():
    ctrl = MonitoringController([], [])
    with patch("view.monitoring_view.show_stock_status") as mock:
        ctrl.show_stock_status()
    mock.assert_called_once_with([], [])
