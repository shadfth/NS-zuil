import json
import psycopg2

def insert_to_database(beoordeeld):
    conn = psycopg2.connect(
        host="localhost",
        database="ns_zuil",
        user="postgres",
        password="Babyborn123",
        port=5432)

    # Open a cursor to perform database operations
    cur = conn.cursor()

    script_bericht = f"""INSERT INTO bericht (naam, bericht, tijd, datum, station, moderator_nummer) 
                        VALUES (%s,%s,%s,%s,%s,%s);"""
    data = (beoordeeld['bericht']['naam'],beoordeeld['bericht']['bericht'],beoordeeld['bericht']['tijd'],beoordeeld['bericht']['datum'],beoordeeld['bericht']['station'],beoordeeld['ID'])
    # Execute a command: this creates a new table
    cur.execute(script_bericht,data)
    # Make the changes to the database persistent
    conn.commit()

    conn.close()
