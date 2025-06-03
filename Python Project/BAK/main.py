# src/main/main.py

#from src.main.db.rds_connector import read_from_rds, logger
import configparser
import os
from sqlalchemy import text

def main():
    # Absolute path to the config file
    config_file = os.path.abspath("resources/config_file.ini")

    # Load config
    config = configparser.ConfigParser()
    config.read(config_file)

    if "database" not in config:
        #logger.error("❌ Missing [database] section in config file.")
        print("Sections found:", config.sections())
        return

    # Sample query
    query = text("SELECT * FROM labours")

    # Execute query
    #final_result = read_from_rds(config, query)
    #logger.info(f"✅ Query result:\n{final_result}")

if __name__ == "__main__":
    main()
