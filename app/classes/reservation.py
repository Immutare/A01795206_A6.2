"""
3. Reservation
    a. Create a Reservation (Customer,
    Hotel)
    b. Cancel a Reservation
"""

from dataclasses import asdict
from app.classes.base import BaseClass
from app.dtos.reservation_dto import ReservationDTO


class Reservation(BaseClass):
    """
    Class that handles the services for the Reservation entity
    a. Create a Reservation (Customer,
    Hotel)
    b. Cancel a Reservation
    """

    def __init__(self, file_path, file_name="reservation"):
        super().__init__(file_path, file_name)

    def create(self, reservation: ReservationDTO) -> ReservationDTO:
        """
        Creates a new instance of the class entity and saves it on a json
        """
        reservations = list(
            map(ReservationDTO.from_json, self.read_file_json())
            )

        result = ReservationDTO.from_json(reservation)
        reservations.append(result)

        self.write_file(items=list(map(asdict, reservations)))

        return result

    def cancel_reservation(self, id_) -> bool:
        """
        Looks for a reservation by an id match and removes it from the storage
        """
        return self.delete(id_)
