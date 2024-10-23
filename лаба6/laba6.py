# 10. Написать функцию, которая строит ER модель базы
# данных. Можно сгенерировать схему в формате HTML или
# XML, либо воспользоваться сторонними приложениями и библиотеками.

import sqlite3 as sq
from eralchemy import render_er

with sq.connect("basa_name.db") as con:
    cur = con.cursor()
    
    cur.execute("DROP TABLE IF EXISTS products")
    cur.execute("DROP TABLE IF EXISTS users")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS users 
        (
        id INTEGER PRIMARY KEY DEFAULT 1,
        name TEXT,
        age INTEGER,
        score INTEGER
        )   
        """)
    cur.execute("""CREATE TABLE IF NOT EXISTS products 
        (
        id INTEGER PRIMARY KEY,
        name TEXT,
        price REAL,
        count INTEGER
        )
        """)
    
    cur.execute("INSERT INTO users (name, age, score) VALUES ('Artur', 20, 1000)")
    cur.execute("INSERT INTO users (name, age, score) VALUES ('Ruslan', 17, 400)")
    cur.execute("INSERT INTO users (name, age, score) VALUES ('Vlad', 20, 800)")
    
    
    
    cur.execute("INSERT INTO products (name, price) VALUES ('подача', 250)")
    cur.execute("INSERT INTO products (name, price) VALUES ('аут', 50)")
    cur.execute("INSERT INTO products (name, price) VALUES ('удар', 150)")
    
    
    
    con.commit()

# Генерация ER диаграммы
render_er("sqlite:///C:/Users/artur/Desktop/Артур/python лабы/лаба6/basa_name.db", 'er.png')
