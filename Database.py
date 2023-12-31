import pypyodbc as odbc

# Database connection settings
db_server = "localhost"
db_port = 1433
db_database = "Werkstattfertigung"
db_user = "aymenA"
db_password = "1234"


class Database:
    def __init__(self):
        self.connection = None
        self.cursor = None

        try:
            # Connect to the database
            self.connection = odbc.connect(
                f"DRIVER={{ODBC Driver 17 for SQL Server}};"
                f"SERVER={db_server},{db_port};"
                f"DATABASE={db_database};"
                f"UID={db_user};"
                f"PWD={db_password}"
            )
            self.cursor = self.connection.cursor()
            print("Database connection successful.")
        except odbc.Error as error:
            print("Error connecting to the database:", error)

    def execute_query(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.connection.commit()
        except odbc.Error as error:
            print("Error executing query:", error)

    def fetch_one(self):
        result = None
        try:
            if self.cursor.description is not None:
                result = self.cursor.fetchone()
        except Exception as e:
            print("Error fetching data:", str(e))
        return result

    def get_all_rows(self,query, params=None):
        try:
            self.cursor.execute(query,params)
            return self.cursor.fetchall()
        except Exception as e:
            print("Error fetching data:", str(e))
            return []

    def close(self):
        # Clean up resources
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def get_production_plan(self, auftrag_nr):
        query = "SELECT ag_nr, MaschineNr, dauer FROM Arbeitsplan WHERE auftrag_nr = ? ORDER BY ag_nr"
        params = (auftrag_nr,)
        results = self.get_all_rows(query, params)

        production_plan = []
        if results:
            for result in results:
                ag_nr, maschine, dauer = result
                production_plan.append((ag_nr, maschine, dauer))

        return production_plan
