# README – Simple SQLAlchemy + SQLite Demo

## Overview

This project is a minimal demonstration of relational database programming using **Python**, **SQLite**, and **SQLAlchemy Core**. Rather than building a complete application, every line of code is written to illustrate a specific database or software engineering concept. The script intentionally remains small so that learners can focus on understanding **how** each technology works and **why** it is used.

The code also serves as a foundation for many technical interview discussions. Interviewers often use simple CRUD applications like this to evaluate a candidate's understanding of transactions, SQL safety, database design, Python execution, and engineering tradeoffs.

---

## How the Concepts Are Applied

### SQLite In-Memory Database

The first line of the program creates the database using:

```python
engine = create_engine("sqlite:///:memory:")
```

This demonstrates the concept of an **in-memory SQLite database**. Instead of storing data on disk, the database exists only while the Python process is running. Every execution therefore starts from a completely clean state.

This design allows the script to recreate the schema and seed data every time it runs, eliminating stale state, duplicate records, and cleanup work. It also demonstrates why rerunning the script is sufficient to recover from accidental updates—once the program exits, the database disappears.

---

### SQLAlchemy Engine

The `Engine` is the entry point to the database.

```python
engine = create_engine(...)
```

Instead of communicating directly with SQLite, every database operation goes through the SQLAlchemy Engine. The Engine manages database connections and provides a consistent interface that can later be redirected to PostgreSQL or another relational database with minimal code changes. This demonstrates SQLAlchemy's role as a database toolkit rather than simply a SQL execution library.

---

### Transactions with `engine.begin()`

All operations that modify the database use:

```python
with engine.begin() as conn:
```

This demonstrates **transaction management**.

Creating tables, inserting data, and updating rows all occur inside a transaction. If an exception occurs anywhere inside the block, SQLAlchemy automatically performs a rollback so that no partial changes remain. This illustrates the ACID property of **Atomicity**, where either all operations succeed or none of them are committed.

The project intentionally separates write operations into transactional blocks to reinforce that database modifications should always be protected by transactions.

---

### Reading Data with `engine.connect()`

Queries use

```python
with engine.connect() as conn:
```

instead of `engine.begin()`.

This illustrates that read-only operations generally require only a database connection rather than a full write transaction. Separating these two APIs teaches students that reading and modifying data have different responsibilities, even though both ultimately communicate with the same database.

---

### Raw SQL Through `text()`

Every SQL statement is written explicitly:

```python
conn.execute(text("SELECT * FROM users"))
```

This is intentional.

Students see the exact SQL sent to the database instead of immediately learning a higher-level abstraction. This makes it easier to understand how relational databases work before introducing SQLAlchemy Core expressions or the ORM.

---

### CRUD Operations

The script demonstrates the four fundamental database operations:

* **CREATE** – creating the `users` table.
* **INSERT** – adding new users.
* **SELECT** – retrieving data.
* **UPDATE** – modifying existing records.

Each operation is isolated so learners can clearly observe how the database changes after every step.

---

### Safe vs Unsafe UPDATE

One of the most important demonstrations is the difference between

```sql
UPDATE users
SET age = 26
WHERE name = 'Alice'
```

and

```sql
UPDATE users
SET age = age + 1
```

The first updates only one row.

The second updates every row because no `WHERE` clause limits the operation.

This illustrates one of the most common SQL mistakes. It also motivates the professional habit of first running the intended condition as a `SELECT` before executing the `UPDATE`.

---

### SQLite Auto-Increment Behavior

The table is created using

```sql
id INTEGER PRIMARY KEY
```

In SQLite, this column automatically becomes the table's internal row identifier (`rowid`). New IDs are assigned automatically whenever rows are inserted.

This provides a natural introduction to primary keys while also leading into discussions about how PostgreSQL uses `IDENTITY` columns or sequences instead of SQLite's `rowid` mechanism.

---

## Engineering Decisions Demonstrated

Although the program is intentionally small, it demonstrates several software engineering decisions:

* Using **SQLite** to minimize setup complexity and focus on SQL concepts rather than database administration.
* Using **SQLAlchemy Core** instead of the ORM so students understand relational databases before introducing object-relational mapping.
* Using an **in-memory database** to guarantee reproducible execution and eliminate environment-related issues.
* Separating **transactional** and **read-only** operations using `engine.begin()` and `engine.connect()`.
* Keeping SQL visible through **raw SQL** so learners understand exactly what the database executes.
* Demonstrating both **correct** and **incorrect** update patterns to emphasize SQL safety.

---

## Connection to Technical Interviews

Every design choice in this script can naturally expand into larger engineering discussions.

A single line such as

```python
engine = create_engine("sqlite:///:memory:")
```

can lead to questions about SQLite versus PostgreSQL, reproducibility, persistence, concurrency, and database lifecycle.

Similarly,

```python
with engine.begin():
```

opens discussions about transactions, rollback, ACID guarantees, and production database safety.

Even the simple `UPDATE` statements introduce conversations about SQL safety, recovery strategies, large-scale database migrations, batching, monitoring, and operational best practices.

The script therefore functions not only as a CRUD demonstration but also as a compact example containing many of the core concepts that software engineers are expected to understand during technical interviews.
