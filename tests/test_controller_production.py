from model.production import ProductionQueue, ProductionJob
from controller.production_controller import ProductionController


def _make_job():
    return ProductionJob("o1", "S001", 5, 6, 12.0)


def test_show_current_empty(capsys):
    ctrl = ProductionController([], [], ProductionQueue())
    ctrl.show_current()
    assert "없습니다" in capsys.readouterr().out


def test_show_current_with_job(capsys):
    q = ProductionQueue()
    q.enqueue(_make_job())
    ctrl = ProductionController([], [], q)
    ctrl.show_current()
    assert "o1" in capsys.readouterr().out


def test_show_queue_empty(capsys):
    ctrl = ProductionController([], [], ProductionQueue())
    ctrl.show_queue()
    assert "없습니다" in capsys.readouterr().out


def test_show_queue_with_jobs(capsys):
    q = ProductionQueue()
    q.enqueue(_make_job())
    ctrl = ProductionController([], [], q)
    ctrl.show_queue()
    assert "o1" in capsys.readouterr().out
