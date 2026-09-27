class ISBNPersnnoliseConverter:
    regex = r"[0-9]{13}"
    def to_python(self, value):
        return value
    def to_url(self, value):
        return str(value)
