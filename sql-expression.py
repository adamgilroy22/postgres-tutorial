from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing the instructions from our localhost "chinook" db
# three / means it's hosted locally
db = create_engine("postgresql:///chinook")

meta = MetaData(db)

# making the connection
with db.connect() as connection:
