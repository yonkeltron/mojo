# This code parses date/times, so please
#
#     pip install python-dateutil
#
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = collection_schema_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import List, Any, TypeVar, Callable, Type, cast
from uuid import UUID
from datetime import datetime
import dateutil.parser


T = TypeVar("T")


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class SampleElement:
    """The poem body, expressed as a collection of lines"""
    lines: List[str]
    source: str
    """A UUID to uniquely identify the sample"""
    uuid: UUID

    @staticmethod
    def from_dict(obj: Any) -> 'SampleElement':
        assert isinstance(obj, dict)
        lines = from_list(from_str, obj.get("lines"))
        source = from_str(obj.get("source"))
        uuid = UUID(obj.get("uuid"))
        return SampleElement(lines, source, uuid)

    def to_dict(self) -> dict:
        result: dict = {}
        result["lines"] = from_list(from_str, self.lines)
        result["source"] = from_str(self.source)
        result["uuid"] = str(self.uuid)
        return result


@dataclass
class CollectionSchema:
    name: str
    """The samples composing the collection"""
    samples: List[SampleElement]
    url: str
    uuid: UUID
    written_at: datetime

    @staticmethod
    def from_dict(obj: Any) -> 'CollectionSchema':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        samples = from_list(SampleElement.from_dict, obj.get("samples"))
        url = from_str(obj.get("url"))
        uuid = UUID(obj.get("uuid"))
        written_at = from_datetime(obj.get("writtenAt"))
        return CollectionSchema(name, samples, url, uuid, written_at)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["samples"] = from_list(lambda x: to_class(SampleElement, x), self.samples)
        result["url"] = from_str(self.url)
        result["uuid"] = str(self.uuid)
        result["writtenAt"] = self.written_at.isoformat()
        return result


def collection_schema_from_dict(s: Any) -> CollectionSchema:
    return CollectionSchema.from_dict(s)


def collection_schema_to_dict(x: CollectionSchema) -> Any:
    return to_class(CollectionSchema, x)
