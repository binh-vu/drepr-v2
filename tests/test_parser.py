import pytest

from drepr.models.prelude import DRepr
from tests.conftest import DatasetExample


@pytest.mark.parametrize("name", ["pseudo_people"])
def test_parse_examples(name, example_datasets: dict[str, DatasetExample]):
    ds = example_datasets[name]
    model = DRepr.parse_from_file(ds.model)
