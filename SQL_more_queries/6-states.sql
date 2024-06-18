-- creates the database hbtn_0d_usa and the table states 
-- (in the database hbtn_0d_usa) on your MySQL server.

CREATE database IF not exists hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF not exists states(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);