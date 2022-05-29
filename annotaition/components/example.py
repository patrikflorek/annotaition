# components/example.py

from annotaition.components.feature import FeaturesDict
from annotaition.components.label import LabelsDict


class ExamplesDict(dict):
    def __init__(self, feature_definitions, label_definitions, *args, **kwargs):
        super(ExamplesDict, self).__init__(*args, **kwargs)
        self.features = FeaturesDict(feature_definitions)
        self.labels = LabelsDict(label_definitions)

        self.indices = self.get_indices()

    def __getitem__(self, index):
        return (self.features[index], self.labels[index])

    def get_indices(self):
        features_indices_set = set(self.features.get_indices())
        labels_indices_set = set(self.labels.get_indices())
        indices_set = features_indices_set.union(labels_indices_set)

        sorted_indices = sorted(list(indices_set))
        return sorted_indices

    def update_feature_definitions(self, feature_definitions):
        self.features.update_feature_definitions(feature_definitions)

    def update_label_definitions(self, label_definitions):
        self.labels.update_label_definitions(label_definitions)
    
    def update_labels(self, examples_data):
        self.labels.update_examples_data(examples_data)
