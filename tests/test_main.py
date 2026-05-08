import os
import runpy
from unittest.mock import patch, MagicMock

from main import (
    run_sample_menu, run_order_menu, run_approval_menu,
    run_monitoring_menu, run_production_menu, run_release_menu, main,
)


def test_run_sample_menu():
    ctrl = MagicMock()
    with patch("view.menu_view.show_sample_menu"), \
         patch("view.menu_view.get_choice", side_effect=["1", "2", "3", "0"]):
        run_sample_menu(ctrl)
    ctrl.register.assert_called_once()
    ctrl.list_all.assert_called_once()
    ctrl.search.assert_called_once()


def test_run_order_menu():
    ctrl = MagicMock()
    with patch("view.menu_view.show_order_menu"), \
         patch("view.menu_view.get_choice", side_effect=["1", "0"]):
        run_order_menu(ctrl)
    ctrl.reserve.assert_called_once()


def test_run_approval_menu():
    ctrl = MagicMock()
    with patch("view.menu_view.show_approval_menu"), \
         patch("view.menu_view.get_choice", side_effect=["1", "2", "3", "0"]):
        run_approval_menu(ctrl)
    ctrl.list_reserved.assert_called_once()
    ctrl.approve.assert_called_once()
    ctrl.reject.assert_called_once()


def test_run_monitoring_menu():
    ctrl = MagicMock()
    with patch("view.menu_view.show_monitoring_menu"), \
         patch("view.menu_view.get_choice", side_effect=["1", "2", "0"]):
        run_monitoring_menu(ctrl)
    ctrl.show_order_status.assert_called_once()
    ctrl.show_stock_status.assert_called_once()


def test_run_production_menu():
    ctrl = MagicMock()
    with patch("view.menu_view.show_production_menu"), \
         patch("view.menu_view.get_choice", side_effect=["1", "2", "0"]):
        run_production_menu(ctrl)
    ctrl.show_current.assert_called_once()
    ctrl.show_queue.assert_called_once()


def test_run_release_menu():
    ctrl = MagicMock()
    with patch("view.menu_view.show_release_menu"), \
         patch("view.menu_view.get_choice", side_effect=["1", "2", "0"]):
        run_release_menu(ctrl)
    ctrl.list_confirmed.assert_called_once()
    ctrl.process_release.assert_called_once()


def test_main_all_choices():
    # 메인 메뉴 1~6 진입 후 각 서브메뉴에서 즉시 "0"으로 복귀, 마지막 "0"으로 종료
    side_effects = ["1", "0", "2", "0", "3", "0", "4", "0", "5", "0", "6", "0", "0"]
    with patch("view.menu_view.get_choice", side_effect=side_effects), \
         patch("builtins.print"):
        main()


def test_main_entry_point():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with patch("view.menu_view.get_choice", return_value="0"), \
         patch("builtins.print"):
        runpy.run_path(os.path.join(root, "main.py"), run_name="__main__")
