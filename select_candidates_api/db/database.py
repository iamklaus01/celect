import databases
import sqlalchemy

DATABASE_URL = "postgresql://klaus:sc_api_2022@localhost/celect"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(DATABASE_URL)
