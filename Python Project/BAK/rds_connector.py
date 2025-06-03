from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from loguru import logger

def read_from_rds(config, query):
    session = None
    try:
        # Get database config
        db_config = config["database"]
        user = db_config["user"]
        password = db_config["password"]
        host = db_config["host"]
        port = db_config["port"]
        database = db_config["database"]
        schema = db_config.get("schema", "public")  # default schema
        db_type = db_config.get("db_type", "postgresql")  # default DB type

        # Create connection string
        connection_string = f"{db_type}://{user}:{password}@{host}:{port}/{database}"
        engine = create_engine(connection_string)

        # Create session
        Session = sessionmaker(bind=engine)
        session = Session()

        # Set schema for PostgreSQL
        if db_type.startswith("postgresql"):
            session.execute(text(f"SET search_path TO {schema}"))

        # Print current schema
        result = session.execute(text("SELECT current_schema();"))
        logger.info(f"✅ Connected to schema: {result.scalar()}")

        # Execute the passed query
        data = session.execute(query).fetchall()
        return data

    except Exception as e:
        logger.error(f"❌ Error in RDS connection: {e}")
        raise

    finally:
        if session:
            session.close()
            logger.info("🔒 Session closed.")
