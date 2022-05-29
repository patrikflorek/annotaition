# feature_definitions/base

class FeatureDataFieldDefinition():
    def __init__(self, data_field_dict):
        self.name = data_field_dict['name']
        self.type = data_field_dict.get('type', None)
        self.icon = data_field_dict.get('icon', '')

        self.source = data_field_dict.get('source', None)
        if self.source == "file_paths":
            self.source_file_paths = data_field_dict.get(
                "source_file_paths", []).copy()

    def __repr__(self):
        return str(self.__dict__)


class FeatureDataFieldDefinitionsList(list):
    def __init__(self, data_fields_list, *args, **kwargs):
        super(FeatureDataFieldDefinitionsList, self).__init__(*args, **kwargs)
        for data_field_dict in data_fields_list:
            data_field = FeatureDataFieldDefinition(data_field_dict)
            self.append(data_field)


class BaseFeatureDefinition:
    def __init__(self, feature_definition_dict):
        self.name = feature_definition_dict['name']
        self.description = feature_definition_dict.get('description', '')
        self.type = feature_definition_dict.get('type', None)
        self.icon = feature_definition_dict.get('icon', '')
        self.index_data_field_name = feature_definition_dict['index_data_field_name']

        data_fields = feature_definition_dict.get('data_fields', [])
        self.data_fields = FeatureDataFieldDefinitionsList(data_fields)

    def __repr__(self):
        return str(self.__dict__)

    def get_data_field_values(self):
        raise NotImplementedError(
            f"method is not implemented in class {self.__class__.__name__}")

    def get_indices(self):
        raise NotImplementedError(
            f"method is not implemented in class {self.__class__.__name__}")
