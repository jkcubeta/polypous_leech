from src.algernon import AlgObject
from src.toll_booth import InvalidSchemaPropertyType


class SchemaPropertyEntry(AlgObject):
    _accepted_types = [
        'String', 'Number', 'DateTime', 'Boolean'
    ]

    def __init__(self,
                 property_name: str,
                 property_data_type: str,
                 sensitive=False,
                 is_id_value=False):
        """

        Args:
            property_name:
            property_data_type:
            sensitive:
            is_id_value:
        """
        if property_data_type not in self._accepted_types:
            raise InvalidSchemaPropertyType(property_name, property_data_type, self._accepted_types)
        self._property_name = property_name
        self._property_data_type = property_data_type
        self._sensitive = sensitive
        self._is_id_value = is_id_value

    @classmethod
    def parse_json(cls, json_dict: dict):
        return cls(
            json_dict['property_name'],
            json_dict['property_data_type'],
            json_dict.get('sensitive', False),
            json_dict.get('is_id_value', False)
        )

    @property
    def sensitive(self):
        return self._sensitive

    @property
    def property_name(self):
        return self._property_name

    @property
    def property_data_type(self):
        return self._property_data_type

    @property
    def is_id_value(self):
        return self._is_id_value


class EdgePropertyEntry(SchemaPropertyEntry):
    def __init__(self,
                 property_name: str,
                 property_data_type: str,
                 property_source: str):
        """

        Args:
            property_name:
            property_data_type:
            property_source:
        """
        super().__init__(property_name, property_data_type)
        self._property_source = property_source

    @classmethod
    def parse_json(cls, json_dict: dict):
        return cls(json_dict['property_name'], json_dict['property_data_type'], json_dict['property_source'])

    @property
    def property_source(self):
        return self._property_source
