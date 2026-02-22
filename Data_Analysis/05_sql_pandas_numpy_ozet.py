# KONU: SQL, Pandas ve NumPy ÖZETİ (Detaylı Anlatım)
# Amaç: Bu 3 teknolojinin nasıl birlikte çalıştığını adım adım görmek.

import sqlite3          # Veritabanı motoru (Backend)
import pandas as pd     # Veri Analizi aracı (Excel gibi)
import numpy as np      # Matematik kütüphanesi (Hızlı Hesaplama)

print("--- 1. BÖLÜM: SQL ile Veritabanı Kurulumu ---")
# 1. BAĞLANTI: Bilgisayarın RAM'inde geçici bir kasa (Veritabanı) açıyoruz.
# ":memory:" demek, dosya oluşturma, sadece hafızada tut ve program bitince sil demektir.
con = sqlite3.connect(":memory:")
cur = con.cursor()  # Cursor: Veritabanına emir veren yetkili.

# 2. TABLO: "urunler" adında bir tablo yaratıyoruz.
# Tabloda 3 sütun var: ad (Yazı), fiyat (Sayı), stok (Sayı)
cur.execute("CREATE TABLE urunler (ad TEXT, fiyat INTEGER, stok INTEGER)")

# 3. VERİ EKLEME: Listeden topluca veri ekliyoruz.
# SQL bu verileri diske (veya RAM'e) en verimli şekilde dizer.
yeni_urunler = [
    ('Bilgisayar', 30000, 5),
    ('Mouse', 500, 100),
    ('Klavye', 1500, 50),
    ('Kulaklık', 2000, 20),
    ('Monitor', 6000, 10)
]
cur.executemany("INSERT INTO urunler VALUES (?, ?, ?)", yeni_urunler)
con.commit() # "Kaydet" butonuna basmak gibidir.
print("✅ SQL: Veriler veritabanına başarıyla kaydedildi.")


print("\n--- 2. BÖLÜM: PANDAS ile Veri Analizi ---")
# 1. VERİYİ ÇEKME: SQL'e "Git bana urunler tablosunu getir" diyoruz.
# Pandas bu veriyi alıp "DataFrame" denilen akıllı tabloya çevirir.
df = pd.read_sql("SELECT * FROM urunler", con)

print("📊 Tüm Tablo:\n", df)

# 2. İSTATİSTİK: Tek komutla tüm sayısal analizi yapar.
# count: Kaç tane var? | mean: Ortalama kaç? | min/max: En ucuz/pahalı?
print("\n📈 Hızlı İstatistik Raporu:\n", df.describe())

# 3. FİLTRELEME: "Stok sayısı 20'den az olan ürünler hangileri?"
# Bu satır, SQL'deki "WHERE" komutunun Pandas halidir.
kritik_stok = df[df["stok"] < 20]
print("\n⚠️ Stok Kritik Olan Ürünler:\n", kritik_stok)


print("\n--- 3. BÖLÜM: NUMPY ile Matematik ---")
# Pandas tablosundan sadece "fiyat" sütununu alıp NumPy dizisine çeviriyoruz.
# NumPy, Python listelerinden 50 kat daha hızlıdır.
fiyatlar = np.array(df["fiyat"])

print("💰 Fiyat Listesi:", fiyatlar)

# Matematiksel İşlemler
ortalama = np.mean(fiyatlar)        # Ortalama Bulma
en_pahali = np.max(fiyatlar)        # En yükseği bulma
zamli = fiyatlar * 1.5              # Her fiyata %50 zam yap (Vektörizasyon)

print(f"Ortalama Fiyat: {ortalama} TL")
print(f"En Pahalı Ürün: {en_pahali} TL")
print(f"Zamlı Fiyatlar: {zamli}")

print("\n--- 4. BÖLÜM: NumPy Fonksiyon Sözlüğü ---")
# Rastgele bir dizi oluşturalım: [10, 20, 50, 120]
test_dizisi = np.array([10, 20, 50, 120])
print(f"Test Dizisi: {test_dizisi}")

# Sık Kullanılan Komutlar:
print(f"np.mean:   {np.mean(test_dizisi)}")   # ORTALAMA (Hepsini topla / Sayıya böl)
print(f"np.max:    {np.max(test_dizisi)}")    # EN BÜYÜK (Zirvedeki sayı)
print(f"np.min:    {np.min(test_dizisi)}")    # EN KÜÇÜK (Dipteki sayı)
print(f"np.sum:    {np.sum(test_dizisi)}")    # TOPLAM (Hepsini topla)
print(f"np.std:    {np.std(test_dizisi)}")    # STANDART SAPMA (Veriler ne kadar dağınık?)
print(f"np.median: {np.median(test_dizisi)}") # ORTANCA (Küçükten büyüğe sırala, ortadakini al)
print(f"np.size:   {np.size(test_dizisi)}")   # ELEMAN SAYISI (Kaç tane var?)

