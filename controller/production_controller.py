from model.order import Order, OrderStatus
from model.sample import Sample
from model.production import ProductionQueue


class ProductionController:
    def __init__(self, samples: list[Sample], orders: list[Order], production_queue: ProductionQueue):
        self._samples = samples
        self._orders = orders
        self._queue = production_queue

    def show_current(self):
        job = self._queue.peek()
        print("\n[ 생산 현황 ]")
        if not job:
            print("현재 생산 중인 작업이 없습니다.")
            return
        print(f"  주문ID: {job.order_id} | 시료ID: {job.sample_id} | "
              f"생산량: {job.actual_production}개 | 예상시간: {job.total_time:.1f}h")

    def show_queue(self):
        jobs = self._queue.all()
        print("\n[ 대기 주문 확인 (FIFO) ]")
        if not jobs:
            print("대기 중인 생산 작업이 없습니다.")
            return
        print(f"{'순서':<6} {'주문ID':<12} {'시료ID':<10} {'생산량':>8} {'예상시간':>10}")
        print("-" * 50)
        for i, job in enumerate(jobs, 1):
            print(f"{i:<6} {job.order_id:<12} {job.sample_id:<10} {job.actual_production:>8} {job.total_time:>9.1f}h")
