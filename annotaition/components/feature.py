# components/feature.py


class FeaturesDict(dict):
    def __init__(self, feature_definitions, *args, **kwargs):
        super(FeaturesDict, self).__init__(*args, **kwargs)
        self.feature_definitions = feature_definitions
        self.data_field_values = feature_definitions.get_data_field_values()

    def _get_blank_features(self):
        features_dict = {}
        for feature_definition in self.feature_definitions:
            feature_name = feature_definition.name
            
            data_fields_dict = {}
            features_dict[feature_name] = data_fields_dict
            
            for data_field in feature_definition.data_fields:
                data_fields_dict[data_field.name] = None

        return features_dict

    def __getitem__(self, index):
        if index not in self.data_field_values:
            return self._get_blank_features()
        
        return self.data_field_values[index]

    def get_indices(self):
        return self.feature_definitions.get_indices()

    def update_feature_definitions(self, feature_definitions):
        self.feature_definitions = feature_definitions
        self.data_field_values = feature_definitions.get_data_field_values()
