from dataclasses import dataclass


@dataclass
class Iot:
    mac:str
    temp:float
    datetime:str
    latitude:float
    longitude:float

@dataclass
class Client:
    name: str
    ip: str
    mac: str
    longitude: float
    latitude: float