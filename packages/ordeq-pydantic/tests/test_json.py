from pathlib import Path

from ordeq_pydantic import PydanticJSON
from pydantic import BaseModel


class MyModel(BaseModel):
    hello: str
    world: str


def test_model(tmp_path):
    file_path = Path(tmp_path / "example.json")
    dataset = PydanticJSON(path=file_path, model_type=MyModel)

    model = MyModel(hello="world", world="hello")
    dataset.save(model)

    assert (
        file_path.read_text(encoding=None)
        == '{"hello":"world","world":"hello"}'
    )

    loaded_model = dataset.load()
    assert model == loaded_model
