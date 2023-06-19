class BufferStore:
    def __init__(self, database):
        self.database = database
        self.parts = []

    def add_part(self, part, machine):
        self.parts.append((part, machine))

    def remove_part(self, part):
        if part in self.parts:
            self.parts.remove(part)

    def get_parts(self):
        return self.parts
