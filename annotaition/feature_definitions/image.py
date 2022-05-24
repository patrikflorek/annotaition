# feature_definitions/image.py

from .base import BaseFeatureDefinition


class ImageFeatureDefinition(BaseFeatureDefinition):
    def get_data_field_values(self):
        print(
            f"Class {self.__class__.__name__} implements get_data_field_values method")
