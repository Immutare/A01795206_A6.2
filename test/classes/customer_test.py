from copy import copy
from dataclasses import asdict
import io
import sys
import unittest
from app.classes.customer import Customer


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("./data")

    def test_read(self):
        self.assertGreaterEqual(len(self.customer.read()), 0)

    def test_find_customer_by_id(self):
        test_customer = {
            "id": "8a9c5bf2-a255-4164-918e-0c155e9c62a8",
            "name": "Audrey Wilkins",
            "address": "407 Prospect Place, Woodburn, Missouri, 4450",
            "birthday": "1950-01-01T12:00:00 +06:00",
            "email": "audreywilkins@aquasure.com",
            "phone": "+1 (819) 461-3290",
        }

        self.assertDictEqual(
            test_customer,
            asdict(self.customer.find_customer_by_id(test_customer.get("id"))),
        )

        with self.assertRaises(IndexError):
            self.customer.find_customer_by_id("1234")

    def test_create(self):
        new_customer = self.customer.create(
            {
                "id": "7b8a2fc0-7891-4773-a0ec-ebbd6956becd",
                "name": "Sasha Rollins",
                "address": "372 Middagh Street, Vienna, Alaska, 5627",
                "birthday": "1950-01-01T12:00:00 +06:00",
                "email": "sasharollins@aquasure.com",
                "phone": "+1 (995) 415-3461",
            }
        )

        self.assertDictEqual(
            {
                "id": "7b8a2fc0-7891-4773-a0ec-ebbd6956becd",
                "name": "Sasha Rollins",
                "address": "372 Middagh Street, Vienna, Alaska, 5627",
                "birthday": "1950-01-01T12:00:00 +06:00",
                "email": "sasharollins@aquasure.com",
                "phone": "+1 (995) 415-3461",
            },
            asdict(new_customer),
        )

    def test_display_customer_info(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.customer.display_customer_info("dc443376-b8c5-485d-8f9e-654cc9099b7e")
        sys.stdout = sys.__stdout__
        print(capturedOutput.getvalue())

        self.assertIn("dc443376-b8c5-485d-8f9e-654cc9099b7e", capturedOutput.getvalue())
        self.assertIn("Logan Schroeder", capturedOutput.getvalue())
        self.assertIn(
            "168 Calyer Street, Brule, Marshall Islands, 8752",
            capturedOutput.getvalue(),
        )
        self.assertIn("1950-01-01T12:00:00 +06:00", capturedOutput.getvalue())
        self.assertIn("loganschroeder@aquasure.com", capturedOutput.getvalue())
        self.assertIn("+1 (957) 456-2647", capturedOutput.getvalue())

    def test_update_customer(self):
        test_customer_id = "d11f0ecb-7ffb-4d5b-a78f-ebb572362b7c"

        old_customer = self.customer.find_customer_by_id(test_customer_id)
        new_customer = copy(old_customer)
        new_customer.name = f"{new_customer.name}__TEST_UPDATE"
        new_customer = self.customer.update_customer(test_customer_id, new_customer)

        self.assertEqual(f"{old_customer.name}__TEST_UPDATE", new_customer.name)
        self.assertEqual(
            new_customer.name, self.customer.find_customer_by_id(test_customer_id).name
        )
