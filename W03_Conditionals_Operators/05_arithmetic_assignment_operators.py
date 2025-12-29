# --- BÖLÜM 1: ARİTMETİK OPERATÖRLER ---
# Bu operatörler, sayılarla temel matematiksel işlemleri yapmak için kullanılır.

print("--- BÖLÜM 1: ARİTMETİK OPERATÖRLER ---")

# Örnek için iki sayı tanımlayalım
sayi1 = 20
sayi2 = 8

# 1. Toplama (+)
# İki sayıyı toplar.
toplam = sayi1 + sayi2
print(f"{sayi1} + {sayi2} = {toplam}") # Çıktı: 28

# 2. Çıkarma (-)
# Bir sayıdan diğerini çıkarır.
fark = sayi1 - sayi2
print(f"{sayi1} - {sayi2} = {fark}") # Çıktı: 12

# 3. Çarpma (*)
# İki sayıyı çarpar.
carpim = sayi1 * sayi2
print(f"{sayi1} * {sayi2} = {carpim}") # Çıktı: 160

# --- Bölme İşlemleri (Önemli Farklılıklar) ---

# 4. Normal Bölme (/)
# Standart bölme işlemi yapar.
# SONUÇ HER ZAMAN 'float' (ondalıklı sayı) olur.
bolum_float = sayi1 / sayi2 # 20 / 8 = 2.5
print(f"{sayi1} / {sayi2} = {bolum_float} (Sonuç 'float' tipindedir)") # Çıktı: 2.5

# 5. Tam Bölme (//) (Floor Division)
# Bölme işleminin sadece tam sayı kısmını alır (sonucu aşağı yuvarlar).
# Eğer sayılar 'int' ise sonuç 'int' olur.
bolum_tam = sayi1 // sayi2 # 20 / 8 = 2 (2.5'in tam kısmı)
print(f"{sayi1} // {sayi2} = {bolum_tam} (Sonuç 'int' tipindedir)") # Çıktı: 2

# Örnek (negatif sayılarda):
# -20 // 8 -> -2.5 yapar, aşağı yuvarlayarak -3 sonucunu verir.
print(f"-20 // 8 = {-20 // 8}") # Çıktı: -3

# 6. Mod Alma (%) (Modulus)
# Bir sayının diğer sayıya bölünmesinden KALANI verir.
# Kalanı bulmak için çok kullanışlıdır (örn: çift/tek sayı kontrolü).
kalan = sayi1 % sayi2 # 20'nin 8'e bölümünden kalan (8 * 2 = 16 -> 20 - 16 = 4)
print(f"{sayi1} % {sayi2} = {kalan} (Bölümden kalan)") # Çıktı: 4

# Çift/Tek Kontrolü Örneği:
print(f"5 % 2 = {5 % 2}") # Kalan 1'dir (Tek sayı)
print(f"6 % 2 = {6 % 2}") # Kalan 0'dır (Çift sayı)

# 7. Üs Alma (**) (Exponentiation)
# Bir sayının kuvvetini (üssünü) alır.
us_alma = 5 ** 3 # 5 üzeri 3 (5 * 5 * 5)
print(f"5 ** 3 = {us_alma}") # Çıktı: 125

# Karakök almak için 0.5. kuvveti kullanılabilir:
karekok = 64 ** 0.5
print(f"64 ** 0.5 = {karekok}") # Çıktı: 8.0

print("\n" + "-" * 30 + "\n") # Ayraç

# --- BÖLÜM 2: ATAMA OPERATÖRLERİ ---
# Bu operatörler, değişkenlere değer atamak veya mevcut değerlerini güncellemek için kullanılır.

print("--- BÖLÜM 2: ATAMA OPERATÖRLERİ ---")

# 1. Temel Atama (=)
# Sağdaki değeri soldaki değişkene atar (eşitlik kontrolü DEĞİLDİR, '==' eşitlik kontrolüdür).
x = 10
print(f"'x' değişkeninin ilk değeri: {x}")

# 2. Birleşik Atama Operatörleri
# Bu operatörler, bir aritmetik işlemi ve atama işlemini birleştirerek
# kodu kısaltmayı sağlar. (Örn: 'x = x + 5' yerine 'x += 5' yazılır)

# 2a. Toplayarak Atama (+=)
# x = x + 5 işleminin kısaltmasıdır.
print("-" * 20)
print(f"'x' (10) üzerine 5 ekleniyor (x += 5)...")
x += 5 # x = 10 + 5
print(f"'x' değişkeninin yeni değeri: {x}") # Çıktı: 15

# 2b. Çıkararak Atama (-=)
# x = x - 3 işleminin kısaltmasıdır.
print("-" * 20)
print(f"'x' (15) değerinden 3 çıkarılıyor (x -= 3)...")
x -= 3 # x = 15 - 3
print(f"'x' değişkeninin yeni değeri: {x}") # Çıktı: 12

# 2c. Çarparak Atama (*=)
# x = x * 2 işleminin kısaltmasıdır.
print("-" * 20)
print(f"'x' (12) değeri 2 ile çarpılıyor (x *= 2)...")
x *= 2 # x = 12 * 2
print(f"'x' değişkeninin yeni değeri: {x}") # Çıktı: 24

# 2d. Bölerek Atama (/=)
# x = x / 4 işleminin kısaltmasıdır.
# Normal bölme (/) kullanıldığı için sonuç 'float' olur.
print("-" * 20)
print(f"'x' (24) değeri 4'e bölünüyor (x /= 4)...")
x /= 4 # x = 24 / 4
print(f"'x' değişkeninin yeni değeri: {x}") # Çıktı: 6.0

# 2e. Tam Bölerek Atama (//=)
# x = x // 5 işleminin kısaltmasıdır.
print("-" * 20)
# 'x' şu an 6.0 (float)
print(f"'x' (6.0) değeri 5'e tam bölünüyor (x //= 5)...")
x //= 5 # x = 6.0 // 5 (Sonuç 1.0)
print(f"'x' değişkeninin yeni değeri: {x}") # Çıktı: 1.0

# 2f. Mod Alarak Atama (%=)
# x = x % 3 işleminin kısaltmasıdır.
print("-" * 20)
# 'x' şu an 1.0
# Yeni bir tamsayı değeri atayalım ki mod alma anlamlı olsun
x = 17
print(f"'x' değeri 17 olarak ayarlandı.")
print(f"'x' (17) değerinin 5'e bölümünden kalanı atanıyor (x %= 5)...")
x %= 5 # x = 17 % 5 (Kalan 2)
print(f"'x' değişkeninin yeni değeri: {x}") # Çıktı: 2

# 2g. Üs Alarak Atama (**=)
# x = x ** 4 işleminin kısaltmasıdır.
print("-" * 20)
print(f"'x' (2) değerinin 4. kuvveti atanıyor (x **= 4)...")
x **= 4 # x = 2 ** 4 (Yani 2 * 2 * 2 * 2)
print(f"'x' değişkeninin yeni değeri: {x}") # Çıktı: 16