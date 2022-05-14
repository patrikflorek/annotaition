# feature_definition.py

import glob


class FeatureDefinitionDataField():
    def __init__(self, data_field_dict):
        self.name = data_field_dict['name']
        self.type = data_field_dict.get('type', None)
        self.icon = data_field_dict.get('icon', '')

        self.source = data_field_dict.get('source', None)
        if self.source == "file_paths":
            self.source_file_paths = data_field_dict.get(
                "source_file_paths", []).copy()


class FeatureDefinitionDataFieldsList(list):
    def __init__(self, data_fields_list, *args, **kwargs):
        super(FeatureDefinitionDataFieldsList, self).__init__(*args, **kwargs)
        for data_field_dict in data_fields_list:
            data_field = FeatureDefinitionDataField(data_field_dict)
            self.append(data_field)


class FeatureDefinition():
    def __init__(self, feature_definition_dict):
        self.name = feature_definition_dict['name']
        self.description = feature_definition_dict.get('description', '')
        self.type = feature_definition_dict.get('type', None)
        self.icon = feature_definition_dict.get('icon', '')
        self.index_data_field_name = feature_definition_dict.get(
            'index_data_field_name', None)

        data_fields = feature_definition_dict.get('data_fields', [])
        self.data_fields = FeatureDefinitionDataFieldsList(data_fields)

    def get_indices(self, index_data_field_name):
        for data_field in self.data_fields:
            if data_field.name != index_data_field_name:
                continue

            if data_field.type == "file_paths" and data_field.source == "file_paths":
                indices = []
                for file_paths_pattern in data_field.source_file_paths:
                    file_paths = glob(file_paths_pattern)
                    indices.extend(file_paths)
                return indices


class FeatureDefinitionsList(list):
    def __init__(self, *args, **kwargs):
        super(FeatureDefinitionsList, self).__init__(*args, **kwargs)
        self.index_feature_name = None
        self._indices = []

    def update(self, data_list, index_feature_name, index_data_field_name):
        self.clear()
        for feature_definition_dict in data_list:
            feature_definition = FeatureDefinition(feature_definition_dict)

            if feature_definition.name == index_feature_name:
                self._indices = feature_definition.get_indices(
                    index_data_field_name)

            self.append(feature_definition)

    def get_indices(self):
        return self._indices
