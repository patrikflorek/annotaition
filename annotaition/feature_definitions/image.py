# feature_definitions/image.py

from glob import glob

from PIL import Image

from .base import BaseFeatureDefinition


class ImageFeatureDefinition(BaseFeatureDefinition):
    def get_data_field_values(self):
        image_file_paths = []
        data_field_names = []
        for data_field in self.data_fields:
            data_field_names.append(data_field.name)
            if data_field.type == "file_path" and data_field.source == "file_paths":
                for file_paths_pattern in data_field.source_file_paths:
                    image_file_paths.extend(glob(file_paths_pattern))

        field_values = {field_name: [] for field_name in data_field_names}
        for image_file_path in image_file_paths:
            field_values["File path"].append(image_file_path)

            image = Image.open(image_file_path)
            field_values["Size"].append(image.size)
            
            exif_data = image.getexif()
            date_time = exif_data.get(306, '') # DateTime EXIF tag
            field_values["Creation date time"].append(date_time) 

        return field_values
