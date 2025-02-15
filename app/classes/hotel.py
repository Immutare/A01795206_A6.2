"""
Class service for Hotel

Implements the following functions:
1. Hotels
    a. Create Hotel
    b. Delete Hotel
    c. Display Hotel informati
    d. Modify Hotel Informati
    e. Reserve a Room
    f. Cancel a Reservation
"""

from dataclasses import asdict
from app.classes.base import BaseClass
from app.classes.reservation import Reservation
from app.dtos.hotel_dto import HotelDTO


class Hotel(BaseClass):
    """
    Class service for Hotel

    Implements the following functions:
    1. Hotels
        a. Create Hotel
        b. Delete Hotel
        c. Display Hotel informati
        d. Modify Hotel Informati
        e. Reserve a Room
        f. Cancel a Reservation
    """
    def __init__(self, file_path, file_name="hotel"):
        super().__init__(file_path, file_name)
        self.file_path = file_path
        self.file_name = file_name
        self.reservations = Reservation(file_path)

    def read(self) -> list[HotelDTO]:
        """
        Reads a json file
        """
        content = self.read_file_json()

        return list(map(HotelDTO.from_json, content))

    def find_hotel_by_id(self, id_: str):
        """
        Reads the json file storage and tries to return a match based on an id.
        Raises an error if not found
        """
        hotels = self.read()
        find = [hotel for hotel in hotels if hotel.id == id_]

        if len(find) > 0:
            return find[0]
        raise IndexError(f"Hotel with id [{id_}] not found")

    def create(self, hotel: HotelDTO) -> HotelDTO:
        """
        Creates a new instance of the class entity and saves it on a json
        """
        hotels = self.read()

        result = HotelDTO.from_json(hotel)
        hotels.append(result)

        self.write_file(list(map(asdict, hotels)))

        return result

    def display_hotel_info(self, found_indx: str):
        """
        Tries to find a hotel by an id and prints the match if found
        Raises an error if not found
        """
        hotel = self.find_hotel_by_id(found_indx)
        print(hotel)

    def update_hotel(self, id_: str, hotel: HotelDTO):
        """
        Retreives all items from the file storage, looks for a match\
        and updates the data if found
        If not found, raises an error
        """
        hotels = self.read()

        found = False
        found_indx = -1

        for indx, htl in enumerate(hotels):
            if htl.id == id_:
                found = True
                found_indx = indx
                break

        if not found:
            raise LookupError(f"Hotel with id [{id_}] wasn't found")

        hotels[found_indx] = hotel

        self.write_file(list(map(asdict, hotels)))

        return hotel

    def reserve_room(self, **kwargs):
        """
        Adds a reservation to the hotel
        """
        return self.reservations.create(
            {
                "hotel_id": kwargs.get("hotel_id"),
                "customer_id": kwargs.get("customer_id"),
                "start_date": kwargs.get("start_date"),
                "end_date": kwargs.get("end_date"),
                "occupancy": kwargs.get("occupancy"),
            }
        )

    def cancel_reservation(self, reservation_id: str):
        """
        Looks for a reservation by an id match and removes it from the storage
        """
        return self.reservations.cancel_reservation(reservation_id)
