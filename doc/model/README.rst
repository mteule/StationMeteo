Step by step generation of model.py from Dia:
=============================================
Dia diagram:
------------
First we have to create the Diagram, the method is described in a tutorial [left.subtree].

SQL .sql file generation:
-------------------------
Checking for the warnings:

    $ parsediasql --file model.dia --db mysql-innodb 1>/dev/null 

Generating the .sql file:

    $ parsediasql --file model.dia --db mysql-innodb 2>/dev/null 1>schema.mysql.sql

In the .sql file it is specified:

    -- Typemap for mysql-innodb not found in input file   
    
SQL .sql file edition:
----------------------
There is a problem with :parsediasql:, it needs the same type in the two tables for the id.
But it will be impossible for mysql to create the tables with 2 'auto_increment' in the same 'Metering' table.
We'll have to remove the 'auto_increment' attribute for the column db.Metering.sensor_id.

Dia diagram edition:
--------------------
To remember the above evocated need for an edition,
we put it in the 'db.Metering.sensor_id' attribute comments.

Mysql Database creation:
------------------------

    $ sudo mysql -u root -p
    mysql> SET PASSWORD FOR 'root'@'localhost' = PASSWORD('nouveau_mot');
    mysql> GRANT ALL PRIVILEGES ON test_dia.* TO 'monty'@'localhost' IDENTIFIED BY 'passwd' WITH GRANT OPTION;
    mysql> use test_dia;
    mysql> source schema.mysql.sql;
    mysql> show tables;

It's better to check the tables are well created.
The Foreign Keys will be easily checked latter by the sqlalchemy insertion verifications.
For example with wrong sensor_id.

Sqlalchemy declarative 'model.py' creation:
-------------------------------------------

    $ sqlacodegen mysql://monty:'passwd'@localhost/test_dia

    $ sqlacodegen mysql://monty:'passwd'@localhost/test_dia 1>model.py

The foreign key existence can be checked with the 2 python lines:

    sensor_id = Column(ForeignKey('Sensor.id'), index=True)
    
    sensor = relationship(u'Sensor')

References:
===========
[left.subtree] http://left.subtree.org/2007/12/05/database-design-with-dia/

