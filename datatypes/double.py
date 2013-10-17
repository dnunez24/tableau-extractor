from dataextract import Type

class Double:
    def __init__(self, column, value, format = None):
        self.column = column
        self.value = self.convert(value)

    def add_to_row(self, row):
        return row.setDouble(self.column, self.value)

    def convert(self, value):
        return float(value)

    def type(self):
        return Type.DOUBLE