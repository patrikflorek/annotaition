# feature_definitions/image.py

from glob import glob

from PIL import Image

from .base import BaseFeatureDefinition


class ImageFeatureDefinition(BaseFeatureDefinition):
    def get_data_field_values(self):
        image_file_paths = self.get_indices()
        field_values = {index: {} for index in image_file_paths}
        for image_file_path in image_file_paths:
            field_values[image_file_path]["File path"] = image_file_path

            image = Image.open(image_file_path)
            field_values[image_file_path]["Size"] = image.size
            
            exif_data = image.getexif()
            date_time = exif_data.get(306, '') # DateTime EXIF tag
            field_values[image_file_path]["Creation date time"] = date_time

        return field_values

    def get_indices(self):
        image_file_paths = []
        for data_field in self.data_fields:
            if data_field.type == "file_path" and data_field.source == "file_paths":
                for file_paths_pattern in data_field.source_file_paths:
                    image_file_paths.extend(glob(file_paths_pattern))
        
        image_file_paths.sort()

        return image_file_paths

