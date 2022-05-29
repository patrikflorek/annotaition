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
            else:
                feature_definition = BaseFeatureDefinition(
                    feature_definition_dict)

            self.append(feature_definition)

    def get_indices(self):
        indices_set = set()
        for feature_definition in self:
            feature_indices = feature_definition.get_indices()
            indices_set = indices_set.union(set(feature_indices))

        sorted_indices = sorted(list(indices_set))
        return sorted_indices

    def get_data_field_values(self):
        indices = self.get_indices()
        values = {index: {} for index in indices}
           
        for feature_definition in self:
            feature_data_field_values = feature_definition.get_data_field_values()
            for index in indices:
                feature_name = feature_definition.name
                data_field_values = {}
                values[index][feature_name] = data_field_values
                for data_field in feature_definition.data_fields:
                    data_field_name = data_field.name
                    values[index][feature_name][data_field_name] = feature_data_field_values[index][data_field_name]
                    
        return values
