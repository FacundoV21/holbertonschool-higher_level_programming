-- Creates table if does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE if not exists states(id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(256) NOT NULL);
