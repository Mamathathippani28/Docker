#  Database & Python ETL – Reproducible Dockerized Setup

##  Overview

This project demonstrates a **Python-based ETL pipeline** that extracts data from a CSV file (`customers-100.csv`), transforms it using `pandas`, and loads it into a **MySQL database** inside a reproducible **Docker Compose environment**.

The entire setup — including database provisioning, environment variables, and Python dependencies — is containerized for seamless deployment and testing.

---

##  Architecture

```
+-------------------+        +--------------------+         +--------------------+
|   CSV Source      |  -->   |   Python ETL       |  -->    |   MySQL Database   |
| customers-100.csv |        |  (Ass1.py + pandas)|         |  customers table   |
+-------------------+        +--------------------+         +--------------------+
```

**Key Components**
- **Python 3.10** – ETL logic and data transformation
- **Pandas** – data cleaning, type conversion, and validation
- **MySQL Connector** – database interaction
- **Docker & Docker Compose** – reproducible deployment and environment isolation

---

##  Project Structure

```
project/
│
├── Ass1.py
├── Dockerfile
├── docker-compose.yaml
├── requirements.txt
├── customers-100.csv
└── README.md
```

---

## Database Schema

**Table Name:** `Customers`

| Column Name       | Data Type   | Description              |
|-------------------|-------------|---------------------------|
| Index             | INT         | Record index             |
| CustomerId        | VARCHAR(64) | Unique customer ID        |
| FirstName         | VARCHAR(100)| Customer first name       |
| LastName          | VARCHAR(100)| Customer last name        |
| Company           | VARCHAR(200)| Company name              |
| City              | VARCHAR(100)| Customer city             |
| Country           | VARCHAR(100)| Customer country          |
| Phone1            | VARCHAR(50) | Primary phone number      |
| Phone2            | VARCHAR(50) | Secondary phone number    |
| Email             | VARCHAR(200)| Email address             |
| SubscriptionDate  | DATE        | Date of subscription      |
| Website           | VARCHAR(255)| Website URL               |

---

##  Environment Variables

The ETL script reads connection details from environment variables to ensure portability:

| Variable Name | Default Value | Description |
|----------------|----------------|-------------|
| `DB_HOST` | mysql | MySQL container hostname |
| `DB_USER` | root | MySQL username |
| `DB_PASSWORD` | password | MySQL password |
| `DB_NAME` | ETL | Target database name |

---

## Docker Setup

### 1️ Build and Run Containers
Run the following from the project root:
```bash
docker compose up --build
```

This will:
- Build the Python ETL image using the provided **Dockerfile**
- Start a **MySQL container** with initialized credentials
- Run the ETL process inside the Python container, which loads the CSV data into MySQL

### 2️ Verify Database Connection
After containers start successfully:
```bash
docker exec -it mysql bash
mysql -u root -p
```
Then execute:
```sql
USE ETL;
SELECT COUNT(*) FROM Customers;
```
You should see the number of rows matching your CSV record count.

---

##  Testing and Validation

| Step | Validation |
|------|-------------|
| CSV Read | Confirm all 100 records are loaded without missing data |
| Date Format | Ensure `SubscriptionDate` is correctly converted to `DATE` type |
| DB Creation | Verify `Customers` table is created with correct schema |
| Data Load | Run a `SELECT * FROM Customers LIMIT 5;` query to confirm records |

---

## Cleanup
To stop and remove all containers, networks, and volumes:
```bash
docker compose down -v
```

---

##  Reproducibility Notes
- Environment setup is **self-contained** within Docker.
- Python dependencies are declared in `requirements.txt`:
  ```
  pandas
  mysql-connector-python
  ```
- The pipeline logic in `Ass1.py` automatically handles:
  - Missing fields (`fillna("")`)
  - Invalid dates (`errors="coerce"`)
  - Table creation if it doesn’t exist

---

##  How It Works

1. **Extract:**  
   Reads `customers-100.csv` via `pandas.read_csv()`

2. **Transform:**  
   - Cleans missing data  
   - Converts subscription dates into MySQL-compatible format  
   - Ensures consistent column names

3. **Load:**  
   - Connects to MySQL  
   - Creates `Customers` table if not exists  
   - Inserts rows using parameterized queries for safety  
   - Commits and closes connection gracefully

---

## Expected Output
- Successful ETL run message in container logs.
- Data visible in MySQL table `Customers`.
- Matching record count between CSV and database.

---

##  References
- ETL_Docker_TechnicalDocument.pdf
- Ass1.py Source Code
- Docker Compose File
- Dockerfile
- requirements.txt

  ---
**Author:** Mamatha Thippani  
**Git:** [GitHub](https://github.com/Mamathathippani28/Docker/tree/main/ETL)
---
