from tableau import schemareader
from tableau import datatranslator

class CSVParser(SchemaReader):
    def __postinit__(self, **kwargs):
        self.translator = kwargs.get("translator", self.default_translator)

    def parse(self, filename):
        data = []
        rows = self.read_rows(filename)

        if self.schema.has_headers:
            rows.next()

        for row in rows:
            translated_row = []

            for column, value in enumerate(row):
                translated_value = self.translate(column, value)
                translated_row.append(translated_value)

            data.append(translated_value)

        return data

    def read_rows(self, filename):
        return csv.reader(open(filename))

    def translate(self, column, value):
        return self.translator.translate(column = column, value = value, format = self.field_formats(column))

    def default_translator(self):
        return DataTranslator