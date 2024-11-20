-- Create the database hbtn_0d_usa if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Create the table cities if it does not already exist
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique, auto-generated, primary key
    state_id INT NOT NULL,             -- Foreign key referencing states(id)
    name VARCHAR(256) NOT NULL,        -- Name column cannot be null
    FOREIGN KEY (state_id) REFERENCES states(id) -- Foreign key constraint
        ON DELETE CASCADE               -- Ensures cities are deleted if the state is deleted
        ON UPDATE CASCADE               -- Updates cities if the state_id is updated
);
