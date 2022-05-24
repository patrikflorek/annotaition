# feature.py

import glob


class Feature(dict):
    def __init__(self, index, feature_definition, feature_data, *args, **kwargs):
        super(Feature, self).__init__(*args, **kwargs)

        for data_field_definition in feature_definition.data_fields:
            data_field_name = data_field_definition.name
            self[data_field_name] = feature_data[data_field_name][index]


class ExampleFeatures(list):
    def __init__(self, example_index, feature_definitions, features_data_table, *args, **kwargs):
        super(ExampleFeatures, self).__init__(*args, **kwargs)
        for feature_definition in feature_definitions:
            feature_name = feature_definition.name
            feature_data = features_data_table[feature_name]
            feature = Feature(example_index, feature_definition, feature_data)
            self.append(feature)


class FeaturesDict(dict):
    def __init__(self, feature_definitions, *args, **kwargs):
        super(FeaturesDict, self).__init__(*args, **kwargs)
        self.feature_definitions = feature_definitions

        for index in self.indices:
            self.update({index: self._get_feature_values(index)})

    def __getitem__(self, index):
        return ExampleFeatures(index, self.feature_definitions,  self.features_data_table)

    def _get_indices(self):
        indices = []
        for feature_definition in self.feature_definitions:
            feature_only_indices = []
            for index in feature_definition.indices:
                if index not in indices:
                    feature_only_indices.append(index)
            indices.extend(feature_only_indices)

        return indices

    def _get_feature_values(index):
        for feature_definition in

    def _get_features_data_table(self):
        data_table = dict.fromkeys(self.feature_definitions.names)
        for feature_definition in self.feature_definitions:
            feature_name = feature_definition.name
            data_table[feature_name] = self._get_indexed_data_fields(
                feature_definition)

        return data_table
