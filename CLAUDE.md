# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 현재 작업: 1.1.1 MVC 스켈레톤 코드 (PoC)

**목적**: 1.2 프로젝트 개발을 위한 PoC 단계. 과도한 구현 없이 MVC 구조와 역할 분리가 동작함을 확인하는 것이 목표.

Model/Controller/View 패키지 구조와 역할 분리를 완성하는 단계. 실제 비즈니스 로직 없이 구조와 인터페이스만 정의한다.

Git 저장소: https://github.com/JongtaeBaek/ConsoleMVC-JongtaeBaek-18028041.git

## 개발 환경

- Python 3.14 (`.venv` 가상환경)
- 외부 의존성 없음 (표준 라이브러리만 사용)

```bash
# 가상환경 활성화 (Windows)
.venv\Scripts\activate

# 실행
python main.py
```

## 목표 디렉터리 구조

```
ConsoleMVC/
├── main.py
├── model/
│   ├── __init__.py
│   ├── sample.py       # Sample 데이터 클래스
│   ├── order.py        # Order 데이터 클래스 + OrderStatus Enum
│   └── production.py   # ProductionLine, ProductionQueue
├── view/
│   ├── __init__.py
│   ├── menu_view.py    # 메인/서브 메뉴 출력
│   ├── sample_view.py
│   ├── order_view.py
│   └── monitoring_view.py
└── controller/
    ├── __init__.py
    ├── sample_controller.py
    ├── order_controller.py
    ├── production_controller.py
    └── release_controller.py
```

## MVC 역할 분리 원칙

- **Model**: 데이터 구조 정의만 (비즈니스 로직 없음)
- **View**: 출력 및 입력 수집만 (데이터 가공 없음)
- **Controller**: Model과 View를 연결하는 흐름 제어
- 의존 방향: `View → Controller → Model` (역방향 금지)

## 도메인 모델 요약

**Sample**: 시료 ID, 이름, 평균 생산시간, 수율

**Order**: 주문 ID, 시료 ID, 고객명, 주문 수량, 상태(OrderStatus)

**OrderStatus** (Enum):
- `RESERVED` → `CONFIRMED` / `PRODUCING` → `CONFIRMED` → `RELEASE`
- `REJECTED` (비정상 흐름)

**ProductionQueue**: FIFO 방식, 시료 하나씩 순차 생산

## 메인 메뉴 항목 (스켈레톤 수준)

1. 시료 관리
2. 시료 주문
3. 주문 승인/거절
4. 모니터링
5. 생산 라인 조회
6. 출고 처리
0. 종료
