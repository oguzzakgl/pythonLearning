

import pandas as pd


print("--- 1. VERİ YÜKLENİYOR ---")
try:
    df = pd.read_csv("satislar.csv")
    print(df.head())
except FileNotFoundError:
    print("HATA: 'satislar.csv' bulunamadı! Önce '04_proje_veri_uret.py' çalıştırın.")
    exit()

print(f"\nToplam Kayıt: {len(df)}")


print("\n--- 2. CİRO RAPORU ---")
toplam_ciro = df["Toplam Tutar"].sum()
ortalama_sepet = df["Toplam Tutar"].mean()
print(f"💰 Toplam Ciro: {toplam_ciro:,.2f} TL")
print(f"🛒 Ortalama Sepet Tutarı: {ortalama_sepet:,.2f} TL")


print("\n--- 3. ŞEHİR BAZLI PERFORMANS ---")
sehir_ciro = df.groupby("Şehir")["Toplam Tutar"].sum().sort_values(ascending=False)
print(sehir_ciro)


print("\n--- 4. EN POPÜLER ÜRÜNLER (ADET) ---")
urun_adet = df.groupby("Ürün")["Adet"].sum().sort_values(ascending=False)
print(urun_adet)


print("\n--- 5. ÜRÜN DETAYLI RAPOR ---")
detay_rapor = df.groupby("Ürün").agg({
    "Toplam Tutar": "sum",
    "Adet": "sum",
    "Birim Fiyat": "mean"
}).sort_values(by="Toplam Tutar", ascending=False)

detay_rapor.columns = ["Toplam Ciro", "Toplam Satış Adedi", "Birim Fiyat"]
print(detay_rapor)

gunluk_ciro = df.groupby(df["Tarih"].dt.date)["Toplam Tutar"].sum()

print("\n--- 6. GÜNLÜK CİRO ÖRNEĞİ (İLK 5 GÜN) ---")
print(gunluk_ciro.head())
