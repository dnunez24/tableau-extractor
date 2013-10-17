from tableau import schemareader
from dataextract import *

class DataExtractCreator(SchemaReader):
    def create(self, source_data, output_file):
        extract = self.create_extract(output_file)
        table = self.add_table_to_extract(extract)
        self.add_data_to_table(source_data, table)
        self.close_extract(extract)
        return extract

    def define_table(self):
        table_definition = self.create_table_definition()

        for column, name in enumerate(self.field_names()):
            table_definition.addColumn(name, self.field_types(column))

        return table_definition

    def add_table_to_extract(self, extract):
        table_definition = self.define_table()
        table = self.create_table(extract, table_definition)
        return table

    def add_data_to_table(self, source_data, table):
        for source_row in source_data:
            row = self.create_row()
            self.add_values_to_row(source_row, row)
            self.add_row_to_table(row, table)
            self.close_row(row)

    def add_values_to_row(self, source_row, row):
        for value in source_row:
            value.add_to_row(row)

    def add_row_to_table(self, row, table):
        return table.insert(row)

    def create_extract(self, output_file):
        return Extract(output_file)

    def close_extract(self, extract):
        extract.close()

    def create_table_definition(self):
        return TableDefinition()

    def create_table(self, extract, table_definition):
        return extract.addTable("Extract", table_definition)

    def create_row(self):
        return Row()

    def close_row(self, row):
        row.close()
