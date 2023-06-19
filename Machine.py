import WorkshopSimulation


class Machine:
    processing_time = 24*60
    def __init__(self, machine_number, description, verf_von, verf_bis, kap_tag):
        self.machine_number = machine_number
        self.description = description
        self.verf_von = verf_von
        self.verf_bis = verf_bis
        self.kap_tag = kap_tag
        self.database = None  # Placeholder for the database instance

    def set_database(self, database):
        self.database = database

    def process_part(self, part, duration, day_count):
        if self.kap_tag > 0 and self.processing_time >= duration:
            self.kap_tag -= 1
            self.processing_time -= duration
            print(f"Processing Part {part} on Machine {self.machine_number}")
            print(f"Processing time: {duration} minutes")
            print(f"Capacities left: {self.kap_tag}")
        elif self.processing_time < duration:
            self.processing_time = 24 * 60  # Reset processing time for a new day
            print(f"Machine {self.machine_number} has reached the maximum processing time for day {day_count}.")
        else:
            print("The machine has reached the maximum processing capacity.")

    def __str__(self):
        return f"Machine Number: {self.machine_number}, Verification From: {self.verf_von}, Verification To: {self.verf_bis}, Capacity per Tag: {self.kap_tag}"