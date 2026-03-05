from dataclasses import dataclass


@dataclass
class Target:
    lat: float
    lon: float
    description: str
