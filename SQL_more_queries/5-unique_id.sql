-- creates the table unique_id on your MySQL server.

CREATE TABLE IF not exists unique_id(
    id INT NOT NULL UNIQUE DEFAULT 1,
    name VARCHAR (256)
);