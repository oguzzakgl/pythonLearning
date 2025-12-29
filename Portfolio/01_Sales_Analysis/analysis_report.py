# 05_proje_analiz.py
# "satislar.csv" dosyasını okuyarak satış raporları oluşturur.

import pandas as pd

# 1. Veriyi Okuma
print("--- 1. VERİ YÜKLENİYOR ---")
try:
    df = pd.read_csv("satislar.csv")
    print(df.head())
except FileNotFoundError:
    print("HATA: 'satislar.csv' bulunamadı! Önce '04_proje_veri_uret.py' çalıştırın.")
    exit()

print(f"\nToplam Kayıt: {len(df)}")

# 2. Genel Ciro Analizi
print("\n--- 2. CİRO RAPORU ---")
toplam_ciro = df["Toplam Tutar"].sum()
ortalama_sepet = df["Toplam Tutar"].mean()
print(f"💰 Toplam Ciro: {toplam_ciro:,.2f} TL")
print(f"🛒 Ortalama Sepet Tutarı: {ortalama_sepet:,.2f} TL")

# 3. Şehir Bazlı Satış
print("\n--- 3. ŞEHİR BAZLI PERFORMANS ---")
sehir_ciro = df.groupby("Şehir")["Toplam Tutar"].sum().sort_values(ascending=False)
print(sehir_ciro)

# 4. En Çok Satan Ürünler
print("\n--- 4. EN POPÜLER ÜRÜNLER (ADET) ---")
urun_adet = df.groupby("Ürün")["Adet"].sum().sort_values(ascending=False)
print(urun_adet)

# 5. Kategori Detayı
print("\n--- 5. ÜRÜN DETAYLI RAPOR ---")
detay_rapor = df.groupby("Ürün").agg({
    "Toplam Tutar": "sum",
    "Adet": "sum",
    "Birim Fiyat": "mean" # Fiyat kontrolü için
}).sort_values(by="Toplam Tutar", ascending=False)

# Sütun isimlerini düzenleme
detay_rapor.columns = ["Toplam Ciro", "Toplam Satış Adedi", "Birim Fiyat"]
print(detay_rapor)

# 6. Zaman Analizi
df["Tarih"] = pd.to_datetime(df["Tarih"])
# Sadece gün kısmını alalım (Örn: 2024-01-01)
gunluk_ciro = df.groupby(df["Tarih"].dt.date)["Toplam Tutar"].sum()

print("\n--- 6. GÜNLÜK CİRO ÖRNEĞİ (İLK 5 GÜN) ---")
print(gunluk_ciro.head())
