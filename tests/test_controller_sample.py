from unittest.mock import patch
from model.sample import Sample
from controller.sample_controller import SampleController


def test_register():
    samples = []
    ctrl = SampleController(samples)
    with patch("view.sample_view.get_sample_input", return_value={
        "sample_id": "S001", "name": "SampleA", "avg_production_time": 2.0, "yield_rate": 0.9,
    }), patch("builtins.print"):
        ctrl.register()
    assert len(samples) == 1
    assert samples[0].name == "SampleA"


def test_list_all():
    samples = [Sample("S001", "SampleA", 2.0, 0.9)]
    ctrl = SampleController(samples)
    with patch("view.sample_view.show_sample_list") as mock_show:
        ctrl.list_all()
    mock_show.assert_called_once_with(samples)


def test_search():
    samples = [Sample("S001", "SampleA", 2.0, 0.9), Sample("S002", "SampleB", 1.5, 0.8)]
    ctrl = SampleController(samples)
    with patch("view.sample_view.get_search_keyword", return_value="SampleA"), \
         patch("view.sample_view.show_search_result") as mock_result:
        ctrl.search()
    mock_result.assert_called_once_with([samples[0]])
