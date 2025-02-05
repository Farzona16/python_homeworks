import sqlite3
# datas
records=[
        ('Benjamin Sisko', 'Human', 40),
        ('Jadzia Dax', "Trill", 300),
        (" Kira Nerys ", "Bajoran", 29)
    ]

with sqlite3.connect("roster.db") as data:
    cursor=data.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Roster(
        Name TEXT NOT NULL,
        Species TEXT NOT NULL,
        Age INTEGER NOT NULL
    )
    """)
    #data and table created 
    
    for record in records:
        cursor.execute("""
        SELECT*FROM Roster WHERE Name=? AND Species=? AND Age=?
        """,record) #checking for unique data
        if not cursor.fetchone():
            cursor.execute("""
            INSERT INTO Roster (Name,Species,Age)
            VALUES (?,?,?)
            """,record)
    
    #UPDATE  DATA
    cursor.execute("""
    UPDATE Roster
    SET Name="Ezri Dax"
    WHERE Age=300;
    """)
    #retrieve query
    cursor.execute("""
    SELECT Name, Age
    FROM Roster
    WHERE Species="Bajoran";
    """)

    #Delete data

    cursor.execute("""
    DELETE FROM Roster
    WHERE Age>100;
    """)

    #bonus task
    # cursor.execute("""
    # ALTER TABLE Roster
    # ADD Rank TEXT DEFAULT 'Unknown';
    # """)
    # ranks = [
    #     ("Benjamin Sisko", "Captain"),
    #     ("Jadzia Dax", "Lieutenant"),
    #     ("Kira Nerys", "Major")
    # ]
    # for Name,rank in ranks:
    #     cursor.execute("""
    #     UPDATE Roster
    #     SET Rank=?
    #     WHERE Name=?;
    #     """,(rank,Name))
    #sort by age
    cursor.execute("""
    SELECT Age
    FROM Roster
    ORDER BY Age DESC;
    """)
    data.commit()