import sqlite3
import sys
import os

from pygame.midi import Input


def add(first_name,last_name,email):
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()
    c.execute('INSERT INTO customer VALUES (?,?,?)',(first_name,last_name,email))
    conn.commit()
    conn.close()

def delete(rowid):
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()
    c.execute('DELETE FROM customer WHERE rowid = ?',(rowid,))
    conn.commit()
    conn.close()

def show():
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()
    c.execute('SELECT rowid , * FROM customer')
    for x in c.fetchall():
        return x
    conn.commit()
    conn.close()

def update():
    info = input('''What you wanted to Update , Press :
    1. For First_name
    2. For Last_name
    3. For Email''')

    if info == "1":
        rowid = input("Enter Rowid:")
        last_name = input("Enter Last Name:")
        email = input("Enter Email:")
        updated_first_name = input("Enter Updated First Name")
        conn = sqlite3.connect("customer.db")
        c = conn.cursor()
        c.execute('UPDATE customer SET first_name = ? WHERE rowid = ? AND last_name = ? AND email = ?',
                  (updated_first_name,
                            rowid,
                            last_name,
                            email))
        for x in c.fetchall():
            return x
        conn.commit()
        conn.close()
    elif info == "2":
        rowid = input("Enter Rowid:")
        first_name = input("Enter First Name:")
        email = input("Enter Email:")
        updated_last_name = input("Enter Updated Last Name:")
        conn = sqlite3.connect("customer.db")
        c = conn.cursor()
        c.execute('UPDATE customer SET last_name = ? WHERE rowid = ? AND first_name = ? AND email = ?',
                  (updated_last_name,rowid, first_name, email))
        for x in c.fetchall():
            return x
        conn.commit()
        conn.close()
    elif info == "3":
        rowid = input("Enter Rowid:")
        first_name = input("Enter First Name:")
        last_name = input("Enter Updated Last Name:")
        updated_email = input("Enter Updated Email:")
        conn = sqlite3.connect("customer.db")
        c = conn.cursor()
        c.execute('UPDATE customer SET email = ? WHERE rowid = ? AND first_name = ? AND last_name = ?',
                  (updated_email, rowid, first_name, last_name))
        for x in c.fetchall():
            return x
        conn.commit()
        conn.close()
    else:
        print("Invalid Entry")



