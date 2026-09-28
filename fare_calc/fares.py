"""Fare rules for the regional network."""
from dataclasses import dataclass

BASE_CENTS = 250
PER_ZONE_CENTS = 75
PEAK_SURCHARGE_CENTS = 50
DISCOUNTS = {"adult": 0.0, "senior": 0.5, "student": 0.3, "child": 1.0}


@dataclass(frozen=True)
class Rider:
    category: str
    has_transfer: bool = False


def is_peak(hour: int) -> bool:
    """Weekday peak windows are 07:00-09:59 and 16:00-18:59."""
    return 7 <= hour < 10 or 16 <= hour < 19


def fare_cents(rider: Rider, zones: int, hour: int) -> int:
    """Return the fare in cents for one journey crossing ``zones`` zones."""
    if zones < 1:
        raise ValueError("a journey crosses at least one zone")
    if rider.category not in DISCOUNTS:
        raise ValueError(f"unknown rider category: {rider.category}")
    if rider.has_transfer:
        return 0
    gross = BASE_CENTS + PER_ZONE_CENTS * (zones - 1)
    if is_peak(hour):
        gross += PEAK_SURCHARGE_CENTS
    return round(gross * (1 - DISCOUNTS[rider.category]))
