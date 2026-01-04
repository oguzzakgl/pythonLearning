import sqlite3
import pandas as pd
from datetime import datetime
import os

# Veritabanı Bağlantısı ve Tablo Oluşturma
# ...
def get_db_connection():
    con = sqlite3.connect('finance.db')
    cursor = con.cursor()
    return con, cursor

def create_tables():
    con, cursor = get_db_connection()

    base_dir = os.path.dirname(os.path.abspath(__file__))
    schema_path = os.path.join(base_dir, 'schema.sql')

    with open(schema_path, 'r') as f:
        sql_script = f.read()

    cursor.executescript(sql_script)

    con.commit()
    con.close()

def add_transaction(kullanici_id, baslik, miktar, tip, tarih):
    con, cursor = get_db_connection()
    cursor.execute('''
        INSERT INTO transactions (kullanici_id, baslik, miktar, tip, tarih)
        VALUES (?, ?, ?, ?, ?)
    ''', (kullanici_id, baslik, miktar, tip, tarih))
    con.commit()
    con.close()

def get_transactions(kullanici_id):
    con, cursor = get_db_connection()
    cursor.execute('''
        SELECT * FROM transactions WHERE kullanici_id = ?
    ''', (kullanici_id,))
    transactions = cursor.fetchall()
    con.close()
    return transactions

def init_db():
    create_tables()