from Machine import Machine
from datetime import datetime


class Machines:
    def __init__(self, database, buffer_store):
        self.database = database
        self.buffer_store = buffer_store

    def get_available_machines(self):
        current_date = datetime.now().date()
        query = "SELECT * FROM Maschine;"
        results = self.database.get_all_rows(query)  # Fetch all machines
        machines = []

        if results:
            for result in results:
                machine_number, description, verf_von, verf_bis, kap_tag = result
                machine = Machine(machine_number, description, verf_von, verf_bis, kap_tag)
                machine.set_database(self.database)

                # Check if the machine is available
                if verf_bis is None or verf_bis > current_date:
                    machines.append(machine)
        return machines
