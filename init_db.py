import sqlite3

def initialize():
    # Connect to the database file (creates it if it doesn't exist)
    connection = sqlite3.connect('cctv_monitor.db')
    
    with open('schema.sql', 'r') as f:
        schema_script = f.read()
    
    # Run the SQL commands
    connection.executescript(schema_script)
    
    connection.commit()
    connection.close()
    print("Database 'cctv_monitor.db' initialized successfully! 🚀")

if __name__ == "__main__":
    initialize()
