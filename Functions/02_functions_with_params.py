# Konu: Parametreli Fonksiyonlar
# Amaç: Fonksiyonlarda parametre kullanımı, varsayılan değerler, *args ve **kwargs.

# Fonksiyonlar, programlamanın temel yapı taşlarıdır ve belirli bir görevi yerine getirmek
# üzere tasarlanmış kod bloklarıdır.

# Fonksiyonları kullanmanın temel amacı ve faydaları:
# 1. Tekrar Kullanılabilirlik (Reusability): Bir görevi bir kez tanımlayıp defalarca çağırabiliriz.
# 2. Modülerlik: Kodu küçük, yönetilebilir parçalara ayırır.
# 3. Bakım Kolaylığı: Koddaki değişiklikler tek bir yerde yapılır.

# Bir fonksiyon genellikle:
# - Girdi (Argümanlar): Üzerinde çalışacağı veriyi alır.
# - İşlem: Tanımlanan görevi yerine getirir.
# - Çıktı (Return): İşlem sonucunda bir değeri geri gönderebilir.
# -----------------------------

# changeName fonksiyonu, immutable (değişmez) tip olan string'lerin
# fonksiyonda değiştirilmesinin orijinal değeri etkilemediğini gösterir.
def changeName(n):
    # Fonksiyon içinde 'n' değişkenine yeni bir referans atanır ('ada').
    # Orijinal 'name' değişkeni hala 'yiğit' nesnesine referans eder.
    n = 'ada'

name = 'yiğit'

changeName(name)
# Çıktı 'yiğit' olacaktır, çünkü string değişmezdir.
print(name)


# change fonksiyonu (şu an yorum satırında), mutable (değişebilir) tiplerin
# (liste gibi) fonksiyonda nasıl değişebileceğini gösterir.
def change(n): 
    # n, orijinal listenin referansını taşır. Bu satırda orijinal liste değişir.
    n[0] = 'istanbul'

sehirler = ['ankara', 'izmir']
# 'sehirler[:]' ile sığ kopyalama yapılır. 'n' ve 'sehirler' artık farklı listelerdir.
n = sehirler[:]
# Değişiklik sadece 'n' listesini etkiler.
n[0] = 'istanbul' 
# 'sehirler' listesi kopyalandığı için değişmeden kalır.
print(sehirler)
# 'n' listesi değiştirilmiş haliyle basılır.
print(n)
# change(sehirler) # Bu satır açılsaydı, 'sehirler' listesi ['istanbul', 'izmir'] olacaktı.
# print(sehirler)

# 'add' fonksiyonu, varsayılan (default) parametre kullanımını gösterir.
def add(a, b, c = 0):
    # sum() yerleşik fonksiyonu ile argümanlar toplanır.
    return sum((a,b,c)) 

# 'c' için 30 değeri kullanılır.
print(add(10, 20,30))
# 'c' argümanı atlandığı için varsayılan değer olan 0 kullanılır.
print(add(10, 20))

# 'add2' fonksiyonu, *args (esnek konumsal argümanlar) kullanımını gösterir.
def add2(*params):
    # *args, gönderilen tüm konumsal argümanları bir tuple (demet) olarak yakalar.
    print(type(params)) 
    print(params)
    return sum(params)

# Farklı sayıda argümanla fonksiyon çağrılır.
print(add2(10, 20,30))
print(add2(10, 20))
print(add2(10, 20 ,34,34,124,54,652,3)) # Çok sayıda argüman gönderimi

# 'displayUser' fonksiyonu, **kwargs (esnek anahtar kelime argümanları) kullanımını gösterir.
def displayUser(**args):
    # **kwargs, gönderilen tüm anahtar=değer argümanlarını bir dictionary (sözlük) olarak yakalar.
    print(type(args)) 
    # Sözlük içindeki anahtar-değer çiftleri üzerinde döngü yapılır.
    for key, value in args.items():
        print('{} is {}'.format(key,value))

# Farklı anahtar=değer çiftleri ile fonksiyon çağrılır.
displayUser(name= 'Cınar', age = 2, city = 'istanbul')
displayUser(name= 'ada', age = 12, city = 'izmir')
displayUser(name= 'ege', age = 23, city = 'bursa')


# 'myFunc' fonksiyonu, tüm argüman tiplerinin (zorunlu, *args, **kwargs) sırasını gösterir.
# Bu sıra zorunludur: Zorunlu argümanlar -> *args -> **kwargs
def myFunc(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

# Argümanların fonksiyona atanma sırası: a=10, b=20, args=(30, 40, 50), kwargs={'key1':..., 'key2':...}
myFunc(10, 20, 30, 40, 50, key1 = 'value 1', key2 = ' valdue 2')