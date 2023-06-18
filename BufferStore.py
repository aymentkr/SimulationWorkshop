import random


class BufferStore:
    def __init__(self, database):
        self.database = database

    def add_part(self, part, machine):
        query = "INSERT INTO Arbeitsplan (Auftrag_nr, ag_nr, MaschineNr, dauer) VALUES (?, ?, ?, ?);"
        params = (part.id, part.id, machine.machine_number, random.randint(1, 3))
        self.database.execute_query(query, params)