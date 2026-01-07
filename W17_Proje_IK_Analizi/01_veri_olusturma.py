import pandas as pd
import numpy as np
from faker import Faker
import random
import os

# 1. Ayarlar
fake = Faker('tr_TR')
random.seed(42)
np.random.seed(42)

# 2. Sabit Listeler
DEPARTMANLAR = ['IT', 'İnsan Kaynakları', 'Finans', 'Satış', 'Pazarlama', 'Üretim']
EGITIM_SEVIYELERI = ['Lise', 'Lisans', 'Yüksek Lisans', 'Doktora']

# 3. Veri Üretimi
calisan_listesi = []

print("Veri üretiliyor, lütfen bekleyin...")

for _ in range(1000):
    # Kişisel Bilgiler
    isim = fake.name()
    sehir = fake.city()
    yas = random.randint(22, 60)
    
    # İş Bilgileri
    departman = random.choice(DEPARTMANLAR)
    egitim = random.choice(EGITIM_SEVIYELERI)
    tecrube = max(0, yas - 22 - random.randint(0, 5))
    
    # Maaş Hesaplama
    base_maas = 25000
    maas = base_maas + (tecrube * 2500)
    
    if departman in ['IT', 'Finans']:
        maas = maas * 1.2
        
    if egitim in ['Yüksek Lisans', 'Doktora']:
        maas = maas + 3000
        
    # Performans
    performans = int(np.random.normal(70, 15))
    performans = max(1, min(100, performans))
    
    # Listeye Ekle
    calisan_listesi.append({
        'Isim': isim,
        'Sehir': sehir,
        'Yas': yas,
        'Departman': departman,
        'Egitim': egitim,
        'Tecrube': tecrube,
        'Maas': int(maas),
        'Performans': performans
    })

# 4. Kaydetme
df = pd.DataFrame(calisan_listesi)

current_dir = os.path.dirname(os.path.abspath(__file__))
dosya_adi = os.path.join(current_dir, 'ik_performans.csv')

df.to_csv(dosya_adi, index=False)

print("\nVeri başarıyla üretildi.")
print(f"Dosya Yolu: {dosya_adi}")
print("-" * 30)
print(df.head())
