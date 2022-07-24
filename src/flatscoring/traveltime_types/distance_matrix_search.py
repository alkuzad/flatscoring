from typing import List
from flatscoring.traveltime_types.locations import TravelTimeLocation
from flatscoring.traveltime_types.arrival_search import ArrivalTravel
import traveltimepy


class ArrivalDateTimeMatrix:
    def __init__(self, from_location: TravelTimeLocation, travel_time: int):
        self._from_location = from_location
        self._travel_time = travel_time
        self.locations = []  # type: List[TravelTimeLocation]
        self.arrival_travels = []  # type: List[ArrivalTravel]

    def add_locations(self, locations: dict):
        new_locations = []
        for location, settings in locations.items():
            new_locations.append(
                TravelTimeLocation(location, settings['lat'], settings['lon'])
            )
        self.locations.extend(new_locations)

    def _get_location(self, name):
        for location in self.locations:
            if location.name == name:
                return location

    def add_arrival_travels(self, travels: dict):
        new_travels = []
        for travel, settings in travels.items():
            new_travels.append(
                ArrivalTravel(
                    travel,
                    from_location=[x.name for x in [self._from_location]],
                    to_location=self._get_location(settings['to']).name,
                    transportation=settings['transporation'],
                    arrival_time=settings['time'],
                    travel_time=self._travel_time,
                )
            )
        self.arrival_travels.extend(new_travels)

    def calculate(self):
        breakpoint()
        return traveltimepy.time_filter(
            locations=[x.to_dict() for x in self.locations],
            arrival_searches=[x.to_dict() for x in self.arrival_travels],
        )
