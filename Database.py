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
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)

        self.connection.commit()

    def fetch_one(self):
        result = None
        try:
            if self.cursor.description is not None:
                result = self.cursor.fetchone()
        except Exception as e:
            print("Error fetching data:", str(e))
        return result

    def fetch_all(self):
        return self.cursor.fetchall()

    def close(self):
        # Clean up resources
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
