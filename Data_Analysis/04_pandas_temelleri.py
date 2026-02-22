# KONU: Pandas (Python Data Analysis) Temelleri - 0'dan
# Amaç: Veriyi "Excel Tablosu" gibi yönetmek, temizlemek ve analiz etmek.

import pandas as pd

print("--- PANDAS DERSİ BAŞLIYOR ---\n")

# 1. TABLO OLUŞTURMA (DataFrame)
# ------------------------------------------------------------------
# Pandas'ta tabloya "DataFrame" (Veri Çerçevesi) denir.
# Sözlükten tablo yaratabiliriz:
veri = {
    "Isim": ["Ahmet", "Mehmet", "Ayşe", "Fatma", "Can"],
    "Yas": [25, 30, 22, 28, 40],
    "Maas": [50000, 60000, 45000, 70000, 100000],
    "Departman": ["IT", "IK", "IT", "Finans", "Yönetim"]
}

df = pd.DataFrame(veri)

print("--- 1. Tablomuz ---")
print(df)

# 2. VERİYE ERİŞİM
# ------------------------------------------------------------------
print("\n--- 2. Veriye Erişim ---")
# Sadece bir sütunu alalım
print("Sadece İsimler:")
print(df["Isim"])

# 3. FİLTRELEME (Analizin Kalbi)
# ------------------------------------------------------------------
print("\n--- 3. Filtreleme (IT Çalışanları) ---")
# Şart: Departmanı 'IT' olanlar
it_calisanlari = df[df["Departman"] == "IT"]
print(it_calisanlari)

print("\n--- 3. Filtreleme (Maaşı 60.000'den Yüksek Olanlar) ---")
zenginler = df[df["Maas"] > 60000]
print(zenginler)

# 4. HIZLI ANALİZ (Describe)
# ------------------------------------------------------------------
print("\n--- 4. Hızlı İstatistik (Özet) ---")
# describe() komutu sayısal sütunların özetini çıkarır (Ortalama, Min, Max vs.)
print(df.describe())

# 5. SIRALAMA
# ------------------------------------------------------------------
print("\n--- 5. Sıralama (Maaşa Göre) ---")
sirali = df.sort_values(by="Maas", ascending=False) # Çoktan aza
print(sirali)


print(df.head(2))
print(df.tail(2))