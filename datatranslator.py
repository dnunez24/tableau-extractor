import tableau.datatypes

class DataTranslator:
    @staticmethod
    def translate(data_type, **kwargs):
        column = kwargs["column"]
        value = kwargs["value"]
        format = kwargs.get("format")

        _class = getattr(datatypes, data_type)
        return _class(column, value, format)
