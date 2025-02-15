"""
DataClass for the Hotel entity
"""

from dataclasses import dataclass, fields
from uuid import uuid4


@dataclass()
class HotelDTO:
    """
    DataClass for the Hotel entity
    """
    id: str
    name: str
    description: str
    address: str
    rating: int
    cost: float

    @classmethod
    def from_json(cls, data):
        """
        Gets a json objects and converts to an instance of the class
        """
        return cls(
            id=data.get("id") or str(uuid4()),
            name=data.get("name"),
            description=data.get("description"),
            address=data.get("address"),
            rating=data.get("rating"),
            cost=data.get("cost"),
        )

    def __str__(self):
        """Returns a string containing only the non-default field values."""
        s = "\n".join(
            f"{field.name}: {getattr(self, field.name)!r}"
            for field in fields(self)
            if getattr(self, field.name) != field.default
        )
        return f"----Hotel----\n{s}"
