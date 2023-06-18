import random


class BufferStore:
    def __init__(self, database):
        self.database = database

    def add_part(self, part, machine):
        query = "INSERT INTO Arbeitsplan VALUES (?, ?, ?, ?);"

        # Retrieve Auftrag_nr from the Auftrag table
        auftrag_query = "SELECT TOP 1 Auftrag_nr FROM Auftrag ORDER BY Auftrag_nr;"
        auftrag_result = self.database.get_all_rows(auftrag_query)
        auftrag_nr = auftrag_result[0][0] if auftrag_result else None

        if auftrag_nr is not None:
            params = (auftrag_nr, part.id, machine.machine_number, part.duration)
            self.database.execute_query(query, params)
        else:
            print("No Auftrag_nr found in the Auftrag table.")
