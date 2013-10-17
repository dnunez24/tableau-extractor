import tableau.datatypes

class DataTranslator:
    @staticmethod
    def translate(data_type, **kwargs):
        column = kwargs["column"]
        value = kwargs["value"]
        format = kwargs.get("format")

        try:
            _class = getattr(datatypes, data_type + "Data")
        except Exception, e:
            raise e

        return _class(column, value, format)
