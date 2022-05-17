# example.py

from feature import FeaturesDict
from label import LabelsDict


class Example():
    def __init__(self, example_index, feature_definitions, label_definitions):
        features = []
        for feature_definition in feature_definitions:
            feature = Feature(example_index, feature_definition)


class ExamplesList(list):
    def __init__(self, index_feature_name, index_data_field_name,
                 feature_definitions, label_definitions, labels_list, *args, **kwargs):
        self.super(ExamplesList, self).__init__(*args, **kwargs)
        self.index_feature_name = index_feature_name
        self.index_data_field_name = index_data_field_name
        self.feature_definitions = feature_definitions
        self.features = FeaturesDict(
            index_feature_name, index_data_field_name, feature_definitions)

        self.label_definitions = label_definitions
        self.labels = LabelsDict(labels_list)

        self._indices = self._get_merged_indices()

    def __getitem__(self, index):
        return Example(index, self.feature_definitions, self.label_definitions)

    def _get_label_indices(self):
        indices = list(self.labels.keys())

        return indices

    def _get_orphan_indices(self):
        orphan_indices = []
        for label_index in self.labels.indices:
            if label_index in self.features.indices:
                continue

            orphan_indices.append(label_index)

        return orphan_indices

    def _get_merged_indices(self):
        orphan_indices = self._get_orphan_indices()

        merged_indices = self.features.indices + orphan_indices
        return merged_indices

    def update_feature_definitions(self, feature_definitions):
        self.feature_definitions = feature_definitions
        self._indices = self._get_raw_indices()

    def update_label_definitions(self, label_definitions):
        self.label_definitions = label_definitions

    def update_labels(self, labels_list):
        self.labels = LabelsDict(labels_list)
