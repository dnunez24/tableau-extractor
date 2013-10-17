class Schema:
    def __init__(self, schema):
        self.has_headers = schema["has_headers"]
        self.parse(schema["fields"])

    def parse(fields):
        self.names = []
        self.types = []
        self.formats = []

        for field in fields:
            self.names.append(field["name"])
            self.types.append(field["type"])
            self.formats.append(field.get("format"))
