import sqlite3

try:
    # Connect to the SQLite database
    conn = sqlite3.connect('colonialAdventure.db')
    cursor = conn.cursor()
    print("Connected to the database.")

    # Define a function to fetch and print data from a table
    def print_table(table_name):
        print(f"Contents of {table_name}:")
        cursor.execute(f"SELECT * FROM {table_name};")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print()

    # Print contents of each table
    print_table('GUIDE')
    print_table('CUSTOMER')
    print_table('RESERVATION')
    print_table('TRIP')
    print_table('TRIP_GUIDES')
    print_table('PARTICIPANTS')
    print_table('ADVENTURE_CLASS')
    print_table('IND_PARTICIPANT')
    print_table('CLASS')

except sqlite3.Error as e:
    print("Error connecting to the database:", e)

finally:
    # Close the database connection
    if conn:
        conn.close()
        print("Database connection closed.")
