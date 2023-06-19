import time

from BufferStore import BufferStore
from Database import Database
from Machines import Machines


def stop():
    global stop_simulation
    stop_simulation = True


class WorkshopSimulation:
    def __init__(self):
        self.database = Database()
        self.buffer_store = BufferStore(self.database)
        self.machines = Machines(self.database, self.buffer_store)

    def main(self):
        # Start the simulation
        print("Workshop Production Simulation")
        print("-------------------------------")
        print()

        # Retrieve the list of auftrag_nr from the Auftrag table
        auftrag_query = "SELECT auftrag_nr FROM Auftrag"
        auftrag_results = self.database.get_all_rows(auftrag_query)
        auftrag_list = [row[0] for row in auftrag_results]

        if not auftrag_list:
            print("No Auftrag found.")
            return

        # Counters for days and total processing time
        day_count = 1
        total_processing_time = 0

        # Process auftrag_nr sequentially
        for auftrag_nr in auftrag_list:
            print(f"Day: {day_count}")

            # Retrieve the production plan for the auftrag_nr from the Arbeitsplan table
            plan_query = "SELECT ag_nr, MaschineNr, dauer FROM Arbeitsplan WHERE auftrag_nr = ? ORDER BY ag_nr"
            plan_results = self.database.get_all_rows(plan_query, (auftrag_nr,))
            plan_list = [dict(ag_nr=row[0], maschine=row[1], dauer=row[2]) for row in plan_results]

            if not plan_list:
                print(f"No production plan found for Auftrag {auftrag_nr}.")
                continue

            print(f"\nProcessing Auftrag {auftrag_nr}:")
            print("-------------------------------")
            print("Starting production steps...\n")

            # Move part through the production plan
            for step in plan_list:
                machine_number = step['maschine']
                duration = step['dauer']
                part_id = step['ag_nr']
                machine = self.machines.get_machine(machine_number)

                if machine:
                    total_processing_time += duration
                    machine.process_part(part_id, duration, day_count)
                    print(f"Part moved to the buffer store.")
                    print()

                    self.buffer_store.add_part(part_id, machine)  # Pass part_id and machine to add_part method
                else:
                    print(f"Machine {machine_number} not found.")

            print(f"Finished processing Auftrag {auftrag_nr}.\n")

            # Increment day count if total processing time exceeds 1440 minutes (24 hours)
            if total_processing_time > 1440:
                day_count += 1
                total_processing_time = 0  # Reset the total processing time

            # Simulate waiting time before processing the next Auftrag
            time.sleep(2)

        print("Simulation Summary")
        print("------------------")
        print(f"Total Days: {day_count}")
        self.buffer_store.print_buffer_store_info()
