from model.sample import Sample


def test_sample_default_stock():
    s = Sample("S001", "SampleA", 2.0, 0.9)
    assert s.sample_id == "S001"
    assert s.name == "SampleA"
    assert s.avg_production_time == 2.0
    assert s.yield_rate == 0.9
    assert s.stock == 0


def test_sample_with_stock():
    s = Sample("S001", "SampleA", 2.0, 0.9, stock=10)
    assert s.stock == 10
