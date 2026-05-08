from model.order import Order
from model.sample import Sample
from view import monitoring_view


class MonitoringController:
    def __init__(self, samples: list[Sample], orders: list[Order]):
        self._samples = samples
        self._orders = orders

    def show_order_status(self):
        monitoring_view.show_order_status_summary(self._orders)

    def show_stock_status(self):
        monitoring_view.show_stock_status(self._samples, self._orders)
