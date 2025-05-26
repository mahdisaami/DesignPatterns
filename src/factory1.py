from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as ET

class FileHandler(ABC):
    @abstractmethod
    def open(self, filepath):
        pass

    @abstractmethod
    def edit(self):
        pass


class JSONFileHandler(FileHandler):
    def __init__(self):
        self.data = None

    def open(self, filepath):
        print(f"Opening JSON file: {filepath}")
        with open(filepath, 'r') as f:
            self.data = json.load(f)

    def edit(self):
        print("Editing JSON data...")
        self.data["edited"] = True
        print("Updated data:", self.data)


class XMLFileHandler(FileHandler):
    def __init__(self):
        self.root = None
        self.tree = None

    def open(self, filepath):
        print(f"Opening XML file: {filepath}")
        self.tree = ET.parse(filepath)
        self.root = self.tree.getroot()

    def edit(self):
        print("Editing XML data...")
        new_element = ET.Element("edited")
        new_element.text = "true"
        self.root.append(new_element)
        print("Updated XML structure:")
        for elem in self.root:
            print(elem.tag, elem.text)


class FileHandlerFactory:
    @staticmethod
    def get_handler(file_type):
        if file_type == "json":
            return JSONFileHandler()
        elif file_type == "xml":
            return XMLFileHandler()
        else:
            raise ValueError(f"Unsupported file type: {file_type}")


def main():
    file_type = input("Enter file type (json/xml): ").strip().lower()
    filepath = input("Enter file path: ").strip()

    try:
        handler = FileHandlerFactory.get_handler(file_type)
        handler.open(filepath)
        handler.edit()
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
