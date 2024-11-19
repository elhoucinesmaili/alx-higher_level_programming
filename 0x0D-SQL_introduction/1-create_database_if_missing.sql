-- Creates the database hbtn_0c_0 if it does not exist
CREATE DATABASE hbtn_0c_0 WHERE NOT EXISTS (
    SELECT SCHEMA_NAME 
    FROM INFORMATION_SCHEMA.SCHEMATA 
    WHERE SCHEMA_NAME = 'hbtn_0c_0'
);
