# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 현재 작업: 1.1.1 MVC 스켈레톤 코드 (PoC)

**목적**: 1.2 프로젝트 개발을 위한 PoC 단계. 과도한 구현 없이 MVC 구조와 역할 분리가 동작함을 확인하는 것이 목표.

Git 저장소: https://github.com/JongtaeBaek/ConsoleMVC-JongtaeBaek-18028041.git

## 개발 환경

- Python 3.14 (`.venv` 가상환경)
- 앱 의존성: 표준 라이브러리만 사용
- 개발 의존성: `pytest`, `pytest-cov`

```bash
.venv\Scripts\activate
pip install pytest pytest-cov

python main.py

# 테스트 실행 (커버리지 100% 강제 + HTML 리포트 자동 산출)
pytest
```

HTML 커버리지 리포트: `htmlcov/index.html` (`pytest.ini`의 `addopts`에 고정)

## 구현된 구조

```
ConsoleMVC/
├── main.py
├── model/
│   ├── sample.py       # Sample 데이터 클래스
│   ├── order.py        # Order 데이터 클래스 + OrderStatus Enum
│   └── production.py   # ProductionJob, ProductionQueue
├── view/
│   ├── menu_view.py    # 메인/서브 메뉴 출력
│   ├── sample_view.py
│   ├── order_view.py
│   └── monitoring_view.py
└── controller/
    ├── sample_controller.py
    ├── order_controller.py
    ├── monitoring_controller.py
    ├── production_controller.py
    └── release_controller.py
```

## MVC 역할 분리 원칙

- **Model**: 데이터 구조 정의만 (비즈니스 로직 없음)
- **View**: 출력 및 입력 수집만 (데이터 가공 없음)
- **Controller**: Model과 View를 연결하는 흐름 제어
- 의존 방향: `View → Controller → Model` (역방향 금지)

## 도메인 모델 및 구현 결정 사항

**Sample**
- 필드: `sample_id`, `name`, `avg_production_time`(시간), `yield_rate`(0.0~1.0), `stock`(재고 수량)
- 재고(`stock`)는 Sample 모델에 포함

**Order**
- 필드: `order_id`, `sample_id`, `customer_name`, `quantity`, `status`(OrderStatus)
- `order_id`: `uuid4()` 앞 8자리 자동 생성

**OrderStatus** (Enum)
```
RESERVED → (승인+재고충분) → CONFIRMED → RELEASE
         → (승인+재고부족) → PRODUCING → CONFIRMED → RELEASE
         → (거절)          → REJECTED  (모니터링 제외)
```

**ProductionJob**
- 필드: `order_id`, `sample_id`, `required_quantity`(부족분), `actual_production`, `total_time`
- 생산량 공식: `actual_production = ceil(required_quantity / (yield_rate × 0.9))`
- 총 생산 시간: `total_time = avg_production_time × actual_production`
- 공식 위치: 현재 `OrderController.approve()` 내부에 구현

**ProductionQueue**
- FIFO 방식, `collections.deque` 사용
- 시료 하나씩 순차 생산

## 현재 데이터 저장 방식 (한계)

모든 데이터는 **인메모리 Python 리스트**로만 관리되며 프로그램 종료 시 소멸한다.

- `samples: list[Sample]` — 1.1.2에서 `samples.json`으로 영속화 예정
- `orders: list[Order]` — 1.1.2에서 `orders.json`으로 영속화 예정
- `ProductionQueue` — 별도 영속화 없이 주문 상태(`PRODUCING`)로 복원 가능

## 테스트 전략

**목표**: 코드 커버리지 100%

**프레임워크**: `pytest` + `pytest-cov`

**리포트**: `pytest` 실행 시 `htmlcov/index.html` 자동 생성 (`addopts` 고정)

**테스트 위치**: `tests/` 디렉터리

```
tests/
├── test_model_sample.py
├── test_model_order.py
├── test_model_production.py
├── test_view_menu.py
├── test_view_sample.py
├── test_view_order.py
├── test_view_monitoring.py
├── test_controller_sample.py
├── test_controller_order.py
├── test_controller_monitoring.py
├── test_controller_production.py
├── test_controller_release.py
└── test_main.py
```

**레이어별 테스트 방식**

- **Model**: 필드 초기화, Enum 값, `ProductionQueue` 메서드(`enqueue`/`dequeue`/`peek`/`all`/`is_empty`) 직접 호출
- **View**: `unittest.mock.patch`로 `builtins.input` / `builtins.print` 모킹 — 입력값 주입 및 출력 검증
- **Controller**: View 함수와 `input`을 모킹하여 Controller 메서드의 상태 변화(`status`, `stock`, `queue`) 검증
- **main.py**: 메뉴 루프의 각 분기(`"0"`~`"6"`)를 `side_effect` 리스트로 순서 제어하여 커버

**커버리지 제외 대상**: 없음 (`# pragma: no cover` 사용 금지)

## 메인 메뉴 구조

1. 시료 관리 (등록 / 조회 / 검색)
2. 시료 주문 (예약)
3. 주문 승인/거절 (목록 / 승인 / 거절)
4. 모니터링 (주문량 확인 / 재고량 확인)
5. 생산 라인 조회 (생산 현황 / 대기 주문)
6. 출고 처리 (목록 / 출고)
0. 종료
