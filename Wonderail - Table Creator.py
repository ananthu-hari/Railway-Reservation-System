#Program to create MySql tables for project Wonderail...
import mysql.connector as sql
from mysql.connector import Error
try:
    connection=sql.connect(host="localhost",username="root",password="root",database="WONDERAIL")
    cursor=connection.cursor()
except Error as e:
    print(e)
try:
    query="CREATE TABLE TICKET (USERNAME VARCHAR(25),TICKET_ID INT PRIMARY KEY UNIQUE,TRAIN_NO INT,DATE_OF_JOURNEY DATE,MOBILE_NUMBER BIGINT,EMAIL_ID VARCHAR(25),PASSENGER_DETAILS VARCHAR(100),TRAIN_NAME VARCHAR(30));"
    cursor.execute(query)
    connection.commit()
except Error as e:
    print(e)
try:
    query="CREATE TABLE ADMIN(USERNAME VARCHAR(25) PRIMARY KEY UNIQUE,PASSWORD VARCHAR(15),NAME VARCHAR(25));"
    cursor.execute(query)
    connection.commit()
except Error as e:
    print(e)
try:
    query="INSERT INTO ADMIN VALUES('admin','ananthu','ANANTHAKRISHNAN T H');"
    cursor.execute(query)
    connection.commit()
except Error as e:
    print(e)
try:
    query="CREATE TABLE TRAIN(TRAIN_NO INT PRIMARY KEY UNIQUE,TRAIN_NAME VARCHAR(30) UNIQUE, FROM_STATION VARCHAR(25),TO_STATION VARCHAR(25),VIA VARCHAR(100),TOTAL_SEATS INT);"
    cursor.execute(query)
    connection.commit()
except Error as e:
    print(e)
try:
    query="INSERT INTO TRAIN VALUES(16315,'Mysore-Kochuveli Express','Mysore','Trivandrum','Banglore,Palakkad,Thrissur,Aluva,Ernakulam,Alappuzha,Kochuveli',500);"
    cursor.execute(query)
    query="INSERT INTO TRAIN VALUES(16316,'Kochuveli-Mysore Express','Trivandrum','Mysore','Kochuveli,Alappuzha,Ernakulam,Aluva,Thrissur,Palakkad,Banglore',500);"
    cursor.execute(query)
    query="INSERT INTO TRAIN VALUES(16315,'Mysore-Kochuveli Express','Mysore','Trivandrum','Banglore,Palakkad,Thrissur,Aluva,Ernakulam,Alappuzha,Kochuveli',500);"
    cursor.execute(query)
    query="INSERT INTO TRAIN VALUES(16315,'Mysore-Kochuveli Express','Mysore','Trivandrum','Banglore,Palakkad,Thrissur,Aluva,Ernakulam,Alappuzha,Kochuveli',500);"
    cursor.execute(query)
    query="INSERT INTO TRAIN VALUES(16315,'Mysore-Kochuveli Express','Mysore','Trivandrum','Banglore,Palakkad,Thrissur,Aluva,Ernakulam,Alappuzha,Kochuveli',500);"
    cursor.execute(query)
    
    connection.commit()
except Error as e:
    print(e)
try:
    query="CREATE TABLE USER(NAME VARCHAR(25),AGE INT,PHONE_NUMBER BIGINT UNIQUE,EMAIL_ID VARCHAR(25) UNIQUE,USERNAME VARCHAR(25) PRIMARY KEY UNIQUE,PASSWORD VARCHAR(15));"
    cursor.execute(query)
    connection.commit()
except Error as e:
    print(e)
    
