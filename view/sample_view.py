from model.sample import Sample


def get_sample_input() -> dict:
    print("\n[ 시료 등록 ]")
    sample_id = input("시료 ID: ").strip()
    name = input("시료 이름: ").strip()
    avg_time = input("평균 생산시간(시간): ").strip()
    yield_rate = input("수율(0.0~1.0): ").strip()
    return {
        "sample_id": sample_id,
        "name": name,
        "avg_production_time": float(avg_time),
        "yield_rate": float(yield_rate),
    }


def show_sample_list(samples: list[Sample]):
    print("\n[ 시료 목록 ]")
    if not samples:
        print("등록된 시료가 없습니다.")
        return
    print(f"{'ID':<10} {'이름':<15} {'평균생산시간':>12} {'수율':>8} {'재고':>6}")
    print("-" * 55)
    for s in samples:
        print(f"{s.sample_id:<10} {s.name:<15} {s.avg_production_time:>12.1f} {s.yield_rate:>8.2f} {s.stock:>6}")


def get_search_keyword() -> str:
    return input("검색어 (이름): ").strip()


def show_search_result(samples: list[Sample]):
    if not samples:
        print("검색 결과가 없습니다.")
        return
    show_sample_list(samples)
