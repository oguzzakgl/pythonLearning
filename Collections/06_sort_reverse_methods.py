# Konu: Liste Sıralama Metotları
# Amaç: sort() ile sıralama ve reverse() ile ters çevirme işlemleri ve farkları.

# --- Python Liste Metotları: sort() ve reverse() ---

# Amaç: Bir listenin içeriğini 'sort' ile sıralamak ve
# 'reverse' ile mevcut sırasını ters çevirmek arasındaki
# farkı anlamak.

# Not: Her iki metot da listeyi 'yerinde' (in-place)
# yani kalıcı olarak değiştirir ve 'None' (boş) döndürür.

print("--- 1. BÖLÜM: sort() Metodu (Sıralama) ---")
# 'sort()' metodu, listeyi varsayılan olarak küçükten büyüğe (sayılar)
# veya alfabetik (string'ler) olarak sıralar.

# 1a. Sayısal Sıralama
sayilar = [40, 10, 500, 5, 20]
print(f"Sayılar (Orijinal Hali): {sayilar}")

# Listeyi küçükten büyüğe sıralayalım
sayilar.sort()
print(f"sort() sonrası (K->B): {sayilar}") # Çıktı: [5, 10, 20, 40, 500]

# 1b. Ters Sıralama (Büyükten Küçüğe)
# 'sort(reverse=True)' parametresi ile sıralama yönünü tersine çevirebiliriz.
sayilar.sort(reverse=True)
print(f"sort(reverse=True) sonrası (B->K): {sayilar}") # Çıktı: [500, 40, 20, 10, 5]

print("-" * 30)

# 1c. Alfabetik Sıralama
kelimeler = ["Elma", "Armut", "Kiraz", "ayva", "Çilek"]
print(f"Kelimeler (Orijinal Hali): {kelimeler}")

# Alfabetik sıralama (Varsayılan)
# DİKKAT: Python'da büyük harfler (ASCII) küçük harflerden önce gelir.
kelimeler.sort()
print(f"sort() sonrası (Alfabetik): {kelimeler}")
# Çıktı: ['Armut', 'Elma', 'Kiraz', 'Çilek', 'ayva']
# (Önce A, E, K, Ç... sonra a)

print("=" * 40)


print("--- 2. BÖLÜM: reverse() Metodu (Ters Çevirme) ---")
# 'reverse()' metodu sıralama YAPMAZ.
# Sadece listenin mevcut sırasını alır ve (ilk öğeyi sonuncu,
# sonuncu öğeyi ilk öğe yapacak şekilde) tersine çevirir.

# 2a. 'reverse()' Kullanımı
# Listemiz en son [500, 40, 20, 10, 5] halindeydi.
print(f"Sayılar (Önceki Hali): {sayilar}")

# Şimdi bu sırayı ters çevirelim:
sayilar.reverse()
print(f"reverse() sonrası: {sayilar}")
# Çıktı: [5, 10, 20, 40, 500]
# (Büyükten küçüğe sıralı listeyi, küçükten büyüğe çevirmiş oldu)

print("-" * 30)

# Karışık bir liste üzerinde deneyelim:
karisik_liste = [10, "Zebra", 5, "Elma"]
print(f"Karışık Liste (Orijinal): {karisik_liste}")

# Bu listeyi 'sort()' yapamayız, çünkü sayı ve string'i karşılaştıramaz (TypeError verir).
# Ancak 'reverse()' edebiliriz, çünkü o sadece sırayı ters çevirir.
karisik_liste.reverse()
print(f"reverse() sonrası: {karisik_liste}")
# Çıktı: ['Elma', 5, 'Zebra', 10] (Sadece sırası değişti)

print("=" * 40)


print("--- ÖZET: ÖNEMLİ FARK ---")
# 'sort(reverse=True)' ve 'reverse()' aynı şey DEĞİLDİR.

yeni_liste = [10, 50, 20]
print(f"Yeni Liste: {yeni_liste}")

# 1. 'sort(reverse=True)': Önce B->K sıralar.
yeni_liste.sort(reverse=True)
print(f"sort(reverse=True) sonrası: {yeni_liste}") # Çıktı: [50, 20, 10]

# 2. 'reverse()': Mevcut sırayı [50, 20, 10] ters çevirir.
yeni_liste.reverse()
print(f"reverse() sonrası: {yeni_liste}") # Çıktı: [10, 20, 50]