# example.py

class ExamplesDict(dict):
    def __init__(self, feature_definitions, label_definitions, *args, **kwargs):
        self.super(ExamplesDict, self).__init__(*args, **kwargs)
        self.feature_definitions = feature_definitions
        self.label_definitions = label_definitions

        self.labels_dict = {}

    def update_feature_definitions(self, feature_definitions):
        self.feature_definitions = feature_definitions

    def update_label_definitions(self, label_definitions):
        self.label_definitions = label_definitions

    def update_labels(self, labels_dict):
        self.labels_dict = labels_dict
