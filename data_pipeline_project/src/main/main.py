from src.main.db.rds_connector import *
import configparser
import os
import csv

def main():
    config_file = os.path.abspath("resources/config_file.ini")
    config = configparser.ConfigParser()
    config.read(config_file)

    if "database" not in config:
        logger.error("❌ Missing [database] section in config file.")
        return

    mysql_db_connection = MySqlConnection(config)
    mysql_db_connection.connect()
    crud = MySqlCRUDOperation(mysql_db_connection)

    csv_path = os.path.abspath("resources/labours.csv")
    crud.insert_from_csv(csv_path, "labours")

    final_result = crud.read_from_rds("SELECT * FROM labours")
    logger.info(f"✅ Data in 'labours' table:\n{final_result}")

    mysql_db_connection.close()

if __name__ == "__main__":
    main()
