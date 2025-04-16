import pymysql

class DBconnect(object):
    def __init__(self):
        self.dbconnection = pymysql.connect(
        host= "localhost",
        port=int(3306),
        user="root",
        passwd="Thinhnguyen2491") # Change the password to your own MySQL password
        
        self.dbcursor = self.dbconnection.cursor()

    def commit_db(self):
        self.dbconnection.commit()
    
    def close_db(self):
        self.dbcursor.close()
        self.dbconnection.close()

db = DBconnect()

# Execute SQL command
def execute_command(connection, command, value=None):
    cursor = connection.dbcursor
    try:
        if command.strip() != '':
            if value is not None:
                cursor.execute(command, value)
            else:
                cursor.execute(command)

    except pymysql.Error as err:
            print(f"Error executing command: {err}")
    
# Establish the database connection
def create_database(db):
    command_types = {
        'DROP DATABASE': [],
        'CREATE DATABASE': [],
        'USE': [],
        'DROP TABLE': [],
        'CREATE TABLE': []
    }

    # Store the SQL commands in a list
    with open('db/create-db.sql', 'r') as file:
        sql = file.read()
        commands = sql.split(';')
        for command in commands:
            for command_type in command_types:
                if command_type in command:
                    command_types[command_type].append(command)

    # Execute each command
    for command_type, command_list in command_types.items():
        for command in command_list:
            execute_command(db, command)

    print("Database is created successfully.")

create_database(db)