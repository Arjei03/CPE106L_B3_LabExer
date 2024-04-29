import sqlite3

conn = sqlite3.connect('colonialSolomaris.db')
cursor = conn.cursor()

#create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS LOCATION 
    (
    LOCATION_NUM DECIMAL (2,0) PRIMARY KEY,
    LOCATION_NAME CHAR(25),
    ADDRESS CHAR(25),
    CITY CHAR(25),
    STATE CHAR(2),
    POSTAL_CODE CHAR(5)
    )
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS CONDO_UNIT
    (
    CONDO_ID DECIMAL(4,0) PRIMARY KEY,
    LOCATION_NUM DECIMAL (2,0),
    UNIT_NUM CHAR(3),
    SQR_FT DECIMAL(5,0),
    BDRMS DECIMAL(2,0),
    BATHS DECIMAL(2,0),
    CONDO_FEE DECIMAL(6,2),
    OWNER_NUM CHAR(5) 
    )
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS OWNER
    (
    OWNER_NUM CHAR(5) PRIMARY KEY,
    LAST_NAME CHAR(25),
    FIRST_NAME CHAR(25),
    ADDRESS CHAR(25),
    CITY CHAR(25),
    STATE CHAR(2),
    POSTAL_CODE CHAR(5) 
    )
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS SERVICE_CATEGORY
    (
    CATEGORY_NUM DECIMAL(4,0) PRIMARY KEY,
    CATEGORY_DESCRIPTION CHAR(35) 
    )
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS SERVICE_REQUEST
    (
    SERVICE_ID DECIMAL(4,0) PRIMARY KEY,
    CONDO_ID DECIMAL(4,0),
    CATEGORY_NUM DECIMAL(4,0),
    DESCRIPTION CHAR(255),
    STATUS CHAR(255),
    EST_HOURS DECIMAL(4,2),
    SPENT_HOURS DECIMAL(4,2),
    NEXT_SERVICE_DATE DATE 
    )
""")

cursor.execute(
"""
    CREATE TABLE IF NOT EXISTS RENTER
    (
    RENTER_NUM DECIMAL(5,0) PRIMARY KEY,
    FIRST_NAME CHAR(25),
    MIDDLE_NAME CHAR(25),
    LAST_NAME CHAR(25),
    ADDRESS CHAR(25),
    CITY CHAR(25),
    STATE CHAR(2),
    POSTAL_CODE CHAR(5),
    PHONE_NUM INTEGER,
    EMAIL_ADD CHAR(50)
    )           
"""
)

cursor.execute("""
CREATE TABLE PROPERTY
    (
    LOCATION_NUM DECIMAL (2,0) PRIMARY KEY,
    LOCATION_NAME CHAR(25),
    ADDRESS CHAR(25),
    CITY CHAR(25),
    STATE CHAR(2),
    POSTAL_CODE CHAR(5),
    SQUARE_FOOTAGE INTEGER,
    NUM_BEDROOMS INTEGER,
    MAX_TENANT INTEGER,
    BASE_RATE INTEGER
    )
""")

cursor.execute("""
CREATE TABLE RENTAL_AGREEMENT
    (
    RENTER_NUM DECIMAL (5,0) PRIMARY KEY,
    FIRST_NAME CHAR(25),
    MIDDLE_NAME CHAR(25),
    LAST_NAME CHAR(25),
    ADDRESS CHAR(25),
    CITY CHAR(25),
    STATE CHAR(2),
    POSTAL_CODE CHAR(5),
    PHONE_NUM INTEGER,
    START_OF_RENT DATE,
    END_OF_RENT DATE,
    WEEKLY_RENT DECIMAL(4,2),
    RENTAL_PERIOD DATE
    )
""")

conn.commit()

tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
for table in tables:
    print("Table:", table[0])
    rows = cursor.execute("SELECT * FROM " + table[0]).fetchall()
    for row in rows:
        print(row)
    print()

conn.close()
