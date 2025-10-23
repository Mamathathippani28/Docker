import os
import pandas as pd
import mysql.connector

connection = mysql.connector.connect(
    host=os.getenv("DB_HOST", "mysql"),
    user=os.getenv("DB_USER", "root"),                 
    password=os.getenv("DB_PASSWORD", "password"),
    database=os.getenv("DB_NAME", "ETL")               
)

cursor = connection.cursor()

#Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS `Customers` (
        `Index` INT,
        `CustomerId` VARCHAR(64),
        `FirstName` VARCHAR(100),
        `LastName` VARCHAR(100),
        `Company` VARCHAR(200),
        `City` VARCHAR(100),
        `Country` VARCHAR(100),
        `Phone1` VARCHAR(50),
        `Phone2` VARCHAR(50),
        `Email` VARCHAR(200),
        `SubscriptionDate` DATE,
        `Website` VARCHAR(255)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
""")

# Read CSV as-is (your headers with spaces are fine)
df = pd.read_csv("customers-100.csv", dtype=str, keep_default_na=False).fillna("")

#  parse date column to DATE
if "Subscription Date" in df.columns:
    df["Subscription Date"] = pd.to_datetime(
        df["Subscription Date"], errors="coerce"
    ).dt.date

# Insert data 
insert_sql = """
    INSERT INTO `Customers`
    (`Index`,`CustomerId`,`FirstName`,`LastName`,`Company`,`City`,`Country`,
     `Phone1`,`Phone2`,`Email`,`SubscriptionDate`,`Website`)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

for _, row in df.iterrows():
    cursor.execute(
        insert_sql,
        (
            row.get('Index'),
            row.get('Customer Id'),
            row.get('First Name'),
            row.get('Last Name'),
            row.get('Company'),
            row.get('City'),
            row.get('Country'),
            row.get('Phone 1'),
            row.get('Phone 2'),
            row.get('Email'),
            row.get('Subscription Date'),
            row.get('Website'),
        )
    )

connection.commit()
connection.close()
