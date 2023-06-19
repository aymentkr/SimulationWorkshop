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

    def print_buffer_store_info(self):
        print("\nBuffer Store Information")
        print("------------------------")
        if self.parts:
            for part_id, machine in self.parts:
                if machine:
                    print(f"Part ID: {part_id} | Location: {machine.description}")
                else:
                    print(f"Part ID: {part_id} | Location: Not found")
        else:
            print("Buffer Store is empty.")


