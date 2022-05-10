# label_definition.py


class LabelCategory():
    def __init__(self, category_dict):
        self.name = category_dict["name"]
        self.avatar = category_dict.get('avatar', None)
        self.color = category_dict.get("color", None)


class LabelCategoriesList(list):
    def __init__(self, categories_list, *args, **kwargs):
        super(LabelCategoriesList, self).__init__(*args, **kwargs)
        for category_dict in categories_list:
            category = LabelCategory(category_dict)
            self.append(category)


class LabelDefinitionDataField():
    def __init__(self, data_field_dict):
        self.name = data_field_dict['name']
        self.type = data_field_dict.get('type', None)
        self.icon = data_field_dict.get('icon', '')

        if self.type == 'selection':
            options = data_field_dict['options']

            # Options can be either a list or a string
            if isinstance(options, list):
                self.options = options.copy()
            else:
                self.options = options


class LabelDefinitionDataFieldsList(list):
    def __init_(self, data_fields_list, *args, **kwargs):
        super(LabelDefinitionDataFieldsList, self).__init__(*args, **kwargs)
        for data_field_dict in data_fields_list:
            data_field = LabelDefinitionDataField(data_field_dict)
            self.append(data_field)


class LabelDefinition():
    def __init__(self, label_definition_dict):
        self.name = label_definition_dict['name']
        self.description = label_definition_dict.get('description', '')
        self.type = label_definition_dict.get('type', None)
        self.icon = label_definition_dict.get('icon', '')

        if "categories" in label_definition_dict:
            categories = label_definition_dict['categories']
            self.categories = LabelCategoriesList(categories)

        data_fields = label_definition_dict.get('data_fields', [])
        self.data_fields = LabelDefinitionDataFieldsList(data_fields)


class LabelDefinitionsList(list):
    def update(self, data_list):
        self.clear()
        for label_definition_dict in data_list:
            label_definition = LabelDefinition(label_definition_dict)
            self.append(label_definition)
