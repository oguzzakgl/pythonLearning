from faker import Faker
import pandas as pd

# ==========================================
# FAKER KÜTÜPHANESİ KULLANIMI
# ==========================================
print("--- FAKER KÜTÜPHANESİ İLE SAHTE VERİ ÜRETİMİ ---\n")

# 1. Faker Nesnesi Oluşturma
# Faker sınıfından bir nesne üretiyoruz.
# 'tr_TR' parametresi ile Türkçe veriler üretebiliriz (isimler, adresler vb.)
# fk = Faker('tr_TR')  # Türkçe kullanım
fake = Faker()         # İngilizce (Varsayılan) kullanım

print("1. Rastgele Kişi Bilgileri:")
# name(): Rastgele ad soyad
print(f"İsim: {fake.name()}")

# address(): Rastgele adres
print(f"Adres: {fake.address()}")

# email(): Rastgele e-posta
print(f"Email: {fake.email()}")
print("-" * 30)

print("2. İş ve Şirket Bilgileri:")
# job(): Meslek
print(f"Meslek: {fake.job()}")

# company(): Şirket adı
print(f"Şirket: {fake.company()}")
print("-" * 30)

print("3. Diğer Yararlı Veriler:")
# date_between(): Belirli tarihler arası rastgele tarih
print(f"Tarih (Son 2 yıl): {fake.date_between(start_date='-2y', end_date='today')}")

# random_int(): Rastgele sayı (maaş vb. için)
print(f"Rastgele Maaş: {fake.random_int(min=20000, max=80000)}")

# color_name(): Renk ismi
print(f"Renk: {fake.color_name()}")
print("-" * 30)

print("4. Basit Bir Veri Seti Oluşturma (Pandas ile):")
# Bir liste içinde sözlükler oluşturarak DataFrame'e çevirebiliriz.

data_list = []

# 5 kişilik örnek veri üretelim
for _ in range(5):
    data_list.append({
        'Ad Soyad': fake.name(),
        'Meslek': fake.job(),
        'Email': fake.email(),
        'Sehir': fake.city()
    })

df = pd.DataFrame(data_list)
print("Oluşturulan Fake Veri Seti:")
print(df)

# İsterseniz bunu kaydebilirsiniz:
# df.to_csv('fake_data_ornegi.csv', index=False)
