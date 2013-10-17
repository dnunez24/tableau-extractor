class SchemaReader:
    def __init__(self, schema, **kwargs):
        self.schema = schema
        self.__postinit__(**kwargs)

    def __postinit__(self, **kwargs):
        pass

    def field_names(self, column = None):
        names = self.schema.names
        return self.field_data(names, column)

    def field_types(self, column = None):
        types = self.schema.types
        return self.field_data(types, column)

    def field_formats(self, column = None):
        formats = self.schema.formats
        return self.field_data(formats, column)

    def field_data(self, data, column):
        if column:
            return data[column]
        else:
            return data
