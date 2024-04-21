from fastapi import FastAPI, HTTPException
import mysql.connector

# MySQL connection parameters
MYSQL_HOST = "192.168.30.44"
MYSQL_PORT = 3999
MYSQL_USER = "root"
MYSQL_PASSWORD = "root"
MYSQL_DATABASE = "hello"
TABLE_NAME = "items"

# Create FastAPI instance
app = FastAPI()

# Function to connect to MySQL
def connect_to_mysql():
    return mysql.connector.connect(
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )

# Function to create table if not exists
def create_table():
    connection = connect_to_mysql()
    cursor = connection.cursor()
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {TABLE_NAME} (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, description TEXT)")
    connection.commit()
    connection.close()

# Function to insert dummy data into table
def insert_dummy_data():
    connection = connect_to_mysql()
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO {TABLE_NAME} (name, description) VALUES ('Item 1', 'Description for Item 1'), ('Item 2', 'Description for Item 2'), ('Item 3', 'Description for Item 3')")
    connection.commit()
    connection.close()

# Endpoint to get all items
@app.get("/items/")
def get_items():
    connection = connect_to_mysql()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {TABLE_NAME}")
    items = cursor.fetchall()
    connection.close()
    return items

# Run create table function
create_table()

# Run insert dummy data function
insert_dummy_data()

# Run FastAPI application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
