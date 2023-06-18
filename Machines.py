from Machine import Machine


class Machines:
    def __init__(self, database, buffer_store):
        self.database = database
        self.buffer_store = buffer_store

    def get_available_machine(self):
        query = "SELECT * FROM Maschine;"
        results = self.database.get_all_rows(query)  # Fetch all available machines
        if results:
            for result in results:
                machine_number, description, verf_von, verf_bis, kap_tag = result
                machine = Machine(machine_number, description, verf_von, verf_bis, kap_tag)
                machine.set_database(self.database)

                print(machine)  # Print each machine's information
                return machine

        return None
