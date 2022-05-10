# feature_definition.py


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
        super(FeatureDefinitionDataField, self).__init__(*args, **kwargs)
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

        self.data_source = feature_definition_dict.get('data_source', None)
        if self.data_source == 'feature':
            self.data_source_feature_name = feature_definition_dict['data_source_feature_name']

        data_fields = feature_definition_dict.get('data_fields', [])
        self.data_fields = FeatureDefinitionDataFieldsList(data_fields)


class FeatureDefinitionsList(list):
    def update(self, data_list):
        self.clear()
        for feature_definition_dict in data_list:
            feature_definition = FeatureDefinition(feature_definition_dict)
            self.append(feature_definition)
