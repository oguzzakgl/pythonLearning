# Konu: Lambda Fonksiyonu Örnekleri
# Amaç: Lambda fonksiyonlarının normal fonksiyonlarla karşılaştırılması ve map/filter ile kullanımı.

def topla(a,b):
    return a+b
print(topla(5, 9) )


toplama = lambda x,y: x+y
print(topla(5, 2))

#------------------

def carpma(j,k,l):
    return j*k*l
print(carpma(1,2,3))

carpim = lambda u,ı,o: u*ı*o
print(carpim(2,3,4))

#------------------

def ters(x):
    return x[::-1]

print(ters("ali"))

terscevir= lambda x: x[::-1]
print(terscevir("bora"))


#------------------
def karesinial(x):
    return x**2

# --- YÖNTEM 1: Geleneksel 'for' Döngüsü (Yerinde Değiştirme) ---
print("\n--- YÖNTEM 1: 'for' Döngüsü ---")

# 1. 1'den 5'e kadar olan sayılardan bir liste oluştur (yani [1, 2, 3, 4, 5])
sayilar = [*range(1,6)]
print(f"Döngü Başlamadan Önce (Orijinal): {sayilar}")

# 2. 'sayilar' listesinin uzunluğu kadar (5 kez) dönecek bir döngü başlat.
# 'index' değişkeni sırayla 0, 1, 2, 3, 4 değerlerini alacak.
for index in range(len(sayilar)):
    # 3. 'sayilar[index]' kullanarak listedeki o anki elemana (örn: sayilar[0] -> 1) eriş.
    # 4. Bu elemanı 'karesinial' fonksiyonuna gönder (örn: karesinial(1) -> 1).
    # 5. Dönen sonucu (1), tekrar 'sayilar[index]'in (eski değerin) üzerine yaz.
    #
    #    !!! DİKKAT: Bu işlem ORİJİNAL listeyi kalıcı olarak değiştirir !!!
    #
    sayilar[index] = karesinial(sayilar[index])

# 6. Döngü bittiğinde, listenin değişmiş son halini yazdır.
print(f"Döngü Bittikten Sonra (Değişmiş): {sayilar}")


# --- YÖNTEM 2: 'map()' Fonksiyonu (Fonksiyonel Yaklaşım) ---
print("\n--- YÖNTEM 2: 'map()' Fonksiyonu ---")

# 1. 1'den 5'e kadar olan sayılardan yeni bir liste oluştur ([1, 2, 3, 4, 5])
sayilar = [*range(1,6)]

# 2. 'map()' fonksiyonunu çağır:
#    - İlk parametre olarak 'karesinial' (hangi fonksiyonun uygulanacağı).
#    - İkinci parametre olarak 'sayilar' (hangi listenin üzerinde çalışılacağı).
# 3. 'map', 'sayilar' listesindeki HER BİR elemanı 'karesinial' fonksiyonuna yollar.
# 4. 'list()' fonksiyonu, 'map' objesinden dönen tüm sonuçları toplayıp YENİ bir liste yapar.
#    (Orijinal 'sayilar' listesi HİÇ DEĞİŞMEZ).
yeni_liste_map = list(map(karesinial, sayilar))

# 5. Orijinal listenin değişmediğini gösterir.
print(f"Orijinal Liste (Değişmedi): {sayilar}")
# 6. 'map' ile oluşturulan yeni listeyi gösterir.
print(f"Map ile Oluşan Yeni Liste: {yeni_liste_map}")


# --- YÖNTEM 3: List Comprehension (En Pythonik/Kısa Yöntem) ---
print("\n--- YÖNTEM 3: List Comprehension ---")

# 1. 1'den 5'e kadar olan sayılardan yeni bir liste oluştur ([1, 2, 3, 4, 5])
sayilar_comp = [*range(1,6)]

# 2. Bu satır, Yöntem 2'nin (map) yaptığı işin aynısını çok daha kısa yazar.
#    Okunuşu: "[ (her 's' için 'karesinial(s)' işlemini yap) (neredeki 's' ler? -> 'sayilar_comp' içindeki) ]"
# 3. 'sayilar_comp' içindeki her bir 's' elemanını alır, 'karesinial'a yollar
#    ve dönen sonuçlardan anında YENİ bir liste oluşturur.
#    (Orijinal 'sayilar_comp' listesi HİÇ DEĞİŞMEZ).
yeni_liste_comp = [karesinial(s) for s in sayilar_comp]

# 4. Orijinal listenin değişmediğini gösterir.
print(f"Orijinal Liste (Değişmedi): {sayilar_comp}")
# 5. List comprehension ile oluşturulan yeni listeyi gösterir.
print(f"List Comp. ile Oluşan Yeni Liste: {yeni_liste_comp}")