# src/main/main.py

from src.main.db.rds_connector import *
import configparser
import os
from sqlalchemy import text

# Absolute path to the config file
config_file = os.path.abspath("resources/config_file.ini")

# Load config
config = configparser.ConfigParser()
config.read(config_file)

def main():
    if "database" not in config:
        logger.error("❌ Missing [database] section in config file.")
        print("Sections found:", config.sections())
        return

    # Create DB connection
    mysql_db_connection = MySqlConnection(config)
    mysql_db_connection.connect()

    # ✅ Pass full connection object
    crud_operation_object = MySqlCRUDOperation(mysql_db_connection)

    # ✅ Replace these with actual column names in the "labours" table
    query = """
        INSERT INTO labours (first_name, last_name, wage, role, email)
        VALUES (:first_name, :last_name, :wage, :role, :email)
    """
    params = {
        "first_name": "Alice",
        "last_name": "Smith",
        "wage": 3000,
        "role": "Engineer",
        "email": "alice.smith@example.com"
    }

    try:
        crud_operation_object.insert_from_mysql(query, params)
    except Exception as e:
        logger.error(f"❌ Insert failed: {e}")
        return

    try:
        final_result = crud_operation_object.read_from_rds("SELECT * FROM labours")
        logger.info(f"✅ Query result:\n{final_result}")
    except Exception as e:
        logger.error(f"❌ Read failed: {e}")

    mysql_db_connection.close()

if __name__ == "__main__":
    main()
