import sqlite3
import csv

# 1. Połączenie z bazą danych (utworzenie bazy, jeśli nie istnieje)
connection = sqlite3.connect('my_database.db')

# 2. Utworzenie kursora
cursor = connection.cursor()

# 3. Tworzenie tabeli
create_table_query = '''
CREATE TABLE IF NOT EXISTS products (
    ID INTEGER PRIMARY KEY,
    productID INTEGER,
    SKU TEXT,
    quantity INTEGER,
    price REAL
);
'''
cursor.execute(create_table_query)

# 4. Zatwierdzenie zmian
connection.commit()

# 5. Zamknięcie połączenia
connection.close()


connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Wykonaj zapytanie SELECT, aby pobrać wszystkie rekordy z tabeli products
cursor.execute("SELECT * FROM products")
rows = cursor.fetchall()

# Wyświetl wyniki
for row in rows:
    print("ID:", row[0])
    print("ProductID:", row[1])
    print("SKU:", row[2])
    print("Quantity:", row[3])
    print("Price:", row[4])
    print()

connection.close()