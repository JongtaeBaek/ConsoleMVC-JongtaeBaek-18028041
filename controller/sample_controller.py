from model.sample import Sample
from view import sample_view


class SampleController:
    def __init__(self, samples: list[Sample]):
        self._samples = samples

    def register(self):
        data = sample_view.get_sample_input()
        sample = Sample(**data)
        self._samples.append(sample)
        print(f"시료 '{sample.name}' 등록 완료.")

    def list_all(self):
        sample_view.show_sample_list(self._samples)

    def search(self):
        keyword = sample_view.get_search_keyword()
        result = [s for s in self._samples if keyword in s.name]
        sample_view.show_search_result(result)
