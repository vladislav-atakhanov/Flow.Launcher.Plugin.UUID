from typing import TypedDict
from dataclasses import dataclass, asdict, field


class AsDict:
    def asdict(self):
        return asdict(self)


class JsonRPCAction(TypedDict):
    method: str
    parameters: list


@dataclass
class QueryResult(AsDict):
    Title: str
    JsonRPCAction: JsonRPCAction
    SubTitle: str = field(default=None)
    IcoPath: str = field(default=None)
