from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from loguru import logger
import csv

class MySqlConnection:
    def __init__(self, config):
        self.config = config
        self.session = None
        self.engine = None

    def connect(self):
        try:
            # Get database config
            db_config = self.config["database"]
            user = db_config["user"]
            password = db_config["password"]
            host = db_config["host"]
            port = db_config["port"]
            database = db_config["database"]
            schema = db_config.get("schema", "public")  # default schema
            db_type = db_config.get("db_type", "postgresql")  # default DB type

            # Create connection string
            connection_string = f"{db_type}://{user}:{password}@{host}:{port}/{database}"
            self.engine = create_engine(connection_string)
            logger.info("Connection Successful ✅")

            # Create session
            Session = sessionmaker(bind=self.engine)
            self.session = Session()

        except Exception as e:
            logger.error(f"Error occurred: {e}")

    def close(self):
        if self.session:
            self.session.close()
            logger.info("🔒 Session closed.")


class MySqlCRUDOperation:
    def __init__(self, mysql_connection):
        self.connection = mysql_connection

    def _set_schema(self, session):
        db_type = self.connection.config["database"].get("db_type", "postgresql")
        if db_type == "postgresql":
            schema = self.connection.config["database"].get("schema", "public")
            session.execute(text(f"SET search_path TO {schema}"))

    def read_from_rds(self, query):
        session = None
        try:
            # Ensure the engine is initialized
            if not self.connection.engine:
                self.connection.connect()

            # Get engine from the connection object (NOT from session)
            engine = self.connection.engine

            # Create a new session
            Session = sessionmaker(bind=engine)
            session = Session()

            # ✅ Set search_path for PostgreSQL
            db_type = self.connection.config["database"].get("db_type", "postgresql")
            if db_type == "postgresql":
                schema = self.connection.config["database"].get("schema", "public")
                session.execute(text(f"SET search_path TO {schema}"))

            # Run the query
            data = session.execute(text(query)).fetchall()
            logger.info(f"{data}")
            return data

        except Exception as e:
            logger.error(f"❌ Error occurred in mysql query run: {e}")
            raise e

        finally:
            if session:
                session.close()
                logger.info("🔒 Session closed.")

    def insert_from_mysql(self, query, parameters):
        session = None
        try:
            # Use existing engine or create a new one
            if not self.connection.engine:
                self.connection.connect()
            engine = self.connection.engine

            # Create session
            Session = sessionmaker(bind=engine)
            session = Session()

            # ✅ Set search_path for PostgreSQL
            db_type = self.connection.config["database"].get("db_type", "postgresql")
            if db_type == "postgresql":
                schema = self.connection.config["database"].get("schema", "public")
                session.execute(text(f"SET search_path TO {schema}"))

            # Execute insert/update/delete with parameters
            session.execute(text(query), parameters)

            # ✅ Commit the transaction
            session.commit()
            logger.info("✅ Data inserted and committed successfully.")

        except Exception as e:
            if session:
                session.rollback()  # ❌ Roll back if error occurs
            logger.error(f"❌ Error occurred in MySQL insert: {e}")
            raise e

        finally:
            if session:
                session.close()
                logger.info("🔒 Session closed.")

    def insert_from_csv(self, csv_path, table_name):
        session = None
        try:
            if not self.connection.engine:
                self.connection.connect()
            Session = sessionmaker(bind=self.connection.engine)
            session = Session()
            self._set_schema(session)

            with open(csv_path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    logger.info(f"Inserting row: {row}")
                    columns = ', '.join(row.keys())
                    placeholders = ', '.join([f":{col}" for col in row.keys()])
                    query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
                    session.execute(text(query), row)

            session.commit()
            logger.info("✅ CSV data inserted successfully.")

        except Exception as e:
            logger.error(f"❌ Error inserting from CSV: {e}")
        finally:
            if session:
                session.close()
                logger.info("🔒 Session closed after CSV insert.")
