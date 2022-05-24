# components/feature_definition.py

from annotaition.feature_definitions import (
    BaseFeatureDefinition,
    ImageFeatureDefinition)


class FeatureDefinitionsList(list):
    def update(self, feature_definitions_list):
        self.clear()
        for feature_definition_dict in feature_definitions_list:
            if feature_definition_dict['type'] == 'image':
                feature_definition = ImageFeatureDefinition(
                    feature_definition_dict)
                feature_definition.get_data_field_values()
            else:
                feature_definition = BaseFeatureDefinition(
                    feature_definition_dict)

            self.append(feature_definition)
