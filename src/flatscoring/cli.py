from pathlib import Path

import click
import os

from flatscoring.settings import load_settings
from flatscoring.traveltime_types.locations import TravelTimeLocation
from flatscoring.traveltime_types.distance_matrix_search import ArrivalDateTimeMatrix


def check_os_vars():
    assert (
        os.getenv("TRAVELTIME_ID", False) is not False
    ), "Set TRAVELTIME_ID env variable"
    assert (
        os.getenv("TRAVELTIME_KEY", False) is not False
    ), "Set TRAVELTIME_KEY env variable"


@click.command(name="calculate-traveltime")
@click.option("--config-file", default="settings.yaml")
@click.argument("lat", type=float)
@click.argument("lon", type=float)
def calculate_traveltime(config_file, lat, lon):
    check_os_vars()
    settings = load_settings(Path(config_file))

    from_location = TravelTimeLocation(name="domek", lat=lat, lon=lon)

    calculator = ArrivalDateTimeMatrix(
        from_location=from_location,
        travel_time=settings["settings"]["travel_time"],
    )

    calculator.locations.append(from_location)
    calculator.add_locations(settings["locations"])
    calculator.add_arrival_travels(settings["arrival_travels"])

    print(calculator.calculate())
