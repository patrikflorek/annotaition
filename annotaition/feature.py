# feature.py

import glob


class FeaturesData(list):
    def __init__(self, index, *args, **kwargs):
        super(ExampleFeatures, self).__init__(*args, **kwargs)


class FeaturesDict(dict):
    def __init__(self, index_feature_name, index_data_field_name, feature_definitions, *args, **kwargs):
        super(FeaturesDict, self).__init__(*args, **kwargs)
        self.index_feature_name = index_feature_name
        self.index_data_field_name = index_data_field_name
        self.feature_definitions = feature_definitions

        self.indices = self._get_indices()

        self._create_features()

    def _create_features(self):
        data_field_values = {}
        for feature_definition in self.feature_definitions:
            feature_name = feature_definition.name
            data_field_values[feature_name] = {}
            for data_field in feature_definition.data_fields:
                data_field_values[feature_name][data_field.name] = self._get_data_field_values(
                    data_field)

        self.clear()
        for index in self.indices:
            self.update({index:})
            for feature_definition in self.feature_definitions:

    def _get_data_field_values(self, data_field):
        values = []

        if (data_field.type == "file_paths" and
                data_field.source == "file_paths"):
            for file_paths_pattern in data_field.source_file_paths:
                file_paths = glob(file_paths_pattern)
                values.extend(file_paths)

            indices = values
            values = dict(zip(indices, values))  # file paths are indices

        return values

    def _get_indices(self):
        for feature_definition in self.feature_definitions:
            if feature_definition.name == self.index_feature_name:
                index_feature_definition = feature_definition
                break

        for data_field in index_feature_definition.data_fields:
            if data_field.name == self.index_data_field_name:
                index_data_field = data_field
                break

        # Keys are the indices
        indices = list(self._get_data_field_values(index_data_field).keys())

        return indices
