import sqlite3


class Person:

    def __init__(self, id_number=-1, first_name='', last_name='', age=-1):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.id_number = id_number
        self.connection = sqlite3.connect('mydb.db')
        self.cursor = self.connection.cursor()

    # Load an object from the database
    def load_person(self, id_number):
        self.cursor.execute("""
        SELECT * FROM persons
        WHERE id = {}
        """.format(id_number))

        results = self.cursor.fetchone()

        self.id_number = id_number
        self.first_name = results[1]
        self.last_name = results[2]
        self.age = results[3]

    # Insert an object instance into a database
    def insert_person(self):
        self.cursor.execute("""
        INSERT INTO persons VALUES 
        ({}, '{}', '{}', {})
        """.format(self.id_number, self.first_name, self.last_name, self.age))

        self.connection.commit()


p1 = Person()
p1.load_person(1)
print(p1.id_number)
print(p1.first_name)
print(p1.last_name)
print(p1.age)
p2 = Person(4, "Alex", "Newgarden", 26)
p2.insert_person()

connection = sqlite3.connect('mydb.db')
cursor = connection.cursor()

cursor.execute("""
SELECT * FROM persons
""")

results = cursor.fetchall()
print(results)
connection.close()
# Create sql table

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS persons (
#      id INTEGER PRIMARY KEY,
#      first_name TEXT,
#      last_name TEXT,
#      age INTEGER
# )
# """)

# Insert values into database manually

# cursor.execute("""
# INSERT INTO persons VALUES
# (1, 'Paul', 'Smith', 24),
# (2, 'Mark', 'Walberg', 42),
# (3 ,'Anna', 'Jade', 22)
# """)

# Conditionally select values

# cursor.execute("""
# SELECT * FROM persons
# WHERE last_name = 'Smith'
# """)
#
# rows = cursor.fetchall()
# print(rows)
# connection.commit()
# connection.close()
