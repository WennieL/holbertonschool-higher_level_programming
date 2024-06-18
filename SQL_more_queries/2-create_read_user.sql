-- creates the database hbtn_0d_2 and the user user_0d_2.

CREATE DATABASE IF not exists hbtn_0d_2;
CREATE USER IF not exists user_0d_2@localhost
IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.*
TO USER user_0d_2@localhost;