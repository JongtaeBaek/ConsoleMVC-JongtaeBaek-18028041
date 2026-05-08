def show_main_menu():
    print("\n========== S-Semi 시료 관리 시스템 ==========")
    print("1. 시료 관리")
    print("2. 시료 주문")
    print("3. 주문 승인/거절")
    print("4. 모니터링")
    print("5. 생산 라인 조회")
    print("6. 출고 처리")
    print("0. 종료")
    print("=============================================")


def show_sample_menu():
    print("\n----- 시료 관리 -----")
    print("1. 시료 등록")
    print("2. 시료 조회")
    print("3. 시료 검색")
    print("0. 뒤로")


def show_order_menu():
    print("\n----- 시료 주문 -----")
    print("1. 시료 예약")
    print("0. 뒤로")


def show_approval_menu():
    print("\n----- 주문 승인/거절 -----")
    print("1. 접수된 주문 목록")
    print("2. 주문 승인")
    print("3. 주문 거절")
    print("0. 뒤로")


def show_monitoring_menu():
    print("\n----- 모니터링 -----")
    print("1. 주문량 확인")
    print("2. 재고량 확인")
    print("0. 뒤로")


def show_production_menu():
    print("\n----- 생산 라인 조회 -----")
    print("1. 생산 현황")
    print("2. 대기 주문 확인")
    print("0. 뒤로")


def show_release_menu():
    print("\n----- 출고 처리 -----")
    print("1. 출고 가능 주문 목록")
    print("2. 출고 처리")
    print("0. 뒤로")


def get_choice(prompt: str = "선택: ") -> str:
    return input(prompt).strip()
