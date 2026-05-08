from model.order import Order, OrderStatus
from view import order_view


class ReleaseController:
    def __init__(self, orders: list[Order]):
        self._orders = orders

    def list_confirmed(self):
        confirmed = [o for o in self._orders if o.status == OrderStatus.CONFIRMED]
        print("\n[ 출고 가능 주문 목록 (CONFIRMED) ]")
        order_view.show_order_list(confirmed)

    def process_release(self):
        self.list_confirmed()
        order_id = order_view.get_order_id_input("출고 처리할 주문 ID: ")
        order = next((o for o in self._orders if o.order_id == order_id and o.status == OrderStatus.CONFIRMED), None)
        if not order:
            print("해당 주문을 찾을 수 없습니다.")
            return
        order.status = OrderStatus.RELEASE
        print(f"주문 {order_id} 출고 완료 → RELEASE 처리.")
