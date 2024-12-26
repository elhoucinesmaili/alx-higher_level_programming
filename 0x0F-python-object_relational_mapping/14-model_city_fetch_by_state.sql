-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0e_14_usa;
USE hbtn_0e_14_usa;

-- Create the 'states' table
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

-- Populate the 'states' table with initial data
INSERT INTO states (name)
VALUES 
    ('California'), 
    ('Arizona'), 
    ('Texas'), 
    ('New York'), 
    ('Nevada');

-- Create the 'cities' table
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);

-- Populate the 'cities' table with initial data
INSERT INTO cities (state_id, name)
VALUES 
    (1, 'San Francisco'), (1, 'San Jose'), (1, 'Los Angeles'), 
    (1, 'Fremont'), (1, 'Livermore'),
    (2, 'Page'), (2, 'Phoenix'),
    (3, 'Dallas'), (3, 'Houston'), (3, 'Austin'),
    (4, 'New York'),
    (5, 'Las Vegas'), (5, 'Reno'), (5, 'Henderson'), (5, 'Carson City');
