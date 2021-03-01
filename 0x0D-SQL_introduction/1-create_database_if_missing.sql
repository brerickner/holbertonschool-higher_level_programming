-- script that creates the database hbtn_0c_0
IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'hbtn_0c_0')
    CREATE DATABASE hbtn_0c_0;
