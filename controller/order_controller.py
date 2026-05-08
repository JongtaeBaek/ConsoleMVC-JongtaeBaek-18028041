import uuid
from model.order import Order, OrderStatus
from model.sample import Sample
from model.production import ProductionJob, ProductionQueue
from view import order_view


class OrderController:
    def __init__(self, samples: list[Sample], orders: list[Order], production_queue: ProductionQueue):
        self._samples = samples
        self._orders = orders
        self._queue = production_queue

    def reserve(self):
        data = order_view.get_order_input()
        order = Order(
            order_id=str(uuid.uuid4())[:8],
            status=OrderStatus.RESERVED,
            **data,
        )
        self._orders.append(order)
        print(f"주문 접수 완료. (주문ID: {order.order_id})")

    def list_reserved(self):
        reserved = [o for o in self._orders if o.status == OrderStatus.RESERVED]
        order_view.show_order_list(reserved)

    def approve(self):
        self.list_reserved()
        order_id = order_view.get_order_id_input("승인할 주문 ID: ")
        order = self._find_order(order_id, OrderStatus.RESERVED)
        if not order:
            print("해당 주문을 찾을 수 없습니다.")
            return

        sample = next((s for s in self._samples if s.sample_id == order.sample_id), None)
        if not sample:
            print("시료 정보를 찾을 수 없습니다.")
            return

        if sample.stock >= order.quantity:
            sample.stock -= order.quantity
            order.status = OrderStatus.CONFIRMED
            print("재고 충분 → 주문 CONFIRMED 처리.")
        else:
            import math
            shortage = order.quantity - sample.stock
            actual = math.ceil(shortage / (sample.yield_rate * 0.9))
            job = ProductionJob(
                order_id=order.order_id,
                sample_id=order.sample_id,
                required_quantity=shortage,
                actual_production=actual,
                total_time=sample.avg_production_time * actual,
            )
            self._queue.enqueue(job)
            order.status = OrderStatus.PRODUCING
            print(f"재고 부족 → 생산 등록 (생산량: {actual}개, 예상시간: {job.total_time:.1f}h). 주문 PRODUCING 처리.")

    def reject(self):
        self.list_reserved()
        order_id = order_view.get_order_id_input("거절할 주문 ID: ")
        order = self._find_order(order_id, OrderStatus.RESERVED)
        if not order:
            print("해당 주문을 찾을 수 없습니다.")
            return
        order.status = OrderStatus.REJECTED
        print("주문 REJECTED 처리.")

    def _find_order(self, order_id: str, status: OrderStatus) -> Order | None:
        return next((o for o in self._orders if o.order_id == order_id and o.status == status), None)
