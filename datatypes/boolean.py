from dataextract import Type
import re

class Boolean:
    def __init__(self, column, value, format = None):
        self.column = column
        self.value = self.convert(value)

    def add_to_row(self, row):
        return row.setBoolean(self.column, self.value)

    def convert(self, value):
        return bool(re.match(r'^t(rue)?|y(es)?|1$', value, re.IGNORECASE))

    def type(self):
        return Type.BOOLEAN
