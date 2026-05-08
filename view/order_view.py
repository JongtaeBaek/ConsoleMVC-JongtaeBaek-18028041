from model.order import Order


def get_order_input() -> dict:
    print("\n[ 시료 예약 ]")
    sample_id = input("시료 ID: ").strip()
    customer_name = input("고객명: ").strip()
    quantity = input("주문 수량: ").strip()
    return {
        "sample_id": sample_id,
        "customer_name": customer_name,
        "quantity": int(quantity),
    }


def show_order_list(orders: list[Order]):
    print("\n[ 접수된 주문 목록 (RESERVED) ]")
    if not orders:
        print("접수된 주문이 없습니다.")
        return
    print(f"{'주문ID':<12} {'시료ID':<10} {'고객명':<15} {'수량':>6} {'상태':<12}")
    print("-" * 60)
    for o in orders:
        print(f"{o.order_id:<12} {o.sample_id:<10} {o.customer_name:<15} {o.quantity:>6} {o.status.value:<12}")


def get_order_id_input(prompt: str = "주문 ID: ") -> str:
    return input(prompt).strip()
