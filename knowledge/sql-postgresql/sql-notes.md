# SQL Fundamentals Notes

## What is SQL?

SQL (Structured Query Language) is used to:

- Store data
- Retrieve data
- Filter data
- Analyze data
- Modify data

SQL works with relational databases such as:

- PostgreSQL
- MySQL
- SQLite
- SQL Server

---

# Basic Database Concepts

## Database

A collection of related data.

Example:

```text
company
```

---

## Table

A structure that stores data in rows and columns.

Example:

| id | name | age |
|----|------|-----|
| 1 | Anshu | 28 |
| 2 | Ravi | 30 |

---

## Row

A single record in a table.

Example:

```text
1 | Anshu | 28
```

---

## Column

A specific attribute of data.

Example:

```text
id
name
age
```

---

# SELECT

Used to retrieve data from a table.

## Syntax

```sql
SELECT column_name
FROM table_name;
```

### Example

```sql
SELECT name
FROM customers;
```

---

## Select Multiple Columns

```sql
SELECT name, age
FROM customers;
```

---

## Select All Columns

```sql
SELECT *
FROM customers;
```

---

# WHERE

Used to filter rows.

## Syntax

```sql
SELECT *
FROM customers
WHERE age > 25;
```

---

### Examples

```sql
SELECT *
FROM customers
WHERE city = 'Delhi';
```

```sql
SELECT *
FROM customers
WHERE age >= 30;
```

---

# Comparison Operators

| Operator | Meaning |
|-----------|---------|
| = | Equal |
| != | Not Equal |
| > | Greater Than |
| < | Less Than |
| >= | Greater Than or Equal |
| <= | Less Than or Equal |

---

# AND

Both conditions must be true.

```sql
SELECT *
FROM customers
WHERE age > 25
AND city = 'Delhi';
```

---

# OR

At least one condition must be true.

```sql
SELECT *
FROM customers
WHERE city = 'Delhi'
OR city = 'Mumbai';
```

---

# ORDER BY

Used to sort results.

## Ascending (Default)

```sql
SELECT *
FROM customers
ORDER BY age;
```

---

## Descending

```sql
SELECT *
FROM customers
ORDER BY age DESC;
```

---

# Aggregate Functions

Aggregate functions perform calculations on multiple rows.

---

## COUNT()

Counts rows.

```sql
SELECT COUNT(*)
FROM customers;
```

---

## SUM()

Returns total value.

```sql
SELECT SUM(salary)
FROM employees;
```

---

## AVG()

Returns average value.

```sql
SELECT AVG(age)
FROM customers;
```

---

## MAX()

Returns largest value.

```sql
SELECT MAX(salary)
FROM employees;
```

---

## MIN()

Returns smallest value.

```sql
SELECT MIN(age)
FROM customers;
```

---

# GROUP BY

Groups rows based on a column.

## Example

```sql
SELECT city, COUNT(*)
FROM customers
GROUP BY city;
```

### Output

```text
Delhi    5
Mumbai   3
Patna    2
```

---

# HAVING

Filters grouped results.

## Example

```sql
SELECT city, COUNT(*)
FROM customers
GROUP BY city
HAVING COUNT(*) > 2;
```

### Difference

WHERE filters rows before grouping.

HAVING filters groups after grouping.

---

# Query Execution Order

Logical execution order:

```text
FROM
↓
WHERE
↓
GROUP BY
↓
HAVING
↓
SELECT
↓
ORDER BY
```

---

# Example Queries

## Customers Older Than 25

```sql
SELECT *
FROM customers
WHERE age > 25;
```

---

## Average Age Per City

```sql
SELECT city,
       AVG(age)
FROM customers
GROUP BY city;
```

---

## Cities With More Than 5 Customers

```sql
SELECT city,
       COUNT(*)
FROM customers
GROUP BY city
HAVING COUNT(*) > 5;
```

---

## Highest Salary

```sql
SELECT MAX(salary)
FROM employees;
```

---

# Key Takeaways

1. SELECT retrieves data.
2. WHERE filters rows.
3. ORDER BY sorts results.
4. AND/OR combine conditions.
5. Aggregate functions summarize data.
6. GROUP BY creates groups.
7. HAVING filters groups.
8. SQL is the foundation of PostgreSQL and database-driven applications.

---

# Next Learning

PostgreSQL Basics

Topics:

- Install PostgreSQL
- Create Database
- Create Table
- Insert Data
- Update Data
- Delete Data
- Query Real Data

Progression:

```text
SQL Fundamentals
        ↓
PostgreSQL
        ↓
FastAPI + PostgreSQL
        ↓
Production Backend Systems
```
