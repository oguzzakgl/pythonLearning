# KONU: NumPy (Numerical Python) Temelleri - 0'dan
# Amaç: Sayılarla hızlı ve kolay işlem yapmak. Python Listelerinin gelişmiş hali.

import numpy as np

print("--- NUMPY DERSİ BAŞLIYOR ---\n")

# 1. LİSTE vs NUMPY ARRAY
# ------------------------------------------------------------------
# Python Listesi
python_listesi = [1, 2, 3]
# python_listesi * 2 -> [1, 2, 3, 1, 2, 3] yapar (Kopyalar)

# NumPy Dizisi (Array)
numpy_dizisi = np.array([1, 2, 3])
# numpy_dizisi * 2 -> [2, 4, 6] yapar (Matematiksel çarpma!)

print(f"Normal Liste Çarpımı: {python_listesi * 2}")
print(f"NumPy Dizi Çarpımı:   {numpy_dizisi * 2}")

# 2. ARRAY OLUŞTURMA YÖNTEMLERİ
# ------------------------------------------------------------------
sifirlar = np.zeros(5)          # [0. 0. 0. 0. 0.]
birler = np.ones(3)             # [1. 1. 1.]
aralik = np.arange(0, 10, 2)    # [0 2 4 6 8] (Range gibi)

print("\n--- Otomatik Diziler ---")
print("Sıfırlar:", sifirlar)
print("Aralık:  ", aralik)

# 3. İSTATİSTİK (Analiz'in Temeli)
# ------------------------------------------------------------------
notlar = np.array([10, 20, 80, 90, 100, 45, 60])

print("\n--- İstatistik ---")
print("Notlar:      ", notlar)
print("Ortalama:    ", np.mean(notlar))  # Hepsini topla, sayıya böl
print("En Yüksek:   ", np.max(notlar))
print("En Düşük:    ", np.min(notlar))
print("Toplam:      ", np.sum(notlar))

# 4. FİLTRELEME (Çok Güçlü!)
# ------------------------------------------------------------------
# "Bana sadece 50'den büyükleri ver" diyebilirsin.
yuksek_notlar = notlar[notlar > 50]

print("\n--- Filtreleme ---")
print("50'den Büyükler:", yuksek_notlar)
