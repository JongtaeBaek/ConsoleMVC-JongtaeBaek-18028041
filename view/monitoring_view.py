from model.order import Order, OrderStatus
from model.sample import Sample


def show_order_status_summary(orders: list[Order]):
    print("\n[ 주문량 확인 ]")
    counts = {s: 0 for s in OrderStatus if s != OrderStatus.REJECTED}
    for o in orders:
        if o.status in counts:
            counts[o.status] += 1
    for status, count in counts.items():
        print(f"  {status.value:<12}: {count}건")


def show_stock_status(samples: list[Sample], orders: list[Order]):
    print("\n[ 재고량 확인 ]")
    print(f"{'시료ID':<10} {'이름':<15} {'재고':>6}  상태")
    print("-" * 45)
    for s in samples:
        reserved = sum(
            o.quantity for o in orders
            if o.sample_id == s.sample_id and o.status in (OrderStatus.RESERVED, OrderStatus.CONFIRMED)
        )
        if s.stock == 0:
            label = "고갈"
        elif s.stock < reserved:
            label = "부족"
        else:
            label = "여유"
        print(f"{s.sample_id:<10} {s.name:<15} {s.stock:>6}  {label}")
