# Konu: Python Veri Yapıları Özeti (Bölüm 1)
# Amaç: List, Tuple, Dict ve Set veri yapılarının temel özelliklerinin ve farklarının özeti.

# liste (list)

# sıralıdırlar, değiştirilebilirler ve farklı veri tiplerini bir arada tutabilir.
# [] ile oluşturulur
# her elemanın index numarası vardır
# olusturduktan sonra eleman eklenebilir cikartilabilri ve değistirilebilir

meyveler = ["elma", "armut", "kiraz", "muz"]


# elemanlara index ile ulasma

print(f"Listenin ilk elemanı (0. indeks): {meyveler[0]}") # Çıktı: elma
print(f"Listenin ikinci elemanı (1. indeks): {meyveler[1]}") # Çıktı: armut
print(f"Listenin son elemanı (-1. indeks): {meyveler[-1]}") # Çıktı: muz

# eleman değistirme

meyveler[0] = "çilek" # elmayı çilekle değistirir
print(f"Değiştirilmiş liste: {meyveler}") # çilek armut kiraz muz yazdırır

# eleman ekleme

meyveler.append("karpuz")
print(meyveler)

# eleman silme 

meyveler.pop(2) # listedeki 2. indexi siler(kiraz)
print(f"pop sonrası: {meyveler}") # çilek armut kiraz muz karpuz

# kac eleman oldugunu bulma

print(f"Listede {len(meyveler)} adet meyve var.")

print("-----------------------------------------------------") 


# tuple 

# sıralıdırlar, değistirilemez bir koleksiyondur () ile gosterilir
# sabit veriler icin kullanılır (günler, koordinat)

kordinatlar = (10.0, 20.5)

# elemanlara erisim

print(f"x koordinatı: {kordinatlar[0]}") # cıktı = 10.0

# 2. Değiştirmeyi Deneme 
# kordinatlar[0] = 15.0  # Bu satır TypeError verir: 'tuple' object does not support item assignment

print("-----------------------------------------------------") 



# dict 

# verileri anahtar değer olarak saklar (key, value)
# sıralıdırlar ve değistirilebilirler {} ile olusturulur
# birbiriyle bağlantılı bilgileri saklamak iicn kullanılır (ogrenci bilgileri, arabanın ozellikleri)


ogrenci = {
    "isim": "bora",
    "soyisim": "caba",
    "yas": 74,
    "numara": 123
}

# veriye erisim

print(f"ogrencinin ismi {ogrenci['isim']}, soyismi {ogrenci['soyisim']}, yasi {ogrenci['yas']}")

# veri degistirme

ogrenci["numara"] = 456 # numara anahtarının değerini 456 olarak degistirir
ogrenci["bolum"] = "isletme" # bolum adında yeni anahtar olusturur ve değerini isletme yapar

print(f"guncel sozluk {ogrenci}")

print("-----------------------------------------------------") 


# set (küme)

#tekrarlanmaz, sırasızlardır, degistirilebilir ve benzersiz elemanlardan olusur
# {} ile olusturukur anca bos olucaksa set() ile olusturulur

# Tekrarlayan elemanlar içeren bir liste
sayilar_listesi = [1, 2, 2, 3, 4, 4, 4, 5, 1]
print(f"Orijinal Liste: {sayilar_listesi}")

# 1. Set'e Çevirerek Benzersiz Hale Getirme
benzersiz_sayilar_seti = set(sayilar_listesi)
print(f"Set Hali (benzersiz): {benzersiz_sayilar_seti}") # Çıktı: {1, 2, 3, 4, 5}

# 2. Set'e Eleman Ekleme
benzersiz_sayilar_seti.add(6)
benzersiz_sayilar_seti.add(1) # 1 zaten var, tekrar eklenmeyecek
print(f"Set'e ekleme sonrası: {benzersiz_sayilar_seti}") # Çıktı: {1, 2, 3, 4, 5, 6}