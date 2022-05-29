# components/label_definition.py

class LabelCategory():
    def __init__(self, category_dict):
        self.name = category_dict["name"]
        self.avatar = category_dict.get('avatar', None)
        self.color = category_dict.get("color", None)

    def __repr__(self):
        return str(self.__dict__)


class LabelCategoriesList(list):
    def __init__(self, categories_list, *args, **kwargs):
        super(LabelCategoriesList, self).__init__(*args, **kwargs)
        for category_dict in categories_list:
            category = LabelCategory(category_dict)
            self.append(category)


class LabelDataFieldDefinition():
    def __init__(self, data_field_dict):
        self.name = data_field_dict['name']
        self.type = data_field_dict.get('type', None)
        self.icon = data_field_dict.get('icon', '')

        if self.type == 'category':
            categories_list = data_field_dict.get('categories', [])
            self.categories = LabelCategoriesList(categories_list)

    def __repr__(self):
        return str(self.__dict__)


class LabelDataFieldDefinitionsList(list):
    def __init__(self, data_fields_list, *args, **kwargs):
        super(LabelDataFieldDefinitionsList, self).__init__(*args, **kwargs)
        for data_field_dict in data_fields_list:
            data_field = LabelDataFieldDefinition(data_field_dict)
            self.append(data_field)


class LabelDefinition():
    def __init__(self, label_definition_dict):
        self.name = label_definition_dict['name']
        self.description = label_definition_dict.get('description', '')
        self.type = label_definition_dict.get('type', None)
        self.icon = label_definition_dict.get('icon', '')

        data_fields = label_definition_dict.get('data_fields', [])
        self.data_fields = LabelDataFieldDefinitionsList(data_fields)

    def __repr__(self):
        return str(self.__dict__)


class LabelDefinitionsList(list):
    def update_label_definitions(self, labels_definitions_data):
        self.clear()
        for label_definition_dict in labels_definitions_data:
            label_definition = LabelDefinition(label_definition_dict)
            self.append(label_definition)
