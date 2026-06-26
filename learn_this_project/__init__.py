# simple_demo.py

from sqlalchemy import create_engine, text

# Concept 1: SQLite in-memory database
# This database exists only while this script is running.
engine = create_engine("sqlite:///:memory:")

# Concept 2: engine.begin()
# Use begin() when changing data.
# It automatically commits if successful, or rolls back if an error happens.
with engine.begin() as conn:
    conn.execute(text("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER
        )
    """))

    conn.execute(text("""
        INSERT INTO users (name, age)
        VALUES ('Alice', 25), ('Bob', 30)
    """))

# Concept 3: engine.connect()
# Use connect() when only reading data.
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM users"))
    print("Initial users:")
    for row in result:
        print(row)

# Concept 4: UPDATE with WHERE
# WHERE controls which rows are changed.
with engine.begin() as conn:
    conn.execute(text("""
        UPDATE users
        SET age = 26
        WHERE name = 'Alice'
    """))

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM users"))
    print("\nAfter updating only Alice:")
    for row in result:
        print(row)

# Concept 5: UPDATE without WHERE
# This changes every row.
with engine.begin() as conn:
    conn.execute(text("""
        UPDATE users
        SET age = age + 1
    """))

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM users"))
    print("\nAfter UPDATE without WHERE:")
    for row in result:
        print(row)