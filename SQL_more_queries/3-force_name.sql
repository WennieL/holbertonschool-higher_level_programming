-- creates the table force_name on your MySQL server.

CREATE TABLE IF not exists force_name(
    id INT NOT NULL,
    name VARCHAR (256) NOT NULL,
    PRIMARY KEY (id)
);