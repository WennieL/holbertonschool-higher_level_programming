-- creates the table id_not_null on your MySQL server.

CREATE TABLE IF not exists id_not_null(
    id int NOT NULL DEFAULT 1,
    name VARCHAR (256)
);