import uuid

from mojo.collection import HaikuElement


def chunk_to_haiku(chunk: str, source: str) -> HaikuElement:
    raw_lines = chunk.split("\n")

    stripped_lines = [line.strip() for line in raw_lines]

    lines = filter(lambda line: line != "", stripped_lines)

    attrs = {
        "lines": list(lines),
        "uuid": str(uuid.uuid4()),
        "source": source,
    }

    return HaikuElement.from_dict(attrs)
