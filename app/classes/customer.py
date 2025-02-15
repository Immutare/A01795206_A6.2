"""
Customer service class

Implements the following functions
a. Create Customer
b. Delete a Customer
c. Display Customer Information
d. Modify Customer Information

"""

from dataclasses import asdict
from app.classes.base import BaseClass
from app.dtos.customer_dto import CustomerDTO


class Customer(BaseClass):
    """
    Customer service class
    Implements the following functions
    a. Create Customer
    b. Delete a Customer
    c. Display Customer Information
    d. Modify Customer Information
    """

    def __init__(self, file_path, file_name="customer"):
        super().__init__(file_path, file_name)
        self.file_path = file_path
        self.file_name = file_name

    def read(self) -> list[CustomerDTO]:
        """
        Reads a json file
        """
        content = self.read_file_json()

        return list(map(CustomerDTO.from_json, content))

    def find_customer_by_id(self, id_: str):
        """
        Reads the json file storage and tries to return a match based on an id.
        Raises an error if not found
        """
        customers = self.read()
        find = [customer for customer in customers if customer.id == id_]

        if len(find) > 0:
            return find[0]
        raise IndexError(f"Customer with id [{id_}] not found")

    def create(self, customer: CustomerDTO) -> CustomerDTO:
        """
        Creates a new instance of the class entity and saves it on a json
        """
        customers = self.read()

        result = CustomerDTO.from_json(customer)
        customers.append(result)

        self.write_file(list(map(asdict, customers)))

        return result

    def display_customer_info(self, id_: str):
        """
        Tries to find a customer by an id and prints the match if found
        Raises an error if not found
        """
        customer = self.find_customer_by_id(id_)
        print(customer)

    def update_customer(self, id_: str, customer: CustomerDTO):
        """
        Retreives all items from the file storage, looks for a match
        and updates the data if found
        If not found, raises an error
        """
        customers = self.read()

        found = False
        found_indx = -1

        for indx, cust in enumerate(customers):
            if cust.id == id_:
                found = True
                found_indx = indx
                break

        if not found:
            raise LookupError(f"Customer with id [{id_}] wasn't found")

        customers[found_indx] = customer

        self.write_file(list(map(asdict, customers)))

        return customer
