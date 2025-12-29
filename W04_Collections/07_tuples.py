# Konu: Tuple (Demet) Temelleri
# Amaç: Tuple oluşturma, değiştirilemezlik (immutable) özelliği, paketleme ve paketten çıkarma.

# --- Tuple (Demet) ---
# Temel Kural: Değiştirilemez (immutable). 
# İçeriği doğrudan güncellenemez, eklenemez veya kaldırılamaz.

# --- 1. Veri Güncelleme (Dolaylı Yöntem) ---
# Doğrudan my_tuple[0] = "x" -> TypeError verir.
my_tuple = ("a", "b", "c")
temp_list = list(my_tuple)  # 1. Listeye çevir
temp_list[0] = "x"          # 2. Listeyi güncelle
my_tuple = tuple(temp_list) # 3. Tekrar tuple'a çevir
print(f"Güncellenmiş: {my_tuple}") # Çıktı: ('x', 'b', 'c')


# --- 2. Veri Ekleme (Dolaylı Yöntem) ---
# .append() metodu yoktur.
# Çözüm: + operatörü ile iki tuple'ı birleştirip YENİ bir tuple oluşturmak.
my_tuple = (1, 2, 3)
# Tek elemanlı tuple eklerken sondaki virgül (,) zorunludur.
new_tuple = my_tuple + (4,) 
print(f"Eklenmiş: {new_tuple}") # Çıktı: (1, 2, 3, 4)


# --- 3. Veri Kaldırma (Dolaylı Yöntem) ---
# .remove(), .pop() veya 'del my_tuple[0]' -> TypeError verir.
my_tuple = ("a", "b", "c")
temp_list = list(my_tuple)  # 1. Listeye çevir
temp_list.remove("b")       # 2. Listeden kaldır
my_tuple = tuple(temp_list) # 3. Tekrar tuple'a çevir
print(f"Kaldırılmış: {my_tuple}") # Çıktı: ('a', 'c')


# --- 4. Tuple Silme (Tamamını) ---
# 'del' komutu değişkenin tamamını bellekten siler.
my_tuple = (1, 2, 3)
del my_tuple
# print(my_tuple) # Bu satır artık NameError verir


# --- 5. Paketleme (Packing) ---
# Birden fazla değeri tek bir değişkene atama işlemidir.
# Python bu değerleri otomatik olarak bir tuple'a "paketler".
student = "Ahmet", 21, "Mühendislik"
print(f"Paketlenmiş: {student}") # Çıktı: ('Ahmet', 21, 'Mühendislik')


# --- 6. Paketten Çıkarma (Unpacking) ---
# Bir tuple içindeki elemanları sırayla birden fazla değişkene atama.
student = ("Ahmet", 21, "Mühendislik")
isim, yas, bolum = student
print(f"Paketten çıkan isim: {isim}") # Çıktı: Ahmet

# Yıldız (*) Operatörü ile Çıkarma:
# '*' bir liste olarak geri kalan elemanları toplar.
my_tuple = (1, 2, 3, 4, 5)
ilk, *orta, son = my_tuple
print(f"İlk: {ilk}")   # Çıktı: 1
print(f"Orta: {orta}")  # Çıktı: [2, 3, 4]  (Liste olarak)
print(f"Son: {son}")   # Çıktı: 5