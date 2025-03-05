import sqlite3

conn = sqlite3.connect("hw.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Roster (
        Name TEXT,
        Species TEXT,
        Age INTEGER
    )
""")

cursor.executemany("""
    INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)
""", [
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29)
])

cursor.execute("""
    UPDATE Roster
    SET Name = 'Ezri Dax'
    WHERE Name = 'Jadzia Dax'
""")

cursor.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'")
bajorans = cursor.fetchall()

print("Bajorans in the Roster:")
for name, age in bajorans:
    print(f"Name: {name}, Age: {age}")

conn.commit()
conn.close()
