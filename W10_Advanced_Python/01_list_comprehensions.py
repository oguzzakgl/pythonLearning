# Konu: List Comprehensions
# Amaç: Döngüleri tek satırda yazarak daha hızlı ve temiz kod oluşturmak.

numbers=[1,2,3,4,5]
list2=[]

for number in numbers:
    list2.append(number)
print(list2)    

list3 = [number*2 for number in numbers]
print(f"Çarpma İşlemi: {list3}")

# ADIM 2: FİLTRELEME (Sadece belirli sayıları al)
# Klasik Yöntem:
cift_sayilar = []
for number in numbers:
    if number % 2 == 0:
        cift_sayilar.append(number)
print(f"Klasik Çiftler: {cift_sayilar}")

# List Comprehension Yöntemi:
# Mantık: [YAPILACAK_ISLEM for DEGISKEN in LISTE if KOSUL]
# Soru: Neden iki tane 'number' var?
# Cevap: 
# 1. 'number': Listeye eklenecek olan şey (Sonuç). Buraya 'number*2' veya 'str(number)' da yazabilirdik.
# 2. 'number': Döngüdeki geçici değişken adı (for i in numbers'daki i gibi).
cift_sayilar_comp = [number for number in numbers if number % 2 == 0]
print(f"Modern Çiftler: {cift_sayilar_comp}")

# ADIM 3: IF-ELSE KULLANIMI (Her sayıya bir işlem yap ama şarta göre değişsin)
# Örnek: Çift sayılar kalsın, tek sayılar "Tek" yazılsın.
# Mantık: [SONUC_IF if KOSUL else SONUC_ELSE for DEGISKEN in LISTE]
sonuc = [number if number % 2 == 0 else "Tek" for number in numbers]
print(f"If-Else Sonuç: {sonuc}")

# ---------------------------------------------------------
# GERÇEK HAYAT SENARYOLARI (Real World Examples)
# ---------------------------------------------------------

print("\n--- GERÇEK HAYAT SENARYOLARI ---")

# SENARYO 1: Veri Temizleme (Web Scraping / E-Ticaret)
# İnternetten fiyatlar böyle bozuk geldi diyelim:
fiyatlar_db = ["100TL", "250TL", "50TL", "800TL"]
# Bizim bunları matematiksel işlem yapmak için sayıya çevirmemiz lazım.
temiz_fiyatlar = [int(fiyat.replace("TL", "")) for fiyat in fiyatlar_db]
print(f"1. Temizlenmiş Fiyatlar: {temiz_fiyatlar}")


# SENARYO 2: Dosya İşlemleri (Sadece Resimleri Bulma)
# Bir klasördeki dosya listesi elimizde olsun:
dosyalar = ["resim1.jpg", "veri.json", "profil.png", "notlar.txt", "logo.jpg"]
# Sadece .jpg ve .png olanları alalım:
resimler = [dosya for dosya in dosyalar if dosya.endswith((".jpg", ".png"))]
print(f"2. Bulunan Resimler: {resimler}")


# SENARYO 3: Veritabanından Kullanıcı E-maillerini Çekme (API / Backend)
# Veritabanından gelen kullanıcı listesi (Dictionary listesi gibi düşün):
users = [
    {"id": 1, "name": "Ali", "email": "ali@gmail.com", "active": True},
    {"id": 2, "name": "Ayşe", "email": "ayse@hotmail.com", "active": False},
    {"id": 3, "name": "Mehmet", "email": "mehmet@yahoo.com", "active": True}
]
# Konu: List Comprehensions
# Amaç: Döngüleri tek satırda yazarak daha hızlı ve temiz kod oluşturmak.

numbers=[1,2,3,4,5]
list2=[]

for number in numbers:
    list2.append(number)
print(list2)    

list3 = [number*2 for number in numbers]
print(f"Çarpma İşlemi: {list3}")

# ADIM 2: FİLTRELEME (Sadece belirli sayıları al)
# Klasik Yöntem:
cift_sayilar = []
for number in numbers:
    if number % 2 == 0:
        cift_sayilar.append(number)
print(f"Klasik Çiftler: {cift_sayilar}")

# List Comprehension Yöntemi:
# Mantık: [YAPILACAK_ISLEM for DEGISKEN in LISTE if KOSUL]
# Soru: Neden iki tane 'number' var?
# Cevap: 
# 1. 'number': Listeye eklenecek olan şey (Sonuç). Buraya 'number*2' veya 'str(number)' da yazabilirdik.
# 2. 'number': Döngüdeki geçici değişken adı (for i in numbers'daki i gibi).
cift_sayilar_comp = [number for number in numbers if number % 2 == 0]
print(f"Modern Çiftler: {cift_sayilar_comp}")

# ADIM 3: IF-ELSE KULLANIMI (Her sayıya bir işlem yap ama şarta göre değişsin)
# Örnek: Çift sayılar kalsın, tek sayılar "Tek" yazılsın.
# Mantık: [SONUC_IF if KOSUL else SONUC_ELSE for DEGISKEN in LISTE]
sonuc = [number if number % 2 == 0 else "Tek" for number in numbers]
print(f"If-Else Sonuç: {sonuc}")

# ---------------------------------------------------------
# GERÇEK HAYAT SENARYOLARI (Real World Examples)
# ---------------------------------------------------------

print("\n--- GERÇEK HAYAT SENARYOLARI ---")

# SENARYO 1: Veri Temizleme (Web Scraping / E-Ticaret)
# İnternetten fiyatlar böyle bozuk geldi diyelim:
fiyatlar_db = ["100TL", "250TL", "50TL", "800TL"]
# Bizim bunları matematiksel işlem yapmak için sayıya çevirmemiz lazım.
temiz_fiyatlar = [int(fiyat.replace("TL", "")) for fiyat in fiyatlar_db]
print(f"1. Temizlenmiş Fiyatlar: {temiz_fiyatlar}")


# SENARYO 2: Dosya İşlemleri (Sadece Resimleri Bulma)
# Bir klasördeki dosya listesi elimizde olsun:
dosyalar = ["resim1.jpg", "veri.json", "profil.png", "notlar.txt", "logo.jpg"]
# Sadece .jpg ve .png olanları alalım:
resimler = [dosya for dosya in dosyalar if dosya.endswith((".jpg", ".png"))]
print(f"2. Bulunan Resimler: {resimler}")


# SENARYO 3: Veritabanından Kullanıcı E-maillerini Çekme (API / Backend)
# Veritabanından gelen kullanıcı listesi (Dictionary listesi gibi düşün):
users = [
    {"id": 1, "name": "Ali", "email": "ali@gmail.com", "active": True},
    {"id": 2, "name": "Ayşe", "email": "ayse@hotmail.com", "active": False},
    {"id": 3, "name": "Mehmet", "email": "mehmet@yahoo.com", "active": True}
]
# Sadece AKTİF olan kullanıcıların E-MAİL adreslerini istiyoruz:
aktif_mailler = [user["email"] for user in users if user["active"] == True]
print(f"3. Aktif Kullanıcı Mailleri: {aktif_mailler}")