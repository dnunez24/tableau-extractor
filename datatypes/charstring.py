from dataextract import Type

class CharString:
    def __init__(self, column, value, format = None):
        self.column = column
        self.value = self.convert(value)

    def add_to_row(self, row):
        return row.setCharString(self.column, self.value)

    def convert(self, value):
        return str(value)

    def type(self):
        return Type.CHAR_STRING