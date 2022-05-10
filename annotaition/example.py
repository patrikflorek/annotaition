# example.py

class ExamplesDict(dict):
    def __init__(self, feature_definitions, label_definitions):
        self.feature_definitions = feature_definitions
        self.label_definitions = label_definitions
