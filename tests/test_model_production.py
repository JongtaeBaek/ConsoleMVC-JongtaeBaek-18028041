from model.production import ProductionJob, ProductionQueue


def _make_job(order_id="o1"):
    return ProductionJob(
        order_id=order_id,
        sample_id="S001",
        required_quantity=5,
        actual_production=6,
        total_time=12.0,
    )


def test_production_job_fields():
    job = _make_job()
    assert job.order_id == "o1"
    assert job.sample_id == "S001"
    assert job.required_quantity == 5
    assert job.actual_production == 6
    assert job.total_time == 12.0


def test_queue_empty_initial():
    q = ProductionQueue()
    assert q.is_empty()
    assert q.peek() is None
    assert q.dequeue() is None
    assert q.all() == []


def test_queue_enqueue_and_peek():
    q = ProductionQueue()
    job = _make_job()
    q.enqueue(job)
    assert not q.is_empty()
    assert q.peek() == job
    assert len(q.all()) == 1


def test_queue_dequeue_fifo():
    q = ProductionQueue()
    j1 = _make_job("o1")
    j2 = _make_job("o2")
    q.enqueue(j1)
    q.enqueue(j2)
    assert q.dequeue() == j1
    assert q.dequeue() == j2
    assert q.is_empty()


def test_queue_all_order():
    q = ProductionQueue()
    j1 = _make_job("o1")
    j2 = _make_job("o2")
    q.enqueue(j1)
    q.enqueue(j2)
    assert q.all() == [j1, j2]
