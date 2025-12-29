# Konu: Dictionary (Sözlük) Temelleri
# Amaç: Sözlük oluşturma, veri ekleme, güncelleme ve hata yönetimi ile veri çekme.

# Tüm öğrencilerin bilgilerini saklamak için 'ogrenciler' adında boş bir sözlük (dictionary) oluşturuyoruz.
ogrenciler = {}

print("--- Yeni Öğrenci Ekleme ---")
# Kullanıcıdan eklenecek öğrencinin bilgilerini 'input()' fonksiyonu ile alıyoruz.
number = input("Ogrenci no: ")
name = input("Ogrenci adı: ")
surname = input("Ogrenci soyadı: ")
phone = input("Telefon: ")

# 'update()' metodu ile 'number' anahtarı altına öğrencinin bilgilerini
# içeren yeni bir iç sözlük ekliyoruz.
ogrenciler.update({ 
    number: {
        'ad': name,
        'soyad': surname,
        'telefon': phone,
    }
})

# Sözlüğün güncel halini ekrana yazdırıyoruz.
print("Sözlüğün güncel hali:", ogrenciler)
print("--------------------") # Ayraç


print("--- Öğrenci Arama (Güvenli) ---")
# Kullanıcıdan, bilgilerini görmek istediği öğrencinin numarasını istiyoruz.
ogrNo = input('Aranacak ogrenci no: ')


# HATA YÖNETİMİ BAŞLANGICI
try:
    # DENE: 'ogrNo' anahtarını kullanarak sözlükten öğrenci bilgilerini almayı dene.
    # EĞER 'ogrNo' anahtarı sözlükte VARSA, 'ogrenci' değişkenine atanır.
    ogrenci = ogrenciler[ogrNo]
    
    # EĞER 'ogrenci' başarıyla alındıysa (yani üst satır hata vermediyse):
    # Bilgileri f-string ile formatlayıp ekrana yazdırıyoruz.
    print(f"Aradıgınız {ogrNo} nolu öğrencinin adı: {ogrenci['ad']}, soyadı: {ogrenci['soyad']}, telefonu: {ogrenci['telefon']}")

except KeyError:
    # YAKALA: Eğer 'try' bloğu bir 'KeyError' fırlatırsa (yani 'ogrNo' anahtarı sözlükte YOKSA):
    # Program çökmez, bunun yerine bu blok çalışır.
    # Kullanıcıya aradığı numaranın bulunamadığını belirten bir mesaj gösterilir.
    print(f"HATA: {ogrNo} numaralı öğrenci sistemde bulunamadı.")
# HATA YÖNETİMİ BİTİŞİ

print("--------------------")
print("Program başarıyla tamamlandı.")