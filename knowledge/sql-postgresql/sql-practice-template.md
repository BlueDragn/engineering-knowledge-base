
# SQL Practice Template

This guide provides a quick reference for common PostgreSQL operations.

## 1\. Create Database

To create a new database in PostgreSQL, use the `CREATE DATABASE` command.

``` sql
CREATE DATABASE database_name;

```

**Connect to the database:**

``` bash
\c database_name

```

## 2\. Create Table

Use `CREATE TABLE` to define your table structure, including column types and constraints.

``` sql
CREATE TABLE table_name (
    id SERIAL PRIMARY KEY,
    column1 VARCHAR(100) NOT NULL,
    column2 INT,
    column3 DATE
);

```

## 3\. Insert Data

Populate your tables using the `INSERT INTO` statement.

**Single row:**

``` sql
INSERT INTO table_name (column1, column2)
VALUES ('Value', 100);

```

**Multiple rows:**

``` sql
INSERT INTO table_name (column1, column2)
VALUES
('Value1', 100),
('Value2', 200),
('Value3', 300);

```

## 4\. View Data

Retrieve data using the `SELECT` statement.

**All columns:**

``` sql
SELECT * FROM table_name;

```

**Specific columns:**

``` sql
SELECT column1, column2 FROM table_name;

```

## 5\. Filter Data

Use the `WHERE` clause to filter result sets.

``` sql
SELECT * FROM table_name WHERE condition;

```

*Examples:*

  * `WHERE age > 25;`
  * `WHERE salary >= 50000;`
  * `WHERE city = 'Delhi';`

## 6\. Multiple Conditions

Combine conditions using `AND` or `OR` operators.

``` sql
-- Both must be true
WHERE condition1 AND condition2;

-- Either can be true
WHERE condition1 OR condition2;

```

## 7\. Sort Data

Control the order of results using `ORDER BY`.

**Ascending:**

``` sql
ORDER BY column_name;

```

**Descending:**

``` sql
ORDER BY column_name DESC;

```

## 8\. Aggregate Functions

Perform calculations on a set of values.

  * `COUNT(*)`: Returns the number of rows.
  * `AVG(column_name)`: Returns the average value.
  * `MAX(column_name)`: Returns the maximum value.
  * `MIN(column_name)`: Returns the minimum value.
  * `SUM(column_name)`: Returns the total sum.

## 9\. GROUP BY

Aggregate data based on common values in a column.

``` sql
SELECT column_name, COUNT(*)
FROM table_name
GROUP BY column_name;

```

## 10\. Update Data

Modify existing records with the `UPDATE` statement.

``` sql
UPDATE table_name
SET column_name = value
WHERE condition;

```

## 11\. Delete Data

Remove records from a table.

``` sql
DELETE FROM table_name
WHERE condition;

```

## 12\. Alter Table

Modify the table schema after creation.

**Add Column:**

``` sql
ALTER TABLE table_name ADD COLUMN column_name data_type;
-- Example:
ALTER TABLE employees ADD COLUMN department_id INT;

```

**Remove Column:**

``` sql
ALTER TABLE table_name DROP COLUMN column_name;

```

## 13\. Joins

Combine rows from two or more tables based on a related column.

  * **INNER JOIN**: Returns records that have matching values in both tables.
  * **LEFT JOIN**: Returns all records from the left table, and matched records from the right table.
  * **RIGHT JOIN**: Returns all records from the right table, and matched records from the left table.
  * **FULL OUTER JOIN**: Returns all records when there is a match in either left or right table.

*Syntax example:*

``` sql
SELECT table1.column, table2.column
FROM table1
INNER JOIN table2 ON table1.foreign_key = table2.primary_key;

```

## 14\. Useful PostgreSQL Commands

Common command-line interface (CLI) shortcuts:

| Command         | Description              |
| :-------------- | :----------------------- |
| `\l`            | List all databases       |
| `\c db_name`    | Connect to a database    |
| `\dt`           | List all tables          |
| `\d table_name` | Describe table structure |
| `\q`            | Quit PostgreSQL          |

-----
