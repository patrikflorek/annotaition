# annotation.py

import json

from annotaition.components.feature_definition import FeatureDefinitionsList
from annotaition.components.label_definition import LabelDefinitionsList
from annotaition.components.example import ExamplesDict


class Annotation():
    def __init__(self):
        self.title = ''
        self.description = ''

        self.feature_definitions = FeatureDefinitionsList()
        self.label_definitions = LabelDefinitionsList()

        self.examples = ExamplesDict(
            self.feature_definitions, self.label_definitions)

    def __repr__(self):
        return str(self.__dict__)

    def get_indices(self):
        return self.examples.get_indices()

    def get_example(self, index):
        return self.examples[index]

    def update_feature_definitions(self, feature_definitions_data):
        self.feature_definitions.update(feature_definitions_data)
        self.examples.update_feature_definitions(self.feature_definitions)

    def update_label_definitions(self, label_definitions_data):
        self.label_definitions.update_label_definitions(label_definitions_data)
        self.examples.update_label_definitions(self.label_definitions)

    def update_labels(self, examples_data):
        self.examples.update_labels(examples_data)

    def update_data(self, data):
        self.title = data.get('title', '')
        self.description = data.get('description', '')

        feature_definitions_data = data.get('feature_definitions', [])
        self.update_feature_definitions(feature_definitions_data)

        label_definitions_data = data.get('label_definitions', [])
        self.update_label_definitions(label_definitions_data)

        examples_data = data.get('examples', [])
        self.update_labels(examples_data)

    def load_json(self, filepath):
        f = open(filepath)
        data = json.load(f)
        self.update_data(data)
