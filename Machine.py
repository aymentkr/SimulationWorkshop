class Machine:
    def __init__(self, number, description, verf_von, verf_bis, kap_tag):
        self.number = number
        self.description = description
        self.verf_von = verf_von
        self.verf_bis = verf_bis
        self.kap_tag = kap_tag
        self.database = None  # Placeholder for the database instance

    def set_database(self, database):
        self.database = database

    def process_part(self, part):
        query = "UPDATE Maschine SET verf_von = GETDATE(), verf_bis = DATEADD(MINUTE, dauer, GETDATE()) WHERE MaschineNr = ?;"
        params = (self.number,)
        self.database.execute_query(query, params)

    def __str__(self):
        return f"Machine {self.number}: {self.description}\n" \
               f"Availability: {self.verf_von} - {self.verf_bis}\n" \
               f"Capacity per day: {self.kap_tag} hours\n"
