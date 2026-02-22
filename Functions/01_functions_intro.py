# Konu: Fonksiyon Temelleri
# Amaç: Fonksiyon tanımlama, argüman gönderme, return değeri ve docstring kullanımı.

# 'sayHello' adında bir fonksiyon tanımlanıyor.
# Bu fonksiyon, parametre olarak aldığı ismi (name) ekrana basar.
def sayHello(name):
    print(f"Hello, {name}!")

# Kullanıcıdan klavye aracılığıyla ismini girmesi istenir.
name = input("Enter your name: ")
# Tanımlanan fonksiyon, kullanıcıdan alınan isim ile çağrılır.
sayHello(name)

# 'total' adında, iki sayıyı toplayıp sonucu döndüren bir fonksiyon tanımlanıyor.
def total(num1, num2):
    return num1 + num2 # Toplama işleminin sonucu geri döndürülür.

# Fonksiyon 5 ve 10 argümanları ile çağrılır ve dönen değer 'result' değişkenine atanır.
result = total(5, 10)
# Toplama işleminin sonucu ekrana basılır.
print(f"Total: {result}")


# 'yasHesapla' adında, doğum yılına göre yaşı hesaplayan bir fonksiyon tanımlanıyor.
# Hesaplama, 2025 yılını baz almaktadır.
def yasHesapla(dogumYili):
    return 2025 - dogumYili # Yaş hesaplanıp geri döndürülür.

# Fonksiyon 1990 argümanı ile çağrılır ve dönen değer 'yas' değişkenine atanır.
yas = yasHesapla(1990)
# Hesaplanan yaş değeri ekrana basılır.
print(f"Yaşınız: {yas}")

# 'emeklilikHesapla' adında, doğum yılı ve isim kullanarak emekliliğe kalan süreyi hesaplayan bir fonksiyon tanımlanıyor.
def emeklilikHesapla(dogumYili, isim):
    '''
    DOCSTRİNG: doğum yılına göre emeklilik süresini hesaplar
    INPUT: dogumYili (int), isim (str)
    OUTPUT: kalanSure (int)
    '''
    # Hesaplanan yaşı almak için 'yasHesapla' fonksiyonu çağrılır.
    yas = yasHesapla(dogumYili)
    # Emeklilik yaşı (65) ile mevcut yaş arasındaki fark hesaplanır.
    kalanSure = 65 - yas
    
    # Kalan süre 0'dan büyükse (emekli olmamışsa)
    if kalanSure > 0:
        print(f"{isim}, emekliliğinize {kalanSure} yıl kaldı.")
    # Kalan süre 0 veya daha azsa (zaten emekli olmuşsa)
    else:
        print(f"{isim}, zaten emekli oldunuz.")

# Fonksiyon, 1990 ve "Ahmet" argümanları ile çağrılır (Çıktı: 30 yıl kaldı).
emeklilikHesapla(1990, "Ahmet")

# 'emeklilikHesapla' fonksiyonunun DOCSTRING içeriğini ve yardım bilgisini ekrana basar.
print(help(emeklilikHesapla))

# 1'den 5'e kadar sayıları içeren bir liste oluşturulur.
list = [1, 2, 3, 4, 5]

# Python'ın yerleşik liste metodu olan 'append'in yardım dokümantasyonunu ekrana basar.
print(help(list.append))