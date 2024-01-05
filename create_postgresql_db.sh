#!/bin/bash

# Define variables
DB_NAME="notesdb"
DB_USER="om"
DB_PASSWORD="1234"

# Access PostgreSQL prompt
sudo -u postgres psql << EOF

-- Create Database
CREATE DATABASE $DB_NAME;

-- Create User
CREATE USER $DB_USER;

-- Set User Password
ALTER USER $DB_USER WITH ENCRYPTED PASSWORD '$DB_PASSWORD';

-- Grant Privileges
GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;

-- Exit
\q

EOF

echo "Database, user, and password created successfully."
