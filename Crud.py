import sqlite3
"""
Module containing queries for CRUD operations designed for CheeseWiz.py

The queries are string literals, accepting values only for expected parameters.
Written by Patty Mosher
"""

# Query Strings
drop_table_qry = "DROP TABLE IF EXISTS cheeses"
create_table_qry = 'CREATE TABLE IF NOT EXISTS cheeses(CheeseId INTEGER PRIMARY KEY, ' \
                   'CheeseNameEn TEXT, ManufacturerProvCode TEXT, ManufacturingTypeEn TEXT, ' \
                   'WebSiteEn TEXT, FatContentPercent REAL, MoisturePercent REAL, ' \
                   'ParticularitiesEn TEXT, FlavourEn TEXT, CharacteristicsEn TEXT, ' \
                   'RipeningEn TEXT, Organic INTEGER, CategoryTypeEn TEXT, MilkTypeEn TEXT, ' \
                   'MilkTreatmentTypeEn TEXT, RindTypeEn TEXT, LastUpdateDate TEXT);'
create_qry = 'INSERT INTO cheeses VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);'
read_by_id_qry = 'SELECT * FROM cheeses WHERE CheeseId=?;'
# Parameters in order: col name, new val, cheese id
update_by_id_qry = 'UPDATE cheeses set ?="?" WHERE CheeseId=?;'
delete_by_id_qry = 'DELETE FROM cheeses WHERE CheeseId=?;'


def init_db():
    """Creates database or connects to database if it already exists, drops table, recreates table, """
    try:
        db = sqlite3.connect('cheese')
        cursor = db.cursor()
        drop_table()
        cursor.execute(create_table_qry)
        db.commit()
        db.close()
    except:
        print("Cannot connect to database")


def drop_table():
    """Drops cheeses table if it exists"""
    try:
        db = sqlite3.connect('cheese')
        cursor = db.cursor()
        cursor.execute(drop_table_qry)
        db.commit()
        db.close()
    except:
        print("Cannot connect to database")


def create_cheese(CheeseId, CheeseNameEn, ManufacturerProvCode, ManufacturingTypeEn,
                  WebSiteEn, FatContentPercent, MoisturePercent, ParticularitiesEn,
                  FlavourEn, CharacteristicsEn, RipeningEn, Organic, CategoryTypeEn,
                  MilkTypeEn, MilkTreatmentTypeEn, RindTypeEn, LastUpdateDate):
    """Reads in values for each column, and creates a new cheese record based on those values"""
    try:
        db = sqlite3.connect('cheese')
        cursor = db.cursor()
        print("connected")
        cursor.execute(create_qry, (CheeseId, CheeseNameEn, ManufacturerProvCode, ManufacturingTypeEn, WebSiteEn,
                                    FatContentPercent, MoisturePercent, ParticularitiesEn, FlavourEn, CharacteristicsEn,
                                    RipeningEn, Organic, CategoryTypeEn, MilkTypeEn, MilkTreatmentTypeEn, RindTypeEn,
                                    LastUpdateDate) )
        print("Record added:  CheeseId: " + str(CheeseId) + ", CheeseName: " + CheeseNameEn)
        db.commit()
        db.close()
    except:
        print("Error creating cheese record")


def read_cheese_by_id(CheeseId):
    """Returns a record matching the CheeseId parameter"""
    try:
        db = sqlite3.connect('cheese')
        cursor = db.cursor()
        record = cursor.execute(read_by_id_qry, str(CheeseId))
        return record.fetchone()
        db.close()
    except:
        return "Cannot find record with CheeseId {}".format(CheeseId)


def read_all():
    """Reads all the records in the database"""
    try:
        db = sqlite3.connect('cheese')
        cursor = db.cursor()
        records = cursor.execute("SELECT * FROM cheeses").fetchall()
        db.close()
        return records
    except:
        return "Cannot connect to database"


def filtered_read(criteria):
    """Takes in SQL constructed in Controller. """
    try:
        db = sqlite3.connect('cheese')
        cursor = db.cursor()
        records = cursor.execute(criteria).fetchall()
        db.close()
        return records
    except:
        return "Cannot connect to database"


def update_cheese_by_id(col_name, new_val, CheeseId):
    """Updates the column col_name to new_val for the record matching CheeseId"""
    try:
        db = sqlite3.connect('cheese')
        cursor = db.cursor()
        cursor.execute(update_by_id_qry, (str(col_name), str(new_val), str(CheeseId)))
        print("CheeseId {}: Updated {} to {} successfully".format(CheeseId, col_name, new_val))
        db.commit()
        db.close()
    except:
        print("Update not successful")


def delete_cheese_by_id(cheese_id):
    """Deletes the record matching the CheeseId"""
    try:
        db = sqlite3.connect('cheese')
        cursor = db.cursor()
        cursor.execute(delete_by_id_qry, str(cheese_id))
        print("{} deleted successfully".format(cheese_id))
        db.commit()
        db.close()
    except:
        print("Cannot delete record")