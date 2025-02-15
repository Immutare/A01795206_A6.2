from dataclasses import asdict
import unittest
from app.classes.reservation import Reservation


class TestReservation(unittest.TestCase):
    def setUp(self):
        self.reservation = Reservation("./data", "reservation")

    def test_create(self):
        new_reservation = self.reservation.create(
                {
                    "id": "6c756dcc-8d01-1234-a3dc-9c763abcb34f",
                    "customer_id": "80a4868f-300f-4385-8f55-747dca7d535f",
                    "hotel_id": "21ffb1bc-2b3c-4177-a4a3-1aed10a55c4a",
                    "start_date": "2025-01-03T10:20:28 +06:00",
                    "end_date": "2025-01-06T09:48:25 +06:00",
                    "occupancy": 5
                }
            )

        self.assertDictEqual(
            {
                "id": "6c756dcc-8d01-1234-a3dc-9c763abcb34f",
                "customer_id": "80a4868f-300f-4385-8f55-747dca7d535f",
                "hotel_id": "21ffb1bc-2b3c-4177-a4a3-1aed10a55c4a",
                "start_date": "2025-01-03T10:20:28 +06:00",
                "end_date": "2025-01-06T09:48:25 +06:00",
                "occupancy": 5
            },
            asdict(new_reservation)
        )

    def test_cancel_reservation(self):
        self.assertTrue(
            self.reservation.cancel_reservation(
                "6c756dcc-8d01-1234-a3dc-9c763abcb34f",
            ),
            "Not cancelled",
        )


if __name__ == "__main__":
    unittest.main()
