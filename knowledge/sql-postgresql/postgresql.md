
# PostgreSQL Basics - Notes

### PostgreSQL Hierarchy
```
PostgreSQL Server
|
└── company (database)
        |
        └── customers (table)
                |
                ├── id
                ├── name
                ├── age
                └── city


```


### Starting PostgreSQL

Open PostgreSQL CLI:  
`sudo -u postgres psql`  

Prompt:  
`postgres=#`

---

### List Databases  

`\l`

---

### Connect to Database  

`\c company`
Output:
You are now connected to database "company"
Prompt changes to:
`company=#`

---

### Create Table  

```
CREATE TABLE customers (
    id INT,
    name VARCHAR(100),
    age INT,
    city VARCHAR(100)
);

````

Output:
`CREATE TABLE`

-----

### List Tables

`\dt`
Example Output:

| Schema | Name      | Type  | Owner    |
| :----- | :-------- | :---- | :------- |
| public | customers | table | postgres |

-----

### Describe Table Structure

`\d customers`
Example Output:
| Column | Type |
| :--- | :--- |
| id | integer |
| name | varchar(100) |
| age | integer |
| city | varchar(100) |

-----

### Insert Data

``` sql
INSERT INTO customers
VALUES
(1, 'Anshu', 28, 'Patna'),
(2, 'Ravi', 25, 'Delhi'),
(3, 'Priya', 30, 'Patna'),
(4, 'Amit', 22, 'Delhi'),
(5, 'Neha', 27, 'Mumbai');

```

Output:
`INSERT 0 5`
Meaning:

  * INSERT = operation successful
  * 0 = OID (ignore for now)
  * 5 = rows inserted

-----

### Verify Data

``` sql
SELECT *
FROM customers;

```

Output:
| id | name | age | city |
| :--- | :--- | :--- | :--- |
| 1 | Anshu | 28 | Patna |
| 2 | Ravi | 25 | Delhi |
| 3 | Priya | 30 | Patna |
| 4 | Amit | 22 | Delhi |
| 5 | Neha | 27 | Mumbai |

-----

### SQL Mental Model

  * **FROM** → Choose table
  * **WHERE** → Choose rows
  * **SELECT** → Choose columns

Example:

``` sql
SELECT name
FROM customers
WHERE age > 25;

```

Read as:

  * From customers
  * Choose rows where age \> 25
  * Show only name

-----

## Basic Queries

### Show All Data

``` sql
SELECT *
FROM customers;

```

### Show Only Names

``` sql
SELECT name
FROM customers;

```

### Filter Rows

``` sql
SELECT *
FROM customers
WHERE age > 25;

```

### Sort Data

Ascending:

``` sql
SELECT *
FROM customers
ORDER BY age;

```

Descending:

``` sql
SELECT *
FROM customers
ORDER BY age DESC;

```

-----

## Aggregate Functions

### Count Rows

``` sql
SELECT COUNT(*)
FROM customers;

```

Output:
`5`

### Average Age

``` sql
SELECT AVG(age)
FROM customers;

```

Output:
`26.4000000000000000`
Rounded:

``` sql
SELECT ROUND(AVG(age), 2)
FROM customers;

```

Output:
`26.40`

### Maximum Age

``` sql
SELECT MAX(age)
FROM customers;

```

### Minimum Age

``` sql
SELECT MIN(age)
FROM customers;

```

### Sum

``` sql
SELECT SUM(age)
FROM customers;

```

-----

### Group By

Count customers by city:

``` sql
SELECT city, COUNT(*)
FROM customers
GROUP BY city;

```

Output:
| city | count |
| :--- | :--- |
| Delhi | 2 |
| Mumbai | 1 |
| Patna | 2 |

-----

## Useful psql Commands

### List Databases

`\l`

### Connect Database

`\c company`

### List Tables

`\dt`

### Describe Table

`\d customers`

### Exit PostgreSQL

`\q`

-----

## Error Handling

### Query Not Finished

Prompt:
`company-#`
Meaning:
PostgreSQL is waiting for the rest of the query.

### Cancel Current Query

`\r`
Output:
`Query buffer reset (cleared)`

-----

## Learning Progress

- [x] PostgreSQL Installation
- [x] Create Database
- [x] Connect Database
- [x] Create Table
- [x] Insert Data
- [x] Verify Data
- [x] Filter Data
- [x] Sort Data
- [x] Aggregate Functions
- [x] GROUP BY
- [x] psql Commands

**Next Topics:**
PRIMARY KEY, NOT NULL, UPDATE, DELETE, SERIAL, Constraints, Relationships

