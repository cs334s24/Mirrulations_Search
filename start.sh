#!/bin/bash

# Define the database file
DB_FILE="my_database.db"

# Define the SQL command to create a table
SQL_CMD="CREATE TABLE IF NOT EXISTS my_table (id INTEGER PRIMARY KEY, name TEXT NOT NULL);"

# Define the list of names
NAMES=("Name1" "Name2" "Name3" "Name4")

# Check if the database file already exists
if [ -f "$DB_FILE" ]; then
    echo "Database file already exists."
else
    # Initialize the SQLite database and create the table
    sqlite3 $DB_FILE "$SQL_CMD"
    echo "Database initialized and table created."

    # Insert names into the table
    for name in "${NAMES[@]}"; do
        sqlite3 $DB_FILE "INSERT INTO my_table (name) VALUES ('$name');"
    done

    echo "Names inserted into the table."
fi