import sqlite3

connection = sqlite3.connect("data.db")
#connecting to SQLite

# -> connection.row_factory = sqlite3.Row
    ## Python + SQLite normally returns data from rows as tuple
    ## This returns a dict-like cursor

def create_table():
    with connection: #auto-commits
        connection.execute("CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);"
        )
    

def add_entry(entry_content, entry_date):
    with connection:
        connection.execute(
            "INSERT INTO entries VALUES (?, ?);", (entry_content, entry_date)
            )
            # WHEN ASKING USER INPUT - avoid SQL injection via asking for tuple 
            # SQL Injection happens when allowing user to write SQL via string format - could delete table


def get_entries():
    cursor = connection.execute('SELECT * FROM entries;')
    return cursor


