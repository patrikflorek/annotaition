# components/feature_definition.py

import os

FEATURE_DEFINITIONS_DIR = 'feature_definitions'

for module in os.listdir(os.path.dirname(FEATURE_DEFINITIONS_DIR)):
    if module == '__init__.py' or module[-3:] != '.py':
        continue
    __import__(module[:-3], locals(), globals())
del module


class FeatureDefinitionsList(list):
    def __init__(self, *args, **kwargs):
        super(FeatureDefinitionsList, self).__init__(*args, **kwargs)

    # def get_indices(self):
    #     indices = []
    #     for feature_definition in self:
    #         unique_indices = []
    #         for index in feature_definition.get_indices():
    #             if index not in indices:
    #                 unique_indices.append(index)
    #         indices.extend(unique_indices)

    #     return indices

    def update(self, feature_definitions_list):
        self.clear()
        for feature_definition_dict in feature_definitions_list:
            self.append(FeatureDefinition(feature_definition_dict))
