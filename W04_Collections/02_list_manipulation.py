# Konu: Liste Düzenleme Metotları
# Amaç: insert, extend, copy metotları ve slicing (dilimleme) ile liste manipülasyonu.

# --- Python Liste Metotları (insert, extend, copy) ve Slicing ---

# Bu örnekte, bir listeyi nasıl daha detaylı
# manipüle edeceğimizi ve kopyalayacağımızı göreceğiz.

# --- 1. insert() Metodu (Araya Ekleme) ---
# 'append()' metodu sadece listenin SONUNA ekler.
# 'insert()' ise belirlediğiniz bir İNDEKSE (araya) öğe ekler.
# Kullanımı: liste.insert(indeks_numarası, eklenecek_oge)

print("--- 1. insert() ---")
harfler = ['a', 'b', 'd', 'e']
print(f"Listenin orijinal hali: {harfler}")

# 'b' (indeks 1) ve 'd' (indeks 2) arasına 'c' harfini ekleyelim.
# 'c' harfini 2. indekse ekliyoruz, 'd' ve 'e' sağa kayıyor.
harfler.insert(2, 'c')

print(f"'c' eklendikten sonra: {harfler}") # Çıktı: ['a', 'b', 'c', 'd', 'e']
print("-" * 30)


# --- 2. extend() Metodu (Listeyi Genişletme) ---
# Bir listeye, başka bir listenin (veya tuple gibi başka bir veri grubunun)
# TÜM ÖĞELERİNİ tek seferde eklemek için kullanılır.
# 'append()' ve 'extend()' farkı çok önemlidir:
#   - append([1, 2]): Listenin sonuna [1, 2] listesini BİR BÜTÜN olarak ekler.
#   - extend([1, 2]): Listenin sonuna 1'i ve 2'yi AYRI AYRI ekler.

print("--- 2. extend() ---")
liste_a = [1, 2, 3]
liste_b = [4, 5, 6]

# 'liste_a'yı, 'liste_b'nin öğeleriyle genişletelim
liste_a.extend(liste_b)
print(f"extend() sonrası liste_a: {liste_a}") # Çıktı: [1, 2, 3, 4, 5, 6]

# Karşılaştırma için 'append' farkı:
liste_c = [10, 20, 30]
liste_d = [40, 50]
liste_c.append(liste_d)
print(f"append() sonrası liste_c: {liste_c}") # Çıktı: [10, 20, 30, [40, 50]]
print("-" * 30)


# --- 3. copy() Metodu (Yüzeysel Kopyalama) ---
# Bir listenin birebir aynısını, ancak bellekte FARKLI bir yerde
# tutan YENİ bir kopyasını oluşturur.
# Bu, kopyalanan listede yapılan değişikliklerin orijinal listeyi ETKİLEMEMESİNİ sağlar.

print("--- 3. copy() ve Atama (=) Farkı ---")
orijinal_liste = ["elma", "armut", "kiraz"]
print(f"Orijinal liste: {orijinal_liste}")

# Yöntem 1: YANLIŞ Kopyalama (Atama = ile)
# Bu bir kopya oluşturmaz. 'yeni_liste_a' sadece 'orijinal_liste'nin
# bellekteki YERİNİ işaret eder. İkisi de AYNI listedir.
yeni_liste_a = orijinal_liste
yeni_liste_a.append("çilek") # 'yeni_liste_a'ya ekleme yapıyoruz...
print(f"Atama (=) ile ekleme sonrası YENİ liste: {yeni_liste_a}")
print(f"Atama (=) sonrası ORİJİNAL liste: {orijinal_liste}") # ORİJİNAL LİSTE DEĞİŞTİ!

print("." * 20)

# Yöntem 2: DOĞRU Kopyalama (.copy() metodu ile)
# 'orijinal_liste_2'nin YÜZEYSEL bir kopyasını oluşturur.
orijinal_liste_2 = ["elma", "armut", "kiraz"]
print(f"Orijinal liste 2: {orijinal_liste_2}")

yeni_liste_b = orijinal_liste_2.copy()
yeni_liste_b.append("çilek") # Sadece KOPYA listeye ekleme yapıyoruz.
print(f".copy() ile ekleme sonrası YENİ liste: {yeni_liste_b}")
print(f".copy() sonrası ORİJİNAL liste 2: {orijinal_liste_2}") # ORİJİNAL LİSTE DEĞİŞMEDİ!
print("-" * 30)


# --- 4. Slicing (Dilimleme) ---
# 'Slicing', bir listenin belirli bir aralığını (dilimini) almaktır.
# Aynı zamanda .copy() gibi YÜZEYSEL KOPYA oluşturmak için de kullanılır.
# Kullanımı: liste[baslangic : bitis : adim]
# - baslangic: Dahildir (varsayılan: 0, en baş)
# - bitis: Dahil DEĞİLDİR (varsayılan: en son)
# - adim: Kaçar kaçar atlayacağı (varsayılan: 1)

print("--- 4. Slicing (Dilimleme) ---")
sayilar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Orijinal sayılar: {sayilar}")

# 4a. Belirli bir aralığı alma
# 2. indeksten başla (dahil), 5. indekse kadar git (5 dahil değil)
dilim_1 = sayilar[2:5]
print(f"sayilar[2:5] : {dilim_1}") # Çıktı: [2, 3, 4]

# 4b. Baştan bir yere kadar
# En baştan (indeks 0) başla, 4. indekse kadar git (4 dahil değil)
dilim_2 = sayilar[:4]
print(f"sayilar[:4]  : {dilim_2}") # Çıktı: [0, 1, 2, 3]

# 4c. Bir yerden sona kadar
# 6. indeksten başla (dahil), sonuna kadar git
dilim_3 = sayilar[6:]
print(f"sayilar[6:]  : {dilim_3}") # Çıktı: [6, 7, 8, 9]

# 4d. Adım (Step) belirterek atlama
# Listenin tamamında (::), 2'şer 2'şer atla (çift sayılar)
dilim_4 = sayilar[::2]
print(f"sayilar[::2] : {dilim_4}") # Çıktı: [0, 2, 4, 6, 8]

# 4e. Listeyi ters çevirme
# Listenin tamamında (::), -1 adımla (tersten) git
dilim_5 = sayilar[::-1]
print(f"sayilar[::-1]: {dilim_5}") # Çıktı: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# 4f. Slicing ile KOPYALAMA
# Listenin tamamını dilimlemek [:] .copy() metoduyla aynı işi yapar.
kopya_liste = sayilar[:]
kopya_liste.append(100)
print(f"Slicing [:] ile kopya liste: {kopya_liste}")
print(f"Orijinal 'sayilar' listesi: {sayilar}") # Orijinal liste DEĞİŞMEDİ.