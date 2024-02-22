CREATE DATABASE Database;


CREATE TABLE users
(
id int primary key,
sn string,
fn string,
pt string
);


CREATE TABLE roles
(
id int primary key,
caption string unique
);