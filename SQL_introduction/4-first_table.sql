-- creates a table called first_table in the current database in MySQL server.

CREATE table if not exists first_table(
    id INT NOT NULL,
    name VARCHAR (256) NOT NULL,
    PRIMARY KEY (id)
);