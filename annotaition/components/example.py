# components/example.py

from annotaition.components.feature import FeaturesDict
from annotaition.components.label import LabelsDict


class Example():
    def __init__(self, index, features, labels):
        self.example_features = features[index]
        self.example_labels = labels[index]


class ExamplesList(list):
    def __init__(self, feature_definitions, label_definitions, *args, **kwargs):
        self.super(ExamplesList, self).__init__(*args, **kwargs)
        self.features = FeaturesDict(feature_definitions)
        self.labels = LabelsDict(examples_data, label_definitions)

        self._indices = self._get_merged_indices()

    def __getitem__(self, index):
        return Example(index, self.features, self.labels)

    def _get_labels_indices(self):
        return list(self.labels.keys())

    def _get_features_indices(self):
        return list(self.features.keys())

    def _get_merged_indices(self):
        features_indices = self._get_features_indices()
        labels_indices = self._get_labels_indices()

        labels_only_indices = []
        for labels_index in labels_indices:
            if labels_index not in features_indices:
                labels_only_indices.append(labels_index)

        return self.features.indices + labels_only_indices

    def update_feature_definitions(self, feature_definitions):
        self.features.update(feature_definitions)
        self._indices = self._get_merged_indices()

    def update_label_definitions(self, label_definitions):
        self.labels.update_label_definitions(label_definitions)

    def update_labels(self, examples_data):
        self.labels.update(examples_data)
        self._indices = self._get_merged_indices()
