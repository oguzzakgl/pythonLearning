# 04_proje_veri_uret.py
# Analiz için rastgele satış verisi üretir.

import pandas as pd
import numpy as np

# 1. Veri Ayarları
satir_sayisi = 1000  # 1000 adet satış verisi üreteceğiz

# Ürünler ve fiyatları
urunler_db = {
    "Laptop": 25000,
    "Telefon": 15000,
    "Kulaklık": 1500,
    "Mouse": 350,
    "Klavye": 750
}
urun_listesi = list(urunler_db.keys())

# Şehirler
sehirler = ["İstanbul", "Ankara", "İzmir", "Bursa", "Antalya"]

print("--- VERİ ÜRETİLİYOR (NUMPY GÜCÜ) ---")
np.random.seed(42) # Tekrarlanabilirlik için random seed

# Rastgele Seçimler
secilen_urunler = np.random.choice(urun_listesi, satir_sayisi)
secilen_sehirler = np.random.choice(sehirler, satir_sayisi)
adetler = np.random.randint(1, 6, satir_sayisi) # 1-5 arası rastgele adet

# Ürün fiyatlarını eşleştirme
birim_fiyatlar = [urunler_db[urun] for urun in secilen_urunler]

# 2. DataFrame Oluşturma
df = pd.DataFrame({
    "Tarih": pd.date_range(start="2024-01-01", periods=satir_sayisi, freq="H"), # Saat başı satış
    "Şehir": secilen_sehirler,
    "Ürün": secilen_urunler,
    "Adet": adetler,
    "Birim Fiyat": birim_fiyatlar
})

# Toplam Tutar Hesapla
df["Toplam Tutar"] = df["Adet"] * df["Birim Fiyat"]

print("--- İLK 5 SATIR ---")
print(df.head())

# 3. CSV Kaydı Bilgilendirmesi
print(f"\nToplam {len(df)} satır veri üretildi.")
df.to_csv("satislar.csv", index=False, encoding="utf-8-sig")
print("✅ Dosya kaydedildi: satislar.csv")
