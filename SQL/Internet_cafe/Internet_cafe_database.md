# Internet Cafe Database

This is a MySQL database that I created to demonstrate my current skills. It was created on the Internet cafe theme, like a telegram bot, so using some libraries and making small changes to the bot code, you can connect this database to it.

### I used:
* dbForge Studio 2020 for MySQL tool for writing code and queries, as well as editing the table itself through the built-in parameters of Alter Table.
* MySQL workbench to visualize the result in the form of a Model (diagram).
* MySQL command line client to fulfill requests.


## Internet Cafe Client

This table is for storing user data. This is the key table, which will be visible on the diagram.
The [code for creating](Create-table-internet_cafe_client.sql) this table looks like this:
```
CREATE TABLE internet_cafe.internet_cafe_client (
  ID int NOT NULL AUTO_INCREMENT,
  Name text NOT NULL,
  Email text NOT NULL,
  Password text NOT NULL,
  Key_word text NOT NULL,
  Code_Comp int NOT NULL,
  PRIMARY KEY (ID)
);
```

