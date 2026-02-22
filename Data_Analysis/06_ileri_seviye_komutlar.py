# KONU: Sektörde En Çok Kullanılan "Pro" Komutlar
# Amaç: SQL, Pandas ve NumPy'ın ileri seviye özelliklerini kod üzerinde görmek.

import sqlite3
import pandas as pd
import numpy as np

print("--- 1. BÖLÜM: SQL (JOIN & GROUP BY) ---")
con = sqlite3.connect(":memory:")
cur = con.cursor()

# İki ayrı tablo oluşturalım: Siparişler ve Müşteriler
cur.execute("CREATE TABLE musteriler (id INTEGER, isim TEXT)")
cur.execute("CREATE TABLE siparisler (id INTEGER, musteri_id INTEGER, tutar INTEGER)")

# Veri Ekleme
cur.executemany("INSERT INTO musteriler VALUES (?, ?)", [(1, 'Ali'), (2, 'Veli')])
cur.executemany("INSERT INTO siparisler VALUES (?, ?, ?)", [(101, 1, 500), (102, 1, 250), (103, 2, 1000)])
con.commit()

# A) JOIN (BİRLEŞTİRME): "Hangi sipariş hangi müşterinin?"
# Müşteri ismini ve Harcadığı tutarı yan yana getir.
print("\n--- JOIN Örneği ---")
sql_join = """
SELECT musteriler.isim, siparisler.tutar 
FROM siparisler 
JOIN musteriler ON siparisler.musteri_id = musteriler.id
"""
cur.execute(sql_join)
print(cur.fetchall())

# B) GROUP BY (GRUPLAMA): "Ali toplam ne kadar harcadı?"
print("\n--- GROUP BY Örneği ---")
sql_group = """
SELECT musteriler.isim, SUM(siparisler.tutar) 
FROM siparisler 
JOIN musteriler ON siparisler.musteri_id = musteriler.id
GROUP BY musteriler.isim
"""
cur.execute(sql_group)
print(cur.fetchall())


print("\n\n--- 2. BÖLÜM: PANDAS (TEMİZLİK & RAPOR) ---")
# İçinde eksik veri (None) olan bir tablo oluşturalım
veri = {
    "Departman": ["IT", "IT", "IK", "IK", "Finans"],
    "Maas": [50000, None, 40000, 45000, 80000] # Dikkat: 2. eleman boş (None)
}
df = pd.DataFrame(veri)
print("Orijinal Tablo:\n", df)

# A) VERİ TEMİZLEME (Fillna/Dropna)
print("\n--- Eksik Verileri Doldurma ---")
# Boş (NaN) maaşları 0 yap
df_temiz = df.fillna(0)
print(df_temiz)

# B) GROUP BY (Pandas Tarzı)
print("\n--- Departman Bazlı Ortalama Maaş ---")
# Her departmanın maaş ortalamasını al
print(df_temiz.groupby("Departman")["Maas"].mean())


print("\n\n--- 3. BÖLÜM: NUMPY (ŞEKİL & RASTGELELİK) ---")

# A) RESHAPE (Şekil Değiştirme)
print("--- Reshape Örneği ---")
duz_dizi = np.arange(1, 11) # 1'den 10'a kadar sayılar
print("Düz:", duz_dizi)

matris = duz_dizi.reshape(2, 5) # 2 Satır, 5 Sütun yap
print("\nMatris (2x5):\n", matris)

# B) RANDOM (Rastgele Veri Üretme)
print("\n--- Random Örneği ---")
# 0 ile 100 arasında 3 tane rastgele sayı tut
rastgele_sayilar = np.random.randint(0, 100, 3)
print("Şanslı Sayılar:", rastgele_sayilar)
