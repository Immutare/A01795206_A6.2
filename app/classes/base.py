"""
Base class for the entities
Implements common methods used on all clases like:
- Reading the file
- Writing the file
- Deleting an entity
"""

import json


class BaseClass:
    """
    Base class for the entities
    Implements common methods used on all clases like:
    - Reading the file
    - Writing the file
    - Deleting an entity
    """

    def __init__(self, file_path, file_name):
        self.file_path = file_path
        self.file_name = file_name

    def read_file_json(self):
        """
        Reads a json file
        """
        with open(
            f"{self.file_path}/{self.file_name}.json", encoding="utf-8"
        ) as json_file:
            content = json.load(json_file)
            json_file.close()

        return content

    def write_file(self, items) -> None:
        """
        Receives a list of items (dictionaries) and dumps them on a json file
        """
        with open(
            f"{self.file_path}/{self.file_name}.json", "w", encoding="utf-8"
        ) as json_file:
            json.dump(items, json_file, ensure_ascii=False, indent=2)
            json_file.close()

    def delete(self, id_) -> bool:
        """
        Deletes an element from the json file based on an id
        """
        items: list[any] = self.read_file_json()

        found = False
        found_indx = -1

        for indx, item in enumerate(items):
            if item.get("id") == id_:
                found = True
                found_indx = indx
                break

        if found:
            items.pop(found_indx)

        return found
