import pytest

from mojo.parse_blank_line_separated import chunk_to_haiku

def test_chunk_to_haiku() -> None:
    chunk = """
    Panda Bamboo
    Curry Noodle
    Tree Flower
    """

    expected = ["Panda Bamboo", "Curry Noodle", "Tree Flower"]

    haiku_element = chunk_to_haiku(chunk, "bogus source")

    assert haiku_element.lines == expected