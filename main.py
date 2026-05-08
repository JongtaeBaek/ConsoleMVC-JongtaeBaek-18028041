from model.order import Order
from model.sample import Sample
from model.production import ProductionQueue
from controller.sample_controller import SampleController
from controller.order_controller import OrderController
from controller.monitoring_controller import MonitoringController
from controller.production_controller import ProductionController
from controller.release_controller import ReleaseController
from view import menu_view


def run_sample_menu(ctrl: SampleController):
    while True:
        menu_view.show_sample_menu()
        choice = menu_view.get_choice()
        if choice == "1":
            ctrl.register()
        elif choice == "2":
            ctrl.list_all()
        elif choice == "3":
            ctrl.search()
        elif choice == "0":
            break


def run_order_menu(ctrl: OrderController):
    while True:
        menu_view.show_order_menu()
        choice = menu_view.get_choice()
        if choice == "1":
            ctrl.reserve()
        elif choice == "0":
            break


def run_approval_menu(ctrl: OrderController):
    while True:
        menu_view.show_approval_menu()
        choice = menu_view.get_choice()
        if choice == "1":
            ctrl.list_reserved()
        elif choice == "2":
            ctrl.approve()
        elif choice == "3":
            ctrl.reject()
        elif choice == "0":
            break


def run_monitoring_menu(ctrl: MonitoringController):
    while True:
        menu_view.show_monitoring_menu()
        choice = menu_view.get_choice()
        if choice == "1":
            ctrl.show_order_status()
        elif choice == "2":
            ctrl.show_stock_status()
        elif choice == "0":
            break


def run_production_menu(ctrl: ProductionController):
    while True:
        menu_view.show_production_menu()
        choice = menu_view.get_choice()
        if choice == "1":
            ctrl.show_current()
        elif choice == "2":
            ctrl.show_queue()
        elif choice == "0":
            break


def run_release_menu(ctrl: ReleaseController):
    while True:
        menu_view.show_release_menu()
        choice = menu_view.get_choice()
        if choice == "1":
            ctrl.list_confirmed()
        elif choice == "2":
            ctrl.process_release()
        elif choice == "0":
            break


def main():
    samples: list[Sample] = []
    orders: list[Order] = []
    queue = ProductionQueue()

    sample_ctrl     = SampleController(samples)
    order_ctrl      = OrderController(samples, orders, queue)
    monitoring_ctrl = MonitoringController(samples, orders)
    production_ctrl = ProductionController(samples, orders, queue)
    release_ctrl    = ReleaseController(orders)

    while True:
        menu_view.show_main_menu()
        choice = menu_view.get_choice()
        if choice == "1":
            run_sample_menu(sample_ctrl)
        elif choice == "2":
            run_order_menu(order_ctrl)
        elif choice == "3":
            run_approval_menu(order_ctrl)
        elif choice == "4":
            run_monitoring_menu(monitoring_ctrl)
        elif choice == "5":
            run_production_menu(production_ctrl)
        elif choice == "6":
            run_release_menu(release_ctrl)
        elif choice == "0":
            print("시스템을 종료합니다.")
            break


if __name__ == "__main__":
    main()
