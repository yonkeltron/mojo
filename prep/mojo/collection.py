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
#     result = collection_from_dict(json.loads(json_string))

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
class HaikuElement:
    """The poem body, expressed as a collection of lines"""
    lines: List[str]
    source: str
    """A UUID to uniquely identify the sample"""
    uuid: UUID

    @staticmethod
    def from_dict(obj: Any) -> 'HaikuElement':
        assert isinstance(obj, dict)
        lines = from_list(from_str, obj.get("lines"))
        source = from_str(obj.get("source"))
        uuid = UUID(obj.get("uuid"))
        return HaikuElement(lines, source, uuid)

    def to_dict(self) -> dict:
        result: dict = {}
        result["lines"] = from_list(from_str, self.lines)
        result["source"] = from_str(self.source)
        result["uuid"] = str(self.uuid)
        return result


@dataclass
class Collection:
    """The samples composing the collection"""
    haiku: List[HaikuElement]
    name: str
    url: str
    uuid: UUID
    written_at: datetime

    @staticmethod
    def from_dict(obj: Any) -> 'Collection':
        assert isinstance(obj, dict)
        haiku = from_list(HaikuElement.from_dict, obj.get("haiku"))
        name = from_str(obj.get("name"))
        url = from_str(obj.get("url"))
        uuid = UUID(obj.get("uuid"))
        written_at = from_datetime(obj.get("writtenAt"))
        return Collection(haiku, name, url, uuid, written_at)

    def to_dict(self) -> dict:
        result: dict = {}
        result["haiku"] = from_list(lambda x: to_class(HaikuElement, x), self.haiku)
        result["name"] = from_str(self.name)
        result["url"] = from_str(self.url)
        result["uuid"] = str(self.uuid)
        result["writtenAt"] = self.written_at.isoformat()
        return result


def collection_from_dict(s: Any) -> Collection:
    return Collection.from_dict(s)


def collection_to_dict(x: Collection) -> Any:
    return to_class(Collection, x)
