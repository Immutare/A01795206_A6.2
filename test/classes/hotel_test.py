from copy import copy
from dataclasses import asdict
from datetime import date
import io
import sys
import unittest
from app.classes.hotel import Hotel


class TestHotel(unittest.TestCase):
    def setUp(self):
        self.hotel = Hotel("./data")

    def test_read(self):
        self.assertGreaterEqual(len(self.hotel.read()), 0)

    def test_find_hotel_by_id(self):
        test_hotel = {
            "id": "1b82f96c-41af-43d3-83c2-98ac64d31c83",
            "name": "Wyndham Garden Brooklyn Sunset Park",
            "description": "A 5-minute walk from a subway station, this trendy hotel with a distinctive geometric facade is 12 miles from the Statue of Liberty and 14 miles from LaGuardia Airport.",
            "address": "501 Coleridge Street, New York, New York",
            "rating": 3,
            "cost": "$1,974.59",
        }

        self.assertDictEqual(
            test_hotel, asdict(self.hotel.find_hotel_by_id(test_hotel.get("id")))
        )

        with self.assertRaises(IndexError):
            self.hotel.find_hotel_by_id("1234")

    def test_create(self):
        new_hotel = self.hotel.create(
            {
                "id": "f4bbb16b-261f-4567-b91b-e1ab0a68f5f7",
                "name": "TEST - Four Points by Sheraton Midtown",
                "description": "TEST - Adjacent to Port Authority Bus Terminal, this straightforward hotel is an 11-minute walk from Times Square and 0.9 miles from Radio City Music Hall.",
                "address": "TEST - 121 Hunts Lane, New York, New York",
                "rating": 2,
                "cost": "$4,534.94",
            }
        )

        self.assertDictEqual(
            {
                "id": "f4bbb16b-261f-4567-b91b-e1ab0a68f5f7",
                "name": "TEST - Four Points by Sheraton Midtown",
                "description": "TEST - Adjacent to Port Authority Bus Terminal, this straightforward hotel is an 11-minute walk from Times Square and 0.9 miles from Radio City Music Hall.",
                "address": "TEST - 121 Hunts Lane, New York, New York",
                "rating": 2,
                "cost": "$4,534.94",
            },
            asdict(new_hotel),
        )

    def test_display_hotel_info(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.hotel.display_hotel_info("935577b1-1e14-492c-8c75-c319333e5a60")
        sys.stdout = sys.__stdout__
        print(capturedOutput.getvalue())

        self.assertIn("Pod 51", capturedOutput.getvalue())
        self.assertIn("935577b1-1e14-492c-8c75-c319333e5a60", capturedOutput.getvalue())
        self.assertIn(
            "This hip modern budget hotel on a leafy block in Midtown East is 1.1 miles from Times Square.",
            capturedOutput.getvalue(),
        )
        self.assertIn(
            "135 Schenck Street, New York, New York", capturedOutput.getvalue()
        )
        self.assertIn("rating: 3", capturedOutput.getvalue())
        self.assertIn("cost: '$3,852.77'", capturedOutput.getvalue())

    def test_update_hotel(self):
        test_hotel_id = "f4bbb16b-261f-4274-b91b-e1ab0a68f5f7"

        old_hotel = self.hotel.find_hotel_by_id(test_hotel_id)
        new_hotel = copy(old_hotel)
        new_hotel.name = f"{new_hotel.name}__TEST_UPDATE"
        new_hotel = self.hotel.update_hotel(test_hotel_id, new_hotel)

        self.assertEqual(f"{old_hotel.name}__TEST_UPDATE", new_hotel.name)
        self.assertEqual(
            new_hotel.name, self.hotel.find_hotel_by_id(test_hotel_id).name
        )

    def test_reserve_room(self):
        new_reservation = self.hotel.reserve_room(
            customer_id="80a4868f-300f-4385-8f55-747dca7d535f",
            hotel_id="21ffb1bc-2b3c-4177-a4a3-1aed10a55c4a",
            start_date="2025-01-03T10:20:28 +06:00",
            end_date="2025-01-03T10:20:28 +06:00",
            occupancy=5,
        )

        self.assertDictEqual(
            {
                "id": new_reservation.id,
                "customer_id": "80a4868f-300f-4385-8f55-747dca7d535f",
                "hotel_id": "21ffb1bc-2b3c-4177-a4a3-1aed10a55c4a",
                "start_date": "2025-01-03T10:20:28 +06:00",
                "end_date": "2025-01-03T10:20:28 +06:00",
                "occupancy": 5,
            },
            asdict(new_reservation),
        )

    def test_cancel_reservation(self):
        self.assertTrue(
            self.hotel.cancel_reservation(
                "6c756dcc-8d01-1234-a3dc-9c763abcb34f",
            ),
            "Not cancelled",
        )


if __name__ == "__main__":
    unittest.main()
