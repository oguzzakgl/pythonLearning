# Veri Analizi ve Raporlama (Pandas & SQL)
import pandas as pd
import numpy as np   
import sqlite3   

con = sqlite3.connect("stok.db")
df = pd.read_sql("SELECT * FROM urunler", con)
con.close()



print(df)

print("---------------------------------------")


print(df[df["stok"] < 20])
print("---------------------------------------")
print(df[df["stok"] > 40])
print("---------------------------------------")
print(df[df["stok"] > 80])
print("---------------------------------------")
print(df[df["stok"] == 100])
print("---------------------------------------")
print(df[df["fiyat"] < 1000])
print("---------------------------------------")
