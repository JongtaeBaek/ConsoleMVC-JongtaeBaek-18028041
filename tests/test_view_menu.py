from unittest.mock import patch
from view import menu_view


def test_show_main_menu(capsys):
    menu_view.show_main_menu()
    out = capsys.readouterr().out
    assert "S-Semi" in out
    assert "0. 종료" in out


def test_show_sample_menu(capsys):
    menu_view.show_sample_menu()
    assert "시료 관리" in capsys.readouterr().out


def test_show_order_menu(capsys):
    menu_view.show_order_menu()
    assert "시료 주문" in capsys.readouterr().out


def test_show_approval_menu(capsys):
    menu_view.show_approval_menu()
    assert "주문 승인/거절" in capsys.readouterr().out


def test_show_monitoring_menu(capsys):
    menu_view.show_monitoring_menu()
    assert "모니터링" in capsys.readouterr().out


def test_show_production_menu(capsys):
    menu_view.show_production_menu()
    assert "생산 라인 조회" in capsys.readouterr().out


def test_show_release_menu(capsys):
    menu_view.show_release_menu()
    assert "출고 처리" in capsys.readouterr().out


def test_get_choice_default_prompt():
    with patch("builtins.input", return_value="  2  ") as mock_input:
        result = menu_view.get_choice()
    assert result == "2"
    mock_input.assert_called_once_with("선택: ")


def test_get_choice_custom_prompt():
    with patch("builtins.input", return_value="1"):
        result = menu_view.get_choice("입력: ")
    assert result == "1"
