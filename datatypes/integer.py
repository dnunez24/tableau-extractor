from dataextract import Type

class Integer:
    def __init__(self, column, value, format = None):
        self.column = column
        self.value = self.convert(value)

    def add_to_row(self, row):
        return row.setInteger(self.column, self.value)

    def convert(self, value):
        return int(value)

    def type(self):
        return Type.INTEGER