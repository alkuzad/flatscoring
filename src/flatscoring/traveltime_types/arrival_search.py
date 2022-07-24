from dataclasses import dataclass, field
from datetime import datetime
import typing


@dataclass(eq=True, frozen=True)
class ArrivalTravel:
    name: str
    from_location: typing.List[str]
    to_location: str
    transportation: str
    arrival_time: datetime
    travel_time: int
    properties: tuple = ("travel_time", "distance", "distance_breakdown")

    def __pre_init__(self):
        assert self.transportation in ["public_transport", "driving", "walking"]

        tzinfo = self.arrival_time.tzinfo
        assert tzinfo is not None and tzinfo.tzname(None) == 'UTC'

    def to_dict(self):
        return {
            "id": self.name,
            "departure_location_ids": self.from_location,
            "arrival_location_id": self.to_location,
            "transportation": {"type": self.transportation},
            "arrival_time":  self.arrival_time.isoformat(),
            "travel_time": self.travel_time,
            "properties": self.properties
        }