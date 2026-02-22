# Konu: Fonksiyonlar Özeti
# Amaç: Fonksiyon tanımlama, parametreler, return, global/local değişkenler ve lambda fonksiyonlarının özeti.

# fonksiyonlar 
# Bir fonksiyonu def (define - tanımla) anahtar kelimesiyle oluştururuz.
# yazdıgımız fonksiyonu kullanmak icinde ismini yazarız ve sonuna () koyariz

# 1. Tanımlama (Bu kod, çağrılana kadar çalışmaz)
def selamla():
    """
    Bu fonksiyon ekrana "Merhaba!" yazar. (Bu bir docstring - açıklama satırıdır)
    """
    print("Merhaba, fonksiyona hoş geldiniz!")
    print("---------------------------------")

# 2. Çağırma (Fonksiyonu adıyla çalıştırıyoruz)
print("Program başladı.")
selamla()  # 'selamla' fonksiyonunun içindeki kodlar şimdi çalışır
selamla()  # İstediğimiz kadar tekrar çağırabiliriz
print("Program bitti.")

# Çıktı:
# Program başladı.
# Merhaba, fonksiyona hoş geldiniz!
# ---------------------------------
# Merhaba, fonksiyona hoş geldiniz!
# ---------------------------------
# Program bitti.

print("---------------------------------")

# parametreli fonksiyonlar

# Fonksiyonları daha kullanışlı hale getirmek için onlara dışarıdan veri (bilgi) gönderebiliriz.

# Parametre: Fonksiyonu tanımlarken parantez içine yazdığımız değişken adıdır (Örn: isim).

# Argüman: Fonksiyonu çağırırken parantez içine yazdığımız gerçek değerdir (Örn: "Ahmet").

# 'kullanici_adi' ve 'yas' burada BİRER PARAMETRE'dir.
def kisi_tanit(kullanici_adi, yas):
    print(f"Ad: {kullanici_adi}")
    print(f"Yaş: {yas}")
    print("---")

# '"Ali"' ve 30 burada BİRER ARGÜMAN'dır.
kisi_tanit("Ali", 30)

# '"Veli"' ve 45 burada BİRER ARGÜMAN'dır.
kisi_tanit("Veli", 45)

# değer dondurme

# Fonksiyonlar sadece print yapmak zorunda değildir. 
# Bir hesaplama yapıp, sonucu geri döndürebilirler. 
# Bu, fonksiyonun ürettiği değeri bir değişkende saklamamızı sağlar.

#return kelimesi fonksiyonu anında sonlandırır ve belirttiğiniz 
# değeri dışarıya (çağrıldığı yere) gönderir.

def topla(sayi1, sayi2):
    toplam = sayi1 + sayi2
    return toplam
    # 'return' sonrası yazılan kodlar ÇALIŞMAZ

# Fonksiyondan dönen değeri 'sonuc' değişkenine atadık
sonuc = topla(10, 20)

print(f"İşlemin sonucu: {sonuc}") # Çıktı: 30
print(f"50 ve 90'ın toplamı: {topla(50, 90)}") # Çıktı: 140

print("---------------------------------")

# global ve local degiskenler

# Local (Yerel) Değişken: Bir fonksiyonun içinde tanımlanan değişkendir. 
# Sadece o fonksiyon içinde yaşar ve dışarıdan erişilemez. 
# Fonksiyon bittiğinde hafızadan silinir.

# Global (Küresel) Değişken: Fonksiyonların dışında (ana kod gövdesinde) 
# tanımlanan değişkendir. Her yerden (tüm fonksiyonların içinden) okunabilir.


global_degisken = "Ben Globalim" # Bu GLOBAL

def benim_fonksiyonum():
    local_degisken = "Ben Localim" # Bu LOCAL
    
    print(f"Fonksiyon içinden local: {local_degisken}")
    print(f"Fonksiyon içinden global: {global_degisken}") # Global'i okuyabiliriz

# 1. Fonksiyonu çağıralım
benim_fonksiyonum()
# Çıktı:
# Fonksiyon içinden local: Ben Localim
# Fonksiyon içinden global: Ben Globalim

# 2. Dışarıdan değişkenlere erişelim
print(f"Dışarıdan global: {global_degisken}") # Çıktı: Dışarıdan global: Ben Globalim
# print(f"Dışarıdan local: {local_degisken}") # HATA! NameError: name 'local_degisken' is not defined

print("---------------------------------")

# lambda fonksiyonu 

# Lambda, isimsiz, tek satırlık küçük fonksiyonlar oluşturmanın hızlı bir yoludur. 
# Genellikle başka bir fonksiyonun (örn: map, filter, sort) 
# içine parametre olarak verilir.

# def kullanmak yerine lambda kelimesini kullanırız.


# Normal Fonksiyon Yolu
def karesini_al(x):
    return x * x
print(f"Normal fonksiyon: {karesini_al(5)}") # Çıktı: 25


# Lambda Fonksiyon Yolu
# lambda parametre(ler) : yapılacak_işlem (return)
karesini_al_lambda = lambda x: x * x
print(f"Lambda fonksiyon: {karesini_al_lambda(5)}") # Çıktı: 25

# En yaygın kullanımı (örn: listeyi sıralarken)
sayilar = [(1, 5), (3, 2), (5, 10)]
# Listeyi, her elemanın 1. indeksine (5, 2, 10) göre sırala
sayilar.sort(key=lambda item: item[1])
print(f"Sıralanmış liste: {sayilar}") # Çıktı: [(3, 2), (1, 5), (5, 10)]