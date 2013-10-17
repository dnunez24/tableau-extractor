from datetime import datetime
from dataextract import Type
from tableau.errors import missingformat

class DateTime:
    def __init__(self, column, value, format = None):
        self.column = column
        self.value = self.convert(value)

    def add_to_row(self, row):
        d = self.value
        parts = [d.year, d.month, d.day, d.hour, d.minute, d.second, d.microsecond/100]
        return row.setDateTime(self.column, *parts)

    def convert(self, value):
        if not self.format:
            raise MissingFormatError("Format is required in schema file for DateTime field type")
        return datetime.strptime(value, self.format)

    def type(self):
        return Type.DATETIME