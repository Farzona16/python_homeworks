import sqlite3
#datas
records=[
    ("To Kill a Mockingbird","Harper Lee",1960,"Fiction"),  
    ("1984 ","George Orwell ",1949, "Dystopian"),
    ("The Great Gatsby","F. Scott Fitzgerald",1925, "Classic")
    ]
#create data
with sqlite3.connect("library.db") as data:
    cursor=data.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Books(
    Title TEXT NOT NULL,
    Author TEXT NOT NULL,
    Year_published INTEGER NOT NULL,
    Genre TEXT NOT NULL
    )
    """)
    #insert unique data
    for record in records:
        cursor.execute("""
        SELECT*FROM Books WHERE Title=? AND Author=? AND Year_published=? AND Genre=?
        """,record)
        if not cursor.fetchone():
            cursor.execute("""
            INSERT INTO Books (Title,Author,Year_published,Genre)
            VALUES(?,?,?,?)
            """,record)
    #Update data
    cursor.execute("""
    UPDATE Books
    SET Year_published=1950
    WHERE Year_published=1949 and Title="1984";
    """)
    #retrieve query
    cursor.execute("""
    SELECT Title, Author
    FROM Books
    WHERE Genre='Dystopian';
    """)

    #delete data
    cursor.execute("""
    DELETE FROM Books
    WHERE Year_published<1950;
    """)
    # #bonus task
    # cursor.execute("""
    # ALTER TABLE Books
    # ADD Rating REAL DEFAULT 0 ;
    # """) 
    
    # Ratings=[
    #         ("To Kill a Mockingbird", 4.8 ),
    #         ("1984 ",4.7  ),
    #         ("The Great Gatsby",  4.5)
    #         ] 
   
    # for Title,Rating in Ratings:
    #     cursor.execute("""
    #     UPDATE Books
    #     SET Rating=?
    #     WHERE Title=?;
    #     """,(Rating,Title))
    # data.commit()

    #sort by published year
    cursor.execute("""
    SELECT Year_published
    FROM Books
    ORDER BY Year_published ASC;
    """)