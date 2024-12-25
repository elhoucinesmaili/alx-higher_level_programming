-- Create database hbtn_0e_14_usa, tables states and cities + some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_14_usa;
USE hbtn_0e_14_usa;

-- Create the 'states' table
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(128) NOT NULL,
    PRIMARY KEY (id)
);

-- Insert sample state data
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

-- Create the 'cities' table, with a foreign key linking to 'states' table
CREATE TABLE IF NOT EXISTS cities ( 
    id INT NOT NULL AUTO_INCREMENT, 
    state_id INT NOT NULL,
    name VARCHAR(128) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);

-- Insert sample city data, with each city belonging to a state
INSERT INTO cities (state_id, name) VALUES 
(1, "San Francisco"), 
(1, "San Jose"), 
(1, "Los Angeles"), 
(1, "Fremont"), 
(1, "Livermore");

INSERT INTO cities (state_id, name) VALUES 
(2, "Page"), 
(2, "Phoenix");

INSERT INTO cities (state_id, name) VALUES 
(3, "Dallas"), 
(3, "Houston"), 
(3, "Austin");

INSERT INTO cities (state_id, name) VALUES 
(4, "New York");

INSERT INTO cities (state_id, name) VALUES 
(5, "Las Vegas"), 
(5, "Reno"), 
(5, "Henderson"), 
(5, "Carson City");
