# Konu: While Döngüsü Temelleri
# Amaç: While döngüsünün yapısı, sonsuz döngüler, break/continue ve else kullanımı.

# Python'da 'while' döngüsü, belirli bir KOŞUL 'True' (Doğru) olduğu sürece
# kendi kod bloğu (girintili alanı) içindeki işlemleri tekrar tekrar
# çalıştırmak için kullanılır.
#
# Bir 'if' (eğer) koşulu sadece BİR KEZ kontrol edilir ve çalışır.
# Bir 'while' (olduğu sürece) koşulu ise, kod bloğu her bittiğinde
# TEKRAR kontrol edilir. Koşul 'True' olmaya devam ettiği sürece
# döngü de devam eder.
#
# Döngünün durması için, koşulun bir noktada 'False' (Yanlış) olması gerekir.

# --- 2. 'while' Döngüsünün Temel Yapısı ---
#
# Genellikle 3 ana bölümden oluşur:
#
# 1. Başlatıcı Değişken: Döngü koşulunun kontrol edeceği değerin
#    ilk halini tanımlarız.
#    (Örn: sayac = 0)
#
# 2. Koşul İfadesi: 'while' anahtar kelimesinden sonra gelen,
#    'True' veya 'False' sonucu üreten ifadedir.
#    (Örn: while sayac < 5:)
#
# 3. Güncelleyici (Çok Önemli!): Döngü bloğunun içinde,
#    başlatıcı değişkeni değiştiren ve koşulun bir noktada 'False'
#    olmasını sağlayan koddur.
#    (Örn: sayac += 1)

# --- 3. DİKKAT: Sonsuz Döngü (Infinite Loop) ---
#
# Eğer döngü içindeki "Güncelleyici" (3. Adım) unutulursa veya
# koşul her zaman 'True' kalacak şekilde ayarlanırsa, döngü
# ASLA durmaz. Buna "Sonsuz Döngü" denir ve programın kilitlenmesine
# neden olur.
#
# (Örn: sayac = 0 -> while sayac < 5: -> print(sayac))
# Burada 'sayac' hep 0 kalacağı için (0 < 5 her zaman True'dur)
# program sonsuza kadar 0 yazdırır.


# --- 4. Kod Örnekleri ---

print("=" * 40)
print("--- Örnek 1: Basit Sayıcı Döngüsü (1'den 5'e kadar) ---")
print("=" * 40)

# 1. Başlatıcı Değişken
sayac = 1

# 2. Koşul ("sayac", 5'ten küçük veya 5'e eşit olduğu sürece)
while sayac <= 5:
    
    # --- Döngü Bloğu Başlangıcı ---
    
    print(f"Sayaç şu anda: {sayac}")
    
    # 3. Güncelleyici (KRİTİK ADIM)
    # Sayacı 1 artırıyoruz.
    # Eğer bu satır olmasaydı, 'sayac' hep 1 kalırdı ve bu bir
    # sonsuz döngü olurdu.
    sayac += 1 # Bu 'sayac = sayac + 1' demektir.
    
    # Döngü bloğu bitti, 'while' satırına geri dönülür.
    # sayac = 2 oldu -> 2 <= 5 mi? True. Tekrar çalış.
    # ...
    # sayac = 5 oldu -> 5 <= 5 mi? True. Tekrar çalış.
    # ...
    # sayac = 6 oldu -> 6 <= 5 mi? False. Döngü biter.

print(f"Döngü bitti. Sayacın son değeri: {sayac}")


print("\n" + "=" * 40)
print("--- Örnek 2: 'while True' ve 'break' (Döngüyü Kırma) ---")
print("=" * 40)

# 'while True:' ifadesi, Python'a "bilerek sonsuz bir döngü başlat" demektir.
# Koşul her zaman 'True'dur.
# Bu döngüden çıkmanın tek yolu 'break' anahtar kelimesidir.
# 'break', içinde bulunduğu döngüyü o an terk eder (kırar).

print("Çıkmak için 'çıkış' veya 'q' yazınız.")

while True:
    kullanici_girisi = input("Lütfen bir kelime giriniz: ")
    
    # Girilen metni küçük harfe çevirip kontrol ediyoruz
    if kullanici_girisi.lower() == 'çıkış' or kullanici_girisi.lower() == 'q':
        # Eğer kullanıcı 'çıkış' veya 'q' yazdıysa...
        print("Çıkış komutu algılandı. Döngü sonlandırılıyor...")
        break # 'break' komutu bu 'while True' döngüsünü KIRAR.
    
    # 'break' çalışmazsa, döngü normal devam eder
    print(f"Girdiğiniz kelime: {kullanici_girisi}")
    print("--- (Döngü başına dönülüyor) ---")

print("Program 'break' sayesinde döngünün dışına çıktı ve bitti.")


print("\n" + "=" * 40)
print("--- Örnek 3: 'continue' (Adımı Atlama) ---")
print("=" * 40)

# 'continue' anahtar kelimesi, 'break' gibi döngüyü kırmaz.
# 'continue', döngü bloğunun geri kalan kodlarını o adım için YARIDA KESER
# ve döngünün en başına (koşul kontrolüne) geri döner.
#
# Görev: 1'den 10'a kadar olan sayılardan sadece TEK sayıları yazdıralım.

sayi = 0
print("1'den 10'a kadar olan TEK sayılar yazdırılacak...")

while sayi < 10:
    # Sayacı döngünün başında artıralım
    sayi += 1 
    
    # Şimdi kontrol edelim:
    # sayi % 2 (mod alma) -> sayının 2'ye bölümünden KALAN'ı verir.
    # Kalan 0 ise, sayı ÇİFT'tir.
    if sayi % 2 == 0:
        # Sayı çift ise...
        # 'continue' komutu, bu adımın geri kalanını (alttaki print) ATLAR
        # ve 'while sayi < 10:' satırına geri döner.
        continue 
    
    # Bu satır SADECE 'if' koşulu 'False' ise (yani sayı TEK ise) çalışır
    print(f"Bulunan Tek Sayı: {sayi}")

print("Döngü bitti.")


# --- Python 'while...else' Kullanımı: İki Durumlu Örnek ---

# Kural: 'else' bloğu, 'while' döngüsü 'break' komutu ile
# KESİLMEZSE çalışır. Döngü 'break' ile terk edilirse, 'else' bloğu atlanır.


print("=" * 40)
print("--- 1. DURUM: 'else' Bloğunun ÇALIŞTIĞI Örnek (Doğal Bitiş) ---")
print("=" * 40)
# Amaç: Geri sayım yapmak. Döngü 'break' ile kesilmeyecek.

sayac = 3
print("Geri sayım başlıyor...")

while sayac > 0:
    print(f"Sayı: {sayac}")
    sayac -= 1
    # Bu döngüde hiç 'break' komutu KULLANILMADI.

else:
    # 'while' koşulu (sayac > 0) 'False' olduğu an
    # (yani sayac = 0 olunca) döngü doğal yolla biter.
    # BU YÜZDEN 'else' BLOĞU ÇALIŞIR.
    print("Döngü doğal yollarla bitti. 'else' bloğu çalıştı.")

print("--- 1. Durumun Sonu ---")


print("\n" + "=" * 40)
print("--- 2. DURUM: 'else' Bloğunun ATLANDIĞI Örnek ('break' ile Kesilme) ---")
print("=" * 40)
# Amaç: Bir listede bir öğeyi aramak ve bulunca 'break' ile çıkmak.

liste = ["elma", "armut", "kiraz", "çilek"]
aranan_meyve = "kiraz"
print(f"Liste: {liste}")
print(f"Aranan: {aranan_meyve}")

i = 0 # İndeks sayacı

while i < len(liste): # Listenin sonuna gelene kadar
    mevcut_meyve = liste[i]
    print(f"Kontrol ediliyor: {mevcut_meyve}")
    
    if mevcut_meyve == aranan_meyve:
        print(f"Aranan meyve ({aranan_meyve}) bulundu!")
        # Sayıyı bulduğumuz için döngüyü 'break' ile terk ediyoruz.
        break
        
    i += 1 # Bir sonraki indekse geç

else:
    # Döngü 'break' komutu ile aniden kesildiği için,
    # BU 'else' BLOĞU TAMAMEN ATLANIR ve HİÇ ÇALIŞMAZ.
    print("!!! BU SATIR ÇALIŞMADI (çünkü 'break' kullanıldı) !!!")

print("--- 2. Durumun Sonu ---")