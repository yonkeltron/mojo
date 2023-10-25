import uuid
from datetime import datetime, timezone
from typing import Any


def collection_from_raw(name: str, url: str, raw: str) -> dict[str, Any]:
    raw_chunks = raw.split("\n\n")
    stripped_chunks = [chunk.strip() for chunk in raw_chunks]
    non_blank_chunks = filter(lambda chunk: chunk != "", stripped_chunks)

    haiku = [chunk_to_haiku_attrs(chunk) for chunk in non_blank_chunks]

    attrs = {
        "haiku": haiku,
        "uuid": str(uuid.uuid4()),
        "url": url,
        "name": name,
        "writtenAt": str(datetime.now(tz=timezone.utc)),
    }

    return attrs


def chunk_to_haiku_attrs(chunk: str) -> dict[str, Any]:
    raw_lines = chunk.split("\n")

    stripped_lines = [line.strip() for line in raw_lines]

    lines = filter(lambda line: line != "", stripped_lines)

    return {"lines": list(lines), "uuid": str(uuid.uuid4())}
