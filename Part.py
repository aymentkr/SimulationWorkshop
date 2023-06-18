class Part:
    def __init__(self, part_id):
        self.id = part_id
        self.duration = None

    def __str__(self):
        return f"Part {self.id}"

    def read_duration(self):
        duration = input("Enter the duration value for the part: ")
        self.duration = int(duration) if duration.isdigit() else None