import sqlite3
conn = sqlite3.connect('database.db')

conn.execute('create table users(id integer primary key autoincrement, name varchar(100), email varchar(255), password varchar(500));')
conn.close()