from Machine import Machine


class Machines:
    def __init__(self, database, buffer_store):
        self.database = database
        self.buffer_store = buffer_store

    def get_available_machine(self):
        query = "SELECT MaschineNr, Bezeichnung, verf_von, verf_bis, Kap_Tag FROM Maschine;"
        self.database.execute_query(query)
        results = self.database.fetch_all()  # Fetch all available machines

        if results:
            for result in results:
                machine_number, description, verf_von, verf_bis, kap_tag = result
                machine = Machine(machine_number, description, verf_von, verf_bis, kap_tag)
                machine.set_database(self.database)
                print(machine)  # Print each machine's information
                return machine

        return None
