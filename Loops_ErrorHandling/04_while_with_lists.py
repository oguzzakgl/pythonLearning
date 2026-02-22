# Konu: Listelerle While Döngüsü Kullanımı
# Amaç: While döngüsü ile liste elemanlarına erişim ve liste üzerinde işlemler.

# 1'den 10'a kadar sayıları içeren bir liste oluşturuluyor.
myNumbers=[1,2,3,4,5,6,7,8,9,10]

# Döngü için bir sayaç (ve aynı zamanda liste indeksi) değişkeni başlatılıyor.
i=0
# Döngü, 'i' değişkeni listenin toplam eleman sayısından (len(myNumbers)) küçük olduğu sürece çalışır.
while i<len(myNumbers):
    # Listenin 'i' indeksindeki elemanı ekrana yazdırır.
    print(myNumbers[i])
    # Sayacı 1 artırır, böylece bir sonraki elemana geçilir.
    i+=1

# Meyve isimlerini içeren bir liste (string) oluşturuluyor.
fruits = ["elma", "muz", "çilek", "portakal"]
# Döngü için 'a' adında bir sayaç başlatılıyor.
a=0
# HATA: Döngü koşulu 'a' yerine 'i' değişkenini kontrol ediyor.
# 'i' bir önceki kod bloğundan kaldığı için değeri 10'dur.
# len(fruits) 4 olduğu için (10 < 4) koşulu 'Yanlış' (False) olur ve döngü HİÇ ÇALIŞMAZ.
while a < len(fruits):
    # Döngü çalışsaydı, 'i' indeksindeki elemanı yazdıracaktı.
    print(fruits[a])
    # Döngü çalışsaydı, 'i' değişkenini 1 artıracaktı.
    a += 1
# NOT: Bu bloğun çalışması için 'a=0' yerine 'i=0' yazılmalı ve döngü içinde 'i' kullanılmalı
# veya 'a=0' korunup döngüde 'a' kullanılmalıdır (while a < len(fruits): ... a += 1).

# Sayıları saklamak için boş bir liste oluşturuluyor.
numbers=[]
# İlk 'while' döngüsü (veri girişi için) sayaç değişkeni 'i' başlatılıyor.
i=0
# Döngü 7 kez çalışacak şekilde ayarlanıyor (i=0'dan 6'ya kadar).
while(i<7):
    # Kullanıcıdan bir sayı girmesi isteniyor ve gelen değer 'int' (tam sayı) tipine dönüştürülüyor.
    num=int(input("Bir sayı girin: "))
    # Alınan tam sayı, 'numbers' listesinin sonuna ekleniyor (.append).
    numbers.append(num)
    # Giriş döngüsünün sayacı 1 artırılıyor.
    i+=1

# 'numbers' listesindeki elemanlar küçükten büyüğe doğru sıralanıyor.
numbers.sort()

# İkinci 'while' döngüsü (veri yazdırma için) sayaç değişkeni 'x' başlatılıyor.
x=0
# Döngü 7 kez çalışacak şekilde ayarlanıyor (x=0'dan 6'ya kadar).
while(x<7):
    # Listenin 'x' indeksindeki elemanı yazdırır.
    # 'end=" "' parametresi, print fonksiyonunun satır sonuna
    # 'yeni satır' (\n) yerine 'boşluk' koymasını sağlar.
    print(numbers[x],end=" ")
    # Yazdırma döngüsünün sayacı 1 artırılıyor.
    x+=1