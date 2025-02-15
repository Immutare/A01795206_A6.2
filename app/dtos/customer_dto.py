"""
DataClass for the Customer entity
"""

from dataclasses import dataclass, fields
from datetime import date
from uuid import uuid4


@dataclass()
class CustomerDTO:
    """
    DataClass for the Customer entity
    """

    id: str
    name: str
    address: str
    birthday: date
    email: str
    phone: str

    @classmethod
    def from_json(cls, data):
        """
        Gets a json objects and converts to an instance of the class
        """
        return cls(
            id=data.get("id") or str(uuid4()),
            name=data.get("name"),
            address=data.get("address"),
            birthday=data.get("birthday"),
            email=data.get("email"),
            phone=data.get("phone"),
        )

    def __str__(self):
        """Returns a string containing only the non-default field values."""
        s = "\n".join(
            f"{field.name}: {getattr(self, field.name)!r}"
            for field in fields(self)
            if getattr(self, field.name) != field.default
        )
        return f"----Customer----\n{s}"
