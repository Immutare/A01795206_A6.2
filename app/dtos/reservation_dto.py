"""
Data class for the reservation entity
"""

from dataclasses import dataclass, fields
from datetime import date
from uuid import uuid4


@dataclass()
class ReservationDTO:
    """
    Data class for the reservation entity
    """
    id: str
    customer_id: str
    hotel_id: str
    start_date: date
    end_date: date
    occupancy: int

    @classmethod
    def from_json(cls, data):
        """
        Gets a json objects and converts to an instance of the class
        """
        return cls(
            id=data.get("id") or str(uuid4()),
            customer_id=data.get("customer_id"),
            hotel_id=data.get("hotel_id"),
            start_date=data.get("start_date"),
            end_date=data.get("end_date"),
            occupancy=data.get("occupancy"),
        )

    def __str__(self):
        """Returns a string containing only the non-default field values."""
        s = "\n".join(
            f"{field.name}: {getattr(self, field.name)!r}"
            for field in fields(self)
            if getattr(self, field.name) != field.default
        )
        return f"----Reservation----\n{s}"
