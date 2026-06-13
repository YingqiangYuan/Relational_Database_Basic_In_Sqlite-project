# Examples — Background and How to Read This Folder

This folder is the hands-on portion of the course. Before you open the first script, please read this page once. It explains **what these scripts are**, **why we organize them this way**, and **what each numbered series is trying to teach you**. A few minutes spent here will save a lot of confusion later.

## What this course is about

This is an introductory course on **relational databases**, using **SQLite** as the concrete database engine. The goal is modest and very deliberate: by the end you should *feel* what a relational database is — tables, rows, columns, primary keys, simple queries — without drowning in the surrounding ecosystem.

We will not cover server administration, indexing strategy, query planners, replication, or production deployment. Those are real and important topics, but they belong to a later course. Here we stay close to the basics so the core ideas stick.

## Why Python scripts, and not a database GUI?

A natural first instinct when learning SQL is to open a database tool (DBeaver, TablePlus, the `sqlite3` shell, etc.), paste in a `CREATE TABLE`, then paste an `INSERT`, then paste a `SELECT`, and read the results in the GUI. That works for a single statement, but it falls apart fast as a teaching format:

- **It is hard to reproduce.** A tutorial usually says "do step 1, then step 2, then step 3." If you forget which step you are on, or run step 3 before step 2, the database is now in a state that does not match the tutorial. From here on every output looks "wrong" and you cannot tell why.
- **It is hard to start over.** To get back to a clean slate you have to manually drop tables, re-create them, re-insert seed data — and now you are debugging the cleanup instead of learning SQL.
- **It hides the order.** Clicking around a GUI does not enforce a sequence. A script does: line 1 runs before line 2, full stop.

Putting every lesson into a small Python script fixes all three:

- The **steps are frozen in the file** in the exact order the lesson intends.
- Every script begins with a **fresh in-memory database** (`sqlite:///:memory:`). The database exists only while the script runs, and disappears when the script exits. The next run gets a brand-new database — there is no stale state to worry about.
- You can **re-run the same script as many times as you want** and the output will be identical. That is the property you need when you are trying to learn what something does.

So the Python file is not the lesson — the **SQL inside it** is the lesson. Python is just a precise, reproducible way to play that SQL back to you in order.

## Why SQLite?

Most "real" relational databases (PostgreSQL, MySQL, SQL Server, Oracle, ...) require you to run a separate **server process**, configure a user, open a network port, manage credentials, and so on. That is a lot of ceremony for someone whose goal is "I want to understand what a SELECT does."

SQLite skips all of that. It is:

- **Just a library.** No server, no port, no daemon.
- **Just a file** (or, as we use it here, just a block of RAM). The whole database lives in a single `.db` file you can delete with one command.
- **Standard SQL** for everything we will teach. The `CREATE TABLE`, `INSERT`, `SELECT`, `UPDATE`, `DELETE` you learn here transfer almost unchanged to Postgres or MySQL later.
- **Already on your machine.** Python ships with it. Nothing to install.

That makes SQLite the perfect classroom database. It is also widely used in production for embedded use cases (mobile apps, desktop apps, small web apps), so the time you spend with it is not wasted.

## Why SQLAlchemy shows up in a "learn SQL" course?

You will notice that none of the scripts call SQLite directly. They all go through a library called [SQLAlchemy](https://www.sqlalchemy.org/). A short explanation of why:

- In the Python world, if you are going to talk to a relational database in any serious way, **SQLAlchemy is the de facto standard**. It is the single most mature, most widely used, most capable database toolkit in the Python ecosystem.
- It is also a *layered* library. The bottom layer lets you send raw SQL strings. A higher layer lets you build SQL out of Python expressions. A top layer (the ORM) lets you treat rows as Python objects. We will use the bottom two layers and ignore the top one.
- It handles a lot of unglamorous-but-important details for us: connection management, transactions, safe value binding, dialect differences between databases. Even when we write raw SQL, going through SQLAlchemy keeps the code cleaner and safer.

For this course, all you need to know is: **SQLAlchemy is the door we walk through to get to the database. It exists, it is powerful, and you do not need to master it right now.**

## The two script series: `s1x_*` and `s2x_*`

The numbered example scripts come in two parallel series. They cover exactly the same SQL topics (`CREATE`, `INSERT`, `SELECT`, `UPDATE`, `DELETE`) but they show two different *styles* of getting that SQL into the database. You should read s1x first, then s2x, in order.

### Series 1 — `s11_*` to `s15_*`: Raw SQL via `text("...")`

These scripts let you write SQL the way you would write it into a database shell — as plain strings:

```python
conn.execute(text("SELECT * FROM users WHERE age > :min_age"),
             {"min_age": 25})
```

This series exists because **before you can appreciate any abstraction over SQL, you need to see SQL itself**. If we jumped straight to the "build the query out of Python objects" style, you would have a hard time telling which parts of the code map to which parts of the SQL, and the abstraction would feel like magic.

Two things worth noticing as you read these scripts:

1. The string passed to `text("...")` *is* the SQL — there is no translation layer on top of it. Copy it into the `sqlite3` shell and it would run unchanged.
2. The colon-prefixed `:name` placeholders are **bound parameters**. Never build SQL by concatenating or f-string-formatting user input; that is how you get SQL injection. The `:name` form lets the database driver handle the value safely.

### Series 2 — `s21_*` to `s25_*`: SQLAlchemy Core Expression

These scripts cover the same SQL topics again, but the SQL is built out of **Python expressions** instead of being typed as a string:

```python
stmt = select(users_table).where(users_table.c.age > 25)
conn.execute(stmt)
```

That looks fancier than the raw-SQL version, and for *one* query it honestly is not a win — you could argue the raw string is clearer. So why does this style exist, and why does practically every serious Python application end up writing SQL this way?

#### Why hand-written SQL is rare in real applications

Imagine your application has a hundred queries against the same `users` table. Each one differs by tiny variations: this one filters by age, that one filters by name, this other one filters by both age **and** city, and adds an `ORDER BY` only when the user clicked a column header in the UI. A few problems show up immediately:

1. **Combinatorial explosion.** If you write each variation as a raw string, you end up with dozens of nearly-identical SQL strings scattered through the codebase. Change the table name and you have to chase every one of them.
2. **Conditional pieces are awkward.** "Add a `WHERE city = :city` *only if* the user selected a city" is painful with string concatenation, and it is exactly the situation where people get tempted to do `f"... WHERE city = '{city}'"` — which is a classic SQL-injection bug.
3. **No help from the language.** A plain string is opaque to your editor, your type checker, and your linter. Typos in column names only surface at runtime, when the query fails against the database.

The Core Expression style addresses these problems by treating a query as a **value** you can build up piece by piece in normal Python code:

- Need a filter only sometimes? Wrap it in an `if`: `if city: stmt = stmt.where(users_table.c.city == city)`.
- Need to reuse a piece across many queries? Assign it to a variable and reuse the variable.
- Need parameter safety? You get it for free — `users_table.c.age > 25` always becomes a bound parameter under the hood, never a string concatenation.
- Misspell a column name? You reference `users_table.c.aeg` and Python raises an error immediately, instead of MySQL complaining at 3am.

That is why production codebases very rarely write SQL as raw strings: they need to *compose* queries, not just *run* them.

#### What does "Core" mean, and why does it look a little abstract?

The Python objects we use in this series — `Table`, `Column`, `select`, `insert`, `update`, `delete`, `where`, `values`, ... — are SQLAlchemy's **Core Expression Language**. They are a small, SQL-shaped vocabulary in Python. Each call returns a query *object*; nothing is sent to the database until you call `conn.execute(stmt)`.

This is why the s2x code looks slightly more abstract than the s1x code. You are not writing SQL directly; you are writing *a description* of SQL. SQLAlchemy compiles that description into the right SQL for whichever database you are pointed at. The payoff is composability; the cost is one extra layer of indirection that takes a little getting used to.

## A quick word on the ORM (and why this course does not use it)

You may have heard the term **ORM** ("Object-Relational Mapper"). SQLAlchemy has one, and it is excellent. The ORM lets you treat database rows as full-blown Python objects: `user.name`, `user.email`, `session.add(user)`, and so on.

The ORM solves a problem that is *related* to what Core Expression solves — it is another way to avoid scattering raw SQL strings through your codebase and to make data access more structured and reusable — but it adds extra concepts (mapped classes, sessions, identity map, lazy loading) that we deliberately do not need here.

This course is your first exposure to relational databases. The goal is to *feel* tables and SQL, not to learn an object framework on top of them. So we will not use the ORM. Just know it exists; it is the natural next step after you are comfortable with raw SQL and Core Expression.

## How to run the examples

From the project root:

```bash
mise run inst                       # one-time: install dependencies
uv run python examples/s11_create_table.py
uv run python examples/s12_insert_data.py
# ...and so on through s15, then s21..s25
```

Each script is **fully self-contained**. It creates a fresh in-memory database, recreates the table, re-inserts whatever seed data it needs, and then demonstrates one topic. You can run any single script on its own and get a complete, repeatable result. You can also run them out of order with no risk of breaking anything — there is nothing persistent to break.

## Suggested reading order

1. This README (you are here).
2. `s11_create_table.py` → `s12_insert_data.py` → `s13_select_data.py` → `s14_update_data.py` → `s15_delete_data.py` (the *raw SQL* tour of the basics).
3. `s21_create_table.py` → `s22_insert_data.py` → `s23_select_data.py` → `s24_update_data.py` → `s25_delete_data.py` (the *Core Expression* tour of the same basics — now you will see what the abstraction buys you).
4. `utils.py` if you are curious how the pretty-printed tables are produced. It is small.

That is enough to give you a real, working feel for relational databases. Once you are comfortable here, you are ready to graduate to a server-based database like PostgreSQL and, later, to the ORM.
