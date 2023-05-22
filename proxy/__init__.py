from dataclasses import dataclass
import typing

@dataclass
class Proxy:
    antecedents: typing.Set[str | int]
    consequents: typing.Set[str | int]
    confidence: float
