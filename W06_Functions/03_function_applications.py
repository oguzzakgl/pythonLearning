# Konu: Fonksiyon Uygulamaları
# Amaç: Fonksiyon tanımlama, parametre kullanımı, asal sayı ve tam bölen bulma örnekleri.

# yazdir fonksiyonu, aldığı 'kelime' string'ini, aldığı 'adet' sayısı kadar ekrana yazdırır.
def yazdir(kelime, adet):
    # String çarpma operatörü kullanılarak kelimeyi çoğaltır.
    # '\n' karakteri her tekrardan sonra alt satıra geçmeyi sağlar.
    print(kelime * adet)

# Fonksiyon çağrılır: 'merhaba\n' 10 kez yazdırılır.
yazdir('merhaba\n', 10)


# ---
# listeyeCevir fonksiyonu, *params (esnek konumsal argümanlar) kullanarak
# fonksiyona gönderilen tüm değerleri bir listeye dönüştürür.
def listeyeCevir(*params):
    # Boş bir liste oluşturulur.
    liste = []

    # *params tarafından yakalanan tuple (demet) üzerindeki her bir öğe için döngü yapılır.
    for param in params:
        # Her öğe listeye eklenir.
        liste.append(param)
    
    # Oluşturulan liste geri döndürülür.
    return liste

# Fonksiyon çağrılır ve farklı tiplerdeki argümanlar bir liste olarak döndürülür.
result = listeyeCevir(10, 20, 30, 40,'merhaba')

# Sonuç listesi ekrana basılır. (Çıktı: [10, 20, 30, 40, 'merhaba'])
print(result)

# ---
# asalSayiBul fonksiyonu, verilen iki sayı arasındaki (dahil) asal sayıları bulur.
def asalSayiBul(sayi1, sayi2):
    # sayi1'den sayi2'ye kadar olan her bir sayı için döngü başlatılır.
    for sayi in range(sayi1, sayi2+1):
        # Asal sayı tanımı gereği, sayının 1'den büyük olup olmadığı kontrol edilir.
        if sayi > 1:
            # 2'den başlayıp sayının kendisine kadar olan sayılarla bölünebilirlik kontrol edilir.
            for i in range(2, sayi):
                # Eğer sayı, i'ye kalansız bölünebiliyorsa asal değildir.
                if sayi % i == 0 :
                    break # İç döngüden çıkılır.
            # else: İç döngü "break" ile kesilmediyse (yani bölünebilen bir sayı bulunamadıysa),
            # sayı asaldır ve ekrana basılır.
            else:
                print(sayi)

# Kullanıcıdan aralık için başlangıç ve bitiş sayıları alınır.
sayi1 = int(input('sayi 1: '))
sayi2 = int(input('sayi 2: '))

# Fonksiyon, alınan aralık ile çağrılır ve asal sayılar ekrana basılır.
# Örn: (sayi 1: 10, sayi 2: 20 girilirse, Çıktı: 11, 13, 17, 19)
asalSayiBul(sayi1, sayi2)

# ---
# tamBolenleriBul fonksiyonu, kendisine verilen sayının 2'den başlayarak tam bölenlerini bulur.
def tamBolenleriBul(sayi):
    # Bulunan tam bölenlerin ekleneceği boş bir liste oluşturulur.
    tamBolenler = []

    # 2'den başlayarak sayının bir eksiğine kadar döngü yapılır. (1 ve sayının kendisi dahil edilmez)
    for i in range(2, sayi):
        # Eğer i, sayıyı kalansız bölüyorsa (tam bölüyorsa)...
        if sayi % i == 0:
            # ... i, tam bölenler listesine eklenir.
            tamBolenler.append(i)
    # Tam bölenler listesi geri döndürülür.
    return tamBolenler

# Fonksiyon 20 argümanı ile çağrılır ve tam bölenler ekrana basılır.
# (Çıktı: [2, 4, 5, 10])
print(tamBolenleriBul(20))