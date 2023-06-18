import random
import time

from BufferStore import BufferStore
from Database import Database
from Machines import Machines
from Part import Part

# Global variables
stop_simulation = False


# Define the WorkshopSimulation class
class WorkshopSimulation:
    def __init__(self):
        self.database = Database()
        self.buffer_store = BufferStore(self.database)
        self.machines = Machines(self.database, self.buffer_store)

    def main(self):
        # Start the simulation
        print("Workshop Production Simulation")
        print("-------------------------------")
        print("INFO: Enter a string value if you want to exit.")
        print()

        # Start the simulation loop
        part_id = 1

        while not stop_simulation:

            # Generate a new part
            part = Part(part_id)
            part_id += 1

            print(f"New Part: {part.id}")

            # Retrieve available machines
            machines = self.machines.get_available_machines()
            if machines:
                # Move part to all available machines
                for machine in machines:
                    print(machine)
                    self.process_part(part, machine)
            else:
                # Buffer store is full, wait until there's space available
                print("Buffer Store is full. Waiting...")
                time.sleep(2)  # Simulate waiting time
                machines = self.machines.get_available_machines()
                if machines:
                    # Move part to all available machines
                    for machine in machines:
                        self.process_part(part, machine)
                else:
                    print("No available machines.")

            # Simulate processing time
            time.sleep(random.randint(1, 3))

    def process_part(self, part, machine):
        print(f"Processing Part {part.id} on Machine {machine.machine_number}")
        machine.process_part(part)
        self.buffer_store.add_part(part, machine)

        print(f"Part {part.id} moved to the buffer store.")
        print()