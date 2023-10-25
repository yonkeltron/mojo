import pytest

from mojo.parse_blank_line_separated import chunk_to_haiku_attrs, collection_from_raw


@pytest.fixture()
def chunk() -> str:
    return """Panda Bamboo
    Curry Noodle
    Tree Flower"""


def test_chunk_to_haiku_attrs(chunk) -> None:
    expected = ["Panda Bamboo", "Curry Noodle", "Tree Flower"]

    haiku_element = chunk_to_haiku_attrs(chunk)

    assert haiku_element["lines"] == expected


def test_collection_from_raw(chunk) -> None:
    raw = f"{chunk}\n\n\n{chunk}\n\n{chunk}\n"

    collection = collection_from_raw("bogus name", "bogus url", raw)

    assert collection["haiku"][0]["lines"] == chunk_to_haiku_attrs(chunk)[
        "lines"]
    assert len(collection["haiku"]) == 3
