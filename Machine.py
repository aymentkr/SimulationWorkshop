class Machine:
    def __init__(self, machine_number, description, verf_von, verf_bis, kap_tag):
        self.machine_number = machine_number
        self.description = description
        self.verf_von = verf_von
        self.verf_bis = verf_bis
        self.kap_tag = kap_tag
        self.database = None  # Placeholder for the database instance

    def set_database(self, database):
        self.database = database

    def process_part(self, part):
        query = "UPDATE Maschine SET verf_von = GETDATE(), verf_bis = DATEADD(MINUTE, dauer, GETDATE()) WHERE MaschineNr = ?;"
        params = (self.machine_number,)
        self.database.execute_query(query, params)

    def __str__(self):
        return f"Machine Number: {self.machine_number}, Verification From: {self.verf_von}, Verification To: {self.verf_bis}, Capacity per Tag: {self.kap_tag}"

