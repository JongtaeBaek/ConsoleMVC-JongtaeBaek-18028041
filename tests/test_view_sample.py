from unittest.mock import patch
from model.sample import Sample
from view import sample_view


def test_get_sample_input():
    with patch("builtins.input", side_effect=["S001", "SampleA", "2.0", "0.9"]):
        result = sample_view.get_sample_input()
    assert result == {
        "sample_id": "S001",
        "name": "SampleA",
        "avg_production_time": 2.0,
        "yield_rate": 0.9,
    }


def test_show_sample_list_empty(capsys):
    sample_view.show_sample_list([])
    assert "없습니다" in capsys.readouterr().out


def test_show_sample_list_with_items(capsys):
    s = Sample("S001", "SampleA", 2.0, 0.9, stock=5)
    sample_view.show_sample_list([s])
    out = capsys.readouterr().out
    assert "S001" in out
    assert "SampleA" in out


def test_get_search_keyword():
    with patch("builtins.input", return_value="  ABC  "):
        assert sample_view.get_search_keyword() == "ABC"


def test_show_search_result_empty(capsys):
    sample_view.show_search_result([])
    assert "없습니다" in capsys.readouterr().out


def test_show_search_result_with_items(capsys):
    s = Sample("S001", "SampleA", 2.0, 0.9)
    sample_view.show_search_result([s])
    assert "S001" in capsys.readouterr().out
