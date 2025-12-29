# --- BÖLÜM 1: MEMBERSHIP (AİTLİK) OPERATÖRLERİ (`in`, `not in`) ---
# Bu operatörler bir değerin, bir dizinin (string, liste, demet, sözlük vb.)
# içinde olup olmadığını kontrol eder ve 'True' veya 'False' döndürür.

print("--- BÖLÜM 1: MEMBERSHIP (AİTLİK) OPERATÖRLERİ ---")

# Örnek verilerimizi hazırlayalım
isim_listesi = ["ali", "veli", "ayşe", "can"]
metin = "merhaba dünya"
ogrenci_notlari = {"ali": 80, "veli": 90} # Sözlük (Dictionary)

# 1. 'in' Operatörü
# "İçinde mi?" anlamına gelir. Değer koleksiyonun içindeyse 'True' döner.

# Liste üzerinde 'in' kullanımı:
print(f"Listemiz: {isim_listesi}")
sonuc_in_1 = "veli" in isim_listesi
print(f"'veli' bu listenin içinde mi? : {sonuc_in_1}") # Çıktı: True

sonuc_in_2 = "mehmet" in isim_listesi
print(f"'mehmet' bu listenin içinde mi? : {sonuc_in_2}") # Çıktı: False

# String (metin) üzerinde 'in' kullanımı:
print(f"\nMetnimiz: '{metin}'")
sonuc_in_3 = "dünya" in metin # Alt metin kontrolü
print(f"'dünya' bu metnin içinde mi? : {sonuc_in_3}") # Çıktı: True

sonuc_in_4 = "mer" in metin
print(f"'mer' bu metnin içinde mi? : {sonuc_in_4}") # Çıktı: True

sonuc_in_5 = "python" in metin
print(f"'python' bu metnin içinde mi? : {sonuc_in_5}") # Çıktı: False

# Sözlük üzerinde 'in' kullanımı:
# DİKKAT: Sözlüklerde 'in' operatörü varsayılan olarak 'anahtarlara (keys)' bakar, değerlere (values) değil.
print(f"\nSözlüğümüz: {ogrenci_notlari}")
sonuc_in_6 = "ali" in ogrenci_notlari # 'ali' bir anahtardır
print(f"'ali' bu sözlükte bir ANAHTAR mı? : {sonuc_in_6}") # Çıktı: True

sonuc_in_7 = 80 in ogrenci_notlari # 80 bir değerdir (value)
print(f"80 bu sözlükte bir ANAHTAR mı? : {sonuc_in_7}") # Çıktı: False
# (Eğer değerleri aramak isterseniz: '80 in ogrenci_notlari.values()' kullanılır)

print("-" * 20)

# 2. 'not in' Operatörü
# "İçinde değil mi?" anlamına gelir. 'in' operatörünün tam tersidir.
# Değer koleksiyonun içinde DEĞİLSE 'True' döner.

sonuc_notin_1 = "mehmet" not in isim_listesi
print(f"'mehmet' bu listenin içinde değil mi? : {sonuc_notin_1}") # Çıktı: True

sonuc_notin_2 = "veli" not in isim_listesi
print(f"'veli' bu listenin içinde değil mi? : {sonuc_notin_2}") # Çıktı: False

sonuc_notin_3 = "python" not in metin
print(f"'python' bu metnin içinde değil mi? : {sonuc_notin_3}") # Çıktı: True

print("\n" + "-" * 30 + "\n") # Ayraç

# --- BÖLÜM 2: BITWISE (BİT DÜZEYİNDE) OPERATÖRLER ---
# DİKKAT: Bu operatörler sayıların 10'luk tabandaki değerleriyle değil,
# 2'lik (binary) tabandaki bit (0 ve 1) karşılıklarıyla işlem yapar.
# Bu operatörleri anlamak için sayıların ikilik karşılıklarını bilmek gerekir.

print("--- BÖLÜM 2: BITWISE (BİT DÜZEYİNDE) OPERATÖRLER ---")

# Örnek sayılarımız (standart 8-bit olarak gösterelim)
# a = 60
# b = 13
#
# İkilik (Binary) Karşılıkları:
# a = 60  ->  0011 1100
# b = 13  ->  0000 1101

a = 60
b = 13

print(f"Sayılarımız: a = {a} (İkilik: {a:08b}), b = {b} (İkilik: {b:08b})")
print("-" * 20)

# 1. Bitwise AND (&)
# İki sayının bitlerini alt alta karşılaştırır.
# Sadece her iki bit de 1 ise sonuç 1 olur, diğer tüm durumlarda 0 olur.
#
#   0011 1100  (60)
# & 0000 1101  (13)
# -------------
#   0000 1100  (Sonuç 12)

sonuc_and = a & b
print(f"a & b (Bitwise AND): {sonuc_and} (İkilik: {sonuc_and:08b})") # Çıktı: 12

print("-" * 20)

# 2. Bitwise OR (|)
# İki sayının bitlerini alt alta karşılaştırır.
# En az bir bit 1 ise sonuç 1 olur, sadece ikisi de 0 ise 0 olur.
#
#   0011 1100  (60)
# | 0000 1101  (13)
# -------------
#   0011 1101  (Sonuç 61)

sonuc_or = a | b
print(f"a | b (Bitwise OR): {sonuc_or} (İkilik: {sonuc_or:08b})") # Çıktı: 61

print("-" * 20)

# 3. Bitwise XOR (^) (Exclusive OR / Özel VEYA)
# İki sayının bitlerini alt alta karşılaştırır.
# Bitler birbirinden FARKLI ise (biri 1, diğeri 0) sonuç 1 olur.
# Bitler aynı ise (ikisi de 0 veya ikisi de 1) sonuç 0 olur.
#
#   0011 1100  (60)
# ^ 0000 1101  (13)
# -------------
#   0011 0001  (Sonuç 49)

sonuc_xor = a ^ b
print(f"a ^ b (Bitwise XOR): {sonuc_xor} (İkilik: {sonuc_xor:08b})") # Çıktı: 49

print("-" * 20)

# 4. Bitwise NOT (~) (Tersi / Tümleyeni)
# Tek bir sayının TÜM BİTLERİNİ tersine çevirir (0'ları 1, 1'leri 0 yapar).
# DİKKAT: Python (ve çoğu dil) negatif sayıları 'İkinin Tümleyeni' (Two's Complement)
# sistemiyle sakladığı için 'Not' işlemi '-(x + 1)' formülüyle sonuçlanır.
#
# ~a = ~60
#   0011 1100  (60)
# -------------
#   1100 0011  (Bu, -61'in ikili sistemdeki temsilidir)
#
# Formül: ~x = -x - 1  ->  ~60 = -60 - 1 = -61

sonuc_not = ~a
print(f"~a (Bitwise NOT): {sonuc_not}") # Çıktı: -61

print("-" * 20)

# 5. Bitwise Left Shift (<<) (Sola Kaydırma)
# Bir sayının bitlerini belirtilen miktar kadar sola kaydırır.
# Sağdan boşalan yerlere 0 eklenir.
# Matematiksel olarak 'x << y', 'x * (2**y)' (x * 2 üzeri y) anlamına gelir.
#
# a << 2  (60'ı 2 bit sola kaydır)
#   0011 1100  (60)
# -------------
#   1111 0000  (Sonuç 240)
#
# Matematiksel kontrol: 60 * (2**2) = 60 * 4 = 240

sonuc_sol_kaydir = a << 2
print(f"a << 2 (Sola Kaydırma): {sonuc_sol_kaydir} (İkilik: {sonuc_sol_kaydir:08b})") # Çıktı: 240

print("-" * 20)

# 6. Bitwise Right Shift (>>) (Sağa Kaydırma)
# Bir sayının bitlerini belirtilen miktar kadar sağa kaydırır.
# Sağdan çıkan bitler atılır (kaybolur).
# Matematiksel olarak 'x >> y', 'x // (2**y)' (x'in 2 üzeri y'ye tam bölümü) anlamına gelir.
#
# a >> 2  (60'ı 2 bit sağa kaydır)
#   0011 1100  (60)
# -------------
#   0000 1111  (Sonuç 15)
#
# Matematiksel kontrol: 60 // (2**2) = 60 // 4 = 15

sonuc_sag_kaydir = a >> 2
print(f"a >> 2 (Sağa Kaydırma): {sonuc_sag_kaydir} (İkilik: {sonuc_sag_kaydir:08b})") # Çıktı: 15