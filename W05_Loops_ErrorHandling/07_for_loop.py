# --- Örnek 1: Liste (List) üzerinde gezinme ---
print("--- Örnek 1: Liste üzerinde gezinme ---")
# 'meyveler' adında bir string listesi oluşturuluyor.
meyveler = ["elma", "muz", "çilek", "karpuz"]

# 'for' döngüsü: 'meyveler' listesindeki her bir elemanı sırayla 'meyve' değişkenine atar.
for meyve in meyveler:
    # O anki 'meyve' değişkeninin değerini ekrana yazdırır.
    print(meyve)


# --- Örnek 2: Demet (Tuple) üzerinde gezinme ---
print("\n--- Örnek 2: Demet (Tuple) üzerinde gezinme ---")
# 'sayilar' adında bir integer demeti (tuple) oluşturuluyor.
sayilar = (1, 2, 3, 4, 5)
# 'for' döngüsü: 'sayilar' demetindeki her bir elemanı sırayla 'sayi' değişkenine atar.
for sayi in sayilar:
    # O anki 'sayi' değişkeninin değerini ekrana yazdırır.
    print(sayi)


# --- Örnek 3: Metin (String) üzerinde gezinme ve 'break' ---
print("\n--- Örnek 3: Metin (String) üzerinde gezinme ve 'break' ---")
# 'text' adında bir string değişkeni oluşturuluyor.
text = "Python"
# 'for' döngüsü: 'text' string'indeki her bir karakteri sırayla 'karakter' değişkenine atar.
for karakter in text:
    # O anki 'karakter'i ekrana yazdırır.
    print(karakter)
    # EĞER o anki 'karakter' 'h' harfine eşitse:
    if karakter == "h":
        # 'break' komutu: Döngüyü o anda tamamen durdurur. 'o' ve 'n' harfleri işlenmez.
        print("Döngü 'break' ile durduruldu.")
        break


# --- Örnek 4: Metin (String) üzerinde gezinme ve 'continue' ---
print("\n--- Örnek 4: Metin (String) üzerinde gezinme ve 'continue' ---")
# 'text' değişkeni "Merhaba" olarak güncelleniyor.
text = "Merhaba"
# 'text' string'indeki her bir karakter için döngü başlatılıyor.
for karakter in text:
    # EĞER o anki 'karakter' 'a' harfine eşitse:
    if karakter == "a":
        # 'continue' komutu: Döngünün o anki adımını (iterasyon) atlar.
        # Geri kalan kodları (print) çalıştırmaz ve döngünün başına (bir sonraki karaktere) döner.
        continue
    # (Karakter 'a' değilse) O anki 'karakter'i ekrana yazdırır.
    print(karakter)


# --- Örnek 5: range(), continue ve 'for...else' (Tek Sayıları Bulma) ---
print("\n--- Örnek 5: range(), continue ve 'for...else' ---")
# Kullanıcıdan bir sayı alınıyor ve 'int' (tam sayı) tipine dönüştürülüyor.
number=int(input("Bir sayı giriniz (Örnek 5 için): "))
# 'for' döngüsü: 0'dan 'number'a kadar (number dahil değil) bir sayı dizisi (range) oluşturur.
for i in range(number):
    # EĞER 'i' sayısının 2'ye bölümünden kalan 0 ise (yani sayı çiftse):
    if(i%2==0):
        # 'continue': Bu adımı atla ve bir sonraki 'i' sayısına geç.
        continue
    # (Eğer 'if' koşulu sağlanmazsa, yani sayı tekse) Bu satır çalışır.
    print(f"{i} tek sayıdır.")
# 'for-else' bloğu: 'for' döngüsü 'break' komutu ile kesilmeden, 
# normal bir şekilde tamamlandığında bu 'else' bloğu çalışır.
else:
    print("Döngü (Örnek 5) tamamlandı.")


# --- Örnek 6: 'pass' komutu kullanımı ve 'for...else' ---
print("\n--- Örnek 6: 'pass' komutu kullanımı ---")
# 0'dan 5'e kadar (5 dahil değil) bir döngü başlatılıyor.
for i in range(5):
    # EĞER sayı çiftse:
    if i%2==0:
        # 'pass': "Hiçbir şey yapma" anlamına gelen bir yer tutucudur.
        # Python burada girintili bir kod bekler, 'pass' ile bu sözdizimi kuralı sağlanır.
        pass
    # EĞER 'if' koşulu sağlanmazsa (yani sayı tekse):
    else:
        print(f"{i} tek sayıdır.")
# 'for' döngüsü normal bir şekilde tamamlandığında çalışır.
else:
    print("2 ye bölünen sayılar için işlem yapılmadı (Örnek 6).")


# --- Örnek 7: İç içe döngüler (Kombinasyonlar) ---
print("\n--- Örnek 7: İç içe döngüler ---")
# İki ayrı liste tanımlanıyor.
sıfatlar = ["büyük", "küçük", "tatlı"]
isimler = ["kedi", "köpek", "kuş"]

# Dış döngü: Her bir sıfat için çalışır.
for f in sıfatlar:
    # İç döngü: Dış döngünün HER BİR adımı için, içteki liste (isimler) tamamen baştan sona döner.
    for g in isimler:
        # O anki dış döngü elemanını (f) ve iç döngü elemanını (g) birleştirip yazdırır.
        print(f"{f} {g}")


# --- Örnek 8: İç içe listeleri döngüyle ayrıştırma (Unpacking) ---
print("\n--- Örnek 8: İç içe listeleri ayrıştırma ---")
# Listelerin içinde listeler (nested list) tanımlanıyor.
# Her iç liste 2 elemanlı.
sayilarim=[
    [1,2],
    [4,5],
    [7,8]
    ]

# "Unpacking" (Ayrıştırma) kullanarak döngü:
# İç listenin 2 elemanı olduğu için, bunlar sırayla 'item1' ve 'item2' değişkenlerine atanır.
for item1,item2 in sayilarim:
    # Atanan değişkenler ekrana yazdırılır.
    print(f"{item1} ve {item2}")


# --- Örnek 9: Sözlük (Dictionary) üzerinde .items() ile gezinme ---
print("\n--- Örnek 9: Sözlük (Dictionary) üzerinde .items() ile gezinme ---")
# 'kullanici_bilgileri' adında bir sözlük (dictionary) oluşturuluyor.
kullanici_bilgileri = {
    'isim': 'Ahmet',
     'yas': 30,
    'meslek': 'Mühendis'
}

# '.items()' metodu, sözlükteki her bir (anahtar, değer) çiftini bir demet (tuple) olarak döndürür.
# Python bu demeti otomatik olarak 'anahtar' ve 'deger' değişkenlerine "ayrıştırır" (unpacking).
for anahtar, deger in kullanici_bilgileri.items():
    # O anki anahtar ve değeri biçimlendirilmiş bir string (f-string) olarak ekrana yazdırır.
    print(f"{anahtar}: {deger}")


# --- Örnek 10: enumerate() fonksiyonu ile (indeks + değer) alma ---
print("\n--- Örnek 10: enumerate() ile (indeks + değer) alma ---")
# 'meyveler' adında yeni bir liste oluşturuluyor.
meyveler_enum = ["elma", "muz", "çilek"]

# 'enumerate()' fonksiyonu, listeyi (0, "elma"), (1, "muz"), (2, "çilek")
# gibi (indeks, değer) çiftlerine dönüştürür.
# Bu çiftler 'indeks' ve 'meyve' değişkenlerine otomatik olarak "ayrıştırılır" (unpacking).
for indeks, meyve in enumerate(meyveler_enum):
    # O anki indeksi ve o indekse karşılık gelen meyveyi ekrana yazdırır.
    print(f"{indeks}. index = {meyve}")


# --- Örnek 11: zip() fonksiyonu ile birden fazla listeyi birleştirme ---
print("\n--- Örnek 11: zip() fonksiyonu ile birden fazla listeyi birleştirme ---")
# Birbiriyle ilişkili, ancak ayrı olan iki liste tanımlanıyor.
ogrenciler = ["Ali", "Veli", "Ayşe"]
notlar = [80, 92, 75]

# 'zip()' fonksiyonu, 'ogrenciler' ve 'notlar' listelerini "fermuarlar".
# İlk listeden 0. elemanı, ikinci listeden 0. elemanı alır ve bir grup (demet) yapar: ('Ali', 80)
# Sonra 1. elemanları alır: ('Veli', 92) ...
# 'for' döngüsü bu çiftleri sırayla alır ve 'ogrenci', 'notu' değişkenlerine ayrıştırır.
for ogrenci, notu in zip(ogrenciler, notlar):
    # O anki eşleşen öğrenci ve notu ekrana yazdırır.
    print(f"{ogrenci} adlı öğrencinin notu: {notu}")

# --- Örnek 12: List Comprehension (Liste Anlayışı) ---
# Bu, 'for' döngüsü mantığını kullanarak tek satırda yeni bir liste oluşturma yöntemidir.
print("\n--- Örnek 12: List Comprehension (Tek satırda 'for' döngüsü) ---")

# Amaç: 0'dan 9'a kadar olan ÇİFT sayıların KARELERİNİ içeren bir liste oluşturmak.

# Yöntem 1: Standart 'for' döngüsü
print("Yöntem 1: Standart 'for' döngüsü")
standart_liste = [] # Boş bir liste ile başla
# 0'dan 9'a kadar olan sayılar için döngüye gir
for i in range(10):
    # Eğer sayı çiftse (2'ye bölümünden kalan 0 ise)
    if i % 2 == 0:
        # Sayının karesini (i * i) listeye ekle (.append)
        standart_liste.append(i * i)
print(standart_liste)

# Yöntem 2: List Comprehension (Aynı işlemin 'Pythonic' yolu)
print("Yöntem 2: List Comprehension (Pythonic Yol)")
# Sözdizimi: [ (yapılacak_işlem) (döngü) (koşul) ]
comprehension_liste = [i * i for i in range(10) if i % 2 == 0]
print(comprehension_liste)