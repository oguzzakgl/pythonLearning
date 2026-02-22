# KONU: SQL, NumPy ve Pandas Entegrasyonu
# Amaç: 
# 1. SQL: Veriyi saklamak (Depo)
# 2. NumPy: Sayısal hesaplama yapmak (Hesap Makinesi)
# 3. Pandas: Veriyi raporlamak ve göstermek (Excel)

import sqlite3
import pandas as pd
import numpy as np

# ---------------------------------------------------------
# ADIM 1: SQL (BACKEND) - Veri Üretme
# ---------------------------------------------------------
print("--- 1. SQL ADIMI: Veritabanı Oluşturuluyor ---")

# Geçici (RAM'de) bir veritabanı kuralım
baglanti = sqlite3.connect(":memory:") 
cursor = baglanti.cursor()

# Tablo Yapısı
cursor.execute("CREATE TABLE sinavlar (ogrenci_adi TEXT, notu INTEGER)")

# Veri Ekleyelim
veriler = [
    ("Ahmet", 85),
    ("Ayşe", 90),
    ("Mehmet", 45),
    ("Fatma", 60),
    ("Ali", 100)
]
cursor.executemany("INSERT INTO sinavlar VALUES (?, ?)", veriler)
baglanti.commit()
print("✅ Veriler SQL'e kaydedildi.")

# ---------------------------------------------------------
# ADIM 2: PANDAS (ANALİZ) - Veriyi Çekme
# ---------------------------------------------------------
print("\n--- 2. PANDAS ADIMI: Veri SQL'den Çekiliyor ---")

# SQL'den veriyi alıp Pandas DataFrame'e (Tabloya) çevirir
df = pd.read_sql("SELECT * FROM sinavlar", baglanti)

print("Pandas Tablosu:")
print(df)

# ---------------------------------------------------------
# ADIM 3: NUMPY (MATEMATİK) - Hesaplama
# ---------------------------------------------------------
print("\n--- 3. NUMPY ADIMI: İstatistiksel Hesaplama ---")

notlar = df["notu"].values # Pandas sütununu NumPy dizisine çevir

ortalama = np.mean(notlar)
standart_sapma = np.std(notlar)
en_yuksek = np.max(notlar)

print(f"Sınıf Ortalaması:  {ortalama}")
print(f"Standart Sapma:    {standart_sapma:.2f}")
print(f"En Yüksek Not:     {en_yuksek}")

# ---------------------------------------------------------
# BONUS: Pandas ile Filtreleme
# ---------------------------------------------------------
print("\n--- BONUS: Geçenler (Notu 50'den Büyük) ---")
gecenler = df[df["notu"] > 50]
print(gecenler)
