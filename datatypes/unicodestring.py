from dataextract import Type

class UnicodeString:
    def __init__(self, column, value, format = None):
        self.column = column
        self.value = self.convert(value)

    def add_to_row(self, row):
        return row.setUnicodeString(self.column, self.value)

    def convert(self, value):
        return str(value)

    def type(self):
        return Type.UNICODE_STRING