# components/label.py


class LabelsDict(dict):
    def __init__(self, label_definitions, examples_data=None, *args, **kwargs):
        super(LabelsDict, self).__init__(*args, **kwargs)
        self.label_definitions = label_definitions
        self.data_field_values = self._get_data_field_values(examples_data)

    def _get_blank_labels(self):
        labels_dict = {}
        for label_definition in self.label_definitions:
            label_name = label_definition.name
            data_fields_dict = {}
            labels_dict[label_name] = data_fields_dict

            for data_field in label_definition.data_fields:
                data_fields_dict[data_field.name] = None

        return labels_dict

    def __getitem__(self, index):
        if index not in self.data_field_values:
            return self._get_blank_labels()

        return self.data_field_values[index]
        
    def get_indices(self):
        return self.data_field_values.keys()

    def _get_data_field_values(self, examples_data=None):
        data_field_values = {}
        if examples_data is not None:
            for example_dict in examples_data:
                index = example_dict['index']
                indexed_labels_values = {}
                data_field_values[index] = indexed_labels_values
                
                labels_list = example_dict['labels']
                for label_dict in labels_list:
                    label_name = label_dict['name']
                    
                    indexed_labels_values[label_name] = {}
                    indexed_label_field_values = indexed_labels_values[label_name]
                    
                    data_fields_list = label_dict['data_fields']
                    for data_field_dict in data_fields_list:
                        data_field_name = data_field_dict['name']
                        data_field_value = data_field_dict['value']
                        indexed_label_field_values[data_field_name] = data_field_value

        return data_field_values

    def update_label_definitions(self, label_definitions):
        self.label_definitions = label_definitions

    def update_examples_data(self, examples_data):
        self.data_field_values = self._get_data_field_values(examples_data)
