

import pandas as pd
import numpy as np


satir_sayisi = 1000  # 1000 adet satış verisi üreteceğiz


urunler_db = {
    "Laptop": 25000,
    "Telefon": 15000,
    "Kulaklık": 1500,
    "Mouse": 350,
    "Klavye": 750
}
urun_listesi = list(urunler_db.keys())


sehirler = ["İstanbul", "Ankara", "İzmir", "Bursa", "Antalya"]

print("--- VERİ ÜRETİLİYOR (NUMPY GÜCÜ) ---")
np.random.seed(42)


secilen_urunler = np.random.choice(urun_listesi, satir_sayisi)
secilen_sehirler = np.random.choice(sehirler, satir_sayisi)
adetler = np.random.randint(1, 6, satir_sayisi)


birim_fiyatlar = [urunler_db[urun] for urun in secilen_urunler]


df = pd.DataFrame({
    "Tarih": pd.date_range(start="2024-01-01", periods=satir_sayisi, freq="H"),
    "Şehir": secilen_sehirler,
    "Ürün": secilen_urunler,
    "Adet": adetler,
    "Birim Fiyat": birim_fiyatlar
})


df["Toplam Tutar"] = df["Adet"] * df["Birim Fiyat"]

print("--- İLK 5 SATIR ---")
print(df.head())


print(f"\nToplam {len(df)} satır veri üretildi.")
df.to_csv("satislar.csv", index=False, encoding="utf-8-sig")
print("✅ Dosya kaydedildi: satislar.csv")
