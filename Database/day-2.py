# SQL = Structure query language

# DDL -- DATA DEFINATION LANGUAGE
# DML -- DATA MALIPULATION LANGUAGE
# DQL -- DATA QUERY LANGUAGE
# DCL -- DATA CONTROL LANGUAGE


# DDL -- DATA DEFINATION LANGUAGE

# used to define structure of data/tables

# commands    purpose

# CREATE    USED TO CREATE TABLE
# ALTER     USED TO UPDATE/MODIFY TABLE
# DROP      USED TO DELETE TABLE


# DML -- DATA MALIPULATION LANGUAGE

# used to change the data

# commands  purpose
# INSERT    USED TO ADD DATA
# UPDATE    USED TO MODIFY/UPDATE DATA
# DELETE    USED TO DELETE DATA


# DQL -- DATA QUERY LANGUAGE

# used to retriwe/read data

# commands      purpose
# SELECT    USED TO READ DATA

# DCL -- DATA CONTROL LANGUAGE

# used to apply permission/restiction

# commands      purpose
# GRANT      used to grant permission
# REVOKE     used to take back the permission


# DATA TYPES IN SQL (PostgreSQL)

# Data type     Meaning
# -----------------------
# INT           integer
# VARCHAR(50)   string/text
# TEXT          text
# BOOLEAN       ture/false
# DATE          date
# FLOAT         decimal value


# CREATE TABLE
# COMMAND : CREATE
# SYNTAX : CREATE TABLE TABLE_NAME (col_name_1 datatype, col_name_2 datatype,....);

# INSERT DATA
# COMMAND : INSERT
# SYNTAX : INSERT INTO TABLE_NAME (col_nmae_1, col_name_2,...) VALUES (val_1, val_2,....);

# INSERT MUITIPLE ENTRIES
# COMMAND : INSERT
# SYNTAX : INSERT INTO TABLE_NAME (col_nmae_1, col_name_2,...) 
# VALUES (val_1, val_2,....),(val_1, val_2,....),(val_1, val_2,....),(val_1, val_2,....);


# READ DATA
# COMMAND : SELECT
# SYNTAX : SELECT * FROM table_name;

# UPDATE DATA
# COMMAND : UPDATE
# SYNTAX : UPDATE TABLE_NAME SET col_name = value WHERE condition;

# DELETE DATA
# COMMAND : DELETE
# SYNTAX : DELETE FROM TABLE_NAME WHERE condition;


# ADD NEW COLUMN
# COMMAND : ALTER 
# SYNTAX : ALTER TABLE table_name ADD COLUMN col_name data_type;

# RENAME A COLUMN
# COMMAND : ALTER
# SYNTAX : ALTER TABLE table_name RENAME COLUMN col_name to new_col_nmae;

# DROP COLUMN/DELETE COLUMN
# COMMAND : ALTER
# SYNTAX : ALTER TABLE table_name DROP COLUMN col_name;

# DROT TABLE
# COMMAND : DROP
# SYNTAX : DROP TABLE table_name;