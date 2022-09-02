import sqlite3

conn = sqlite3.connect('employee.db')

#alllowas to run sql commands
c = conn.cursor()

# c.execute('''CREATE TABLE employees(
# first_name text,
# last_name text,
# pay integer )
#   ''')

c.execute('INSERT INTO employees Values ("Mateus", "Goncalves De Ouro", 25000)')

print(c.execute('SELECT * FROM employees WHERE first_name = "Mateus" '))

conn.commit()

conn.close()