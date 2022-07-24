from dataclasses import dataclass

@dataclass(frozen=True, eq=True)
class TravelTimeLocation():
    name: str
    lat: float
    lon: float

    def __post_init__(self):
        assert len(str(self.lat)) >= 17, "Too low precision latitute"
        assert len(str(self.lon)) >= 17, "Too low precision longitude"

    def to_dict(self):
        return {"id": self.name, "coords": {"lat": self.lat, "lng": self.lon}}