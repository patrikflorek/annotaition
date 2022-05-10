# annotation.py

import json


from feature_definition import FeatureDefinitionsList
from label_definition import LabelDefinitionsList
from example import ExamplesDict


class Annotation():
    @property
    def filepath(self):
        return self._filepath

    @filepath.setter
    def filepath(self, value):
        self._filepath = value

    def __init__(self):
        self.filepath = None

        self.title = ''
        self.description = ''
        self.remote_server = None
        self.index_feature_name = None
        self.index_data_field_name = None

        self.feature_definitions = FeatureDefinitionsList()

        self.label_definitions = LabelDefinitionsList()

        self.examples = ExamplesDict(
            feature_defintions=self.feature_definitions,
            label_definitions=self.label_definitions
        )

    def set_data(self, data):
        self.title = data.get('title', '')
        self.description = data.get('description', '')
        self.remote_server = data.get('remote_server', None)
        self.index_feature_name = data['index_feature_name']
        self.index_data_field_name = data['index_data_field_name']

        feature_definitions_data = data.get('feature_definitions', [])
        self.feature_definitions.update(feature_definitions_data)

        label_definitions_data = data.get('label_definitions', [])
        self.label_definitions.update(label_definitions_data)

        labels_dict = data.get('labels', {})
        self.examples.update(labels_dict)

    def load_json(self, filepath):
        f = open(filepath)
        data = json.load(f)
        self.set_data(data)
        self.filepath = filepath
