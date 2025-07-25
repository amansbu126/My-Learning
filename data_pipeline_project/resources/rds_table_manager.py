import psycopg2

class RDSTableManager:
    def create_employee_table(self):
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS employee_details (
            company TEXT,
            location TEXT,
            department TEXT,
            employee_id TEXT PRIMARY KEY,
            name TEXT,
            role TEXT,
            skills TEXT,
            campaigns TEXT
        );
        """
