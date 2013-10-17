from tableau import schemareader
from tableau import datatranslator

class CSVParser(SchemaReader):
    def __postinit__(self, **kwargs):
        self.translator = kwargs.get("translator", self.default_translator)

    def parse(self, csv_file, **fmtparams):
        rows = self.read_rows(csv_file, **fmtparams)
        self.skip_header(rows)
        return self.translate_rows(rows)

    def read_rows(self, csv_file, **fmtparams):
        return csv.reader(csv_file, **fmtparams)

    def translate_rows(self, rows):
        return [self.translate_row(row) for row in rows]

    def translate_row(self, row):
        return [self.translate_value(column, value) for column, value in enumerate(row)]

    def translate_value(self, column, value):
        format = self.field_formats(column)
        return self.translator.translate(column = column, value = value, format = format)

    def default_translator(self):
        return DataTranslator

    def has_header(self):
        return self.schema.has_header

    def skip_header(self, rows):
        if self.has_header():
            rows.next()
