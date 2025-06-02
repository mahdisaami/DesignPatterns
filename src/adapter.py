import json
import xmltodict

class JsonAdapter:

    @classmethod
    def to_json(cls, file):
        with open(file) as xml_file:
            data_dict = xmltodict.parse(xml_file.read())
            json_data = json.dumps(data_dict)
        with open('data.json', 'w') as json_file:
            data_json = json_file.write(json_data)

        return data_json


if __name__ == '__main__':
    result = JsonAdapter.to_json('xml.xml')