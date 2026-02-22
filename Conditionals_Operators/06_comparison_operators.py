print("--- Karşılaştırma Operatörleri ---")

# Örneklerde kullanmak için değişkenlerimizi tanımlayalım
sayi_a = 20
sayi_b = 10
sayi_c = 20 # 'a' ile aynı değere sahip bir değişken

print(f"Değişkenlerimiz: a = {sayi_a}, b = {sayi_b}, c = {sayi_c}")
print("-" * 30) # Ayraç

# 1. Eşit mi? (==)
# İki değerin birbirine tam olarak eşit olup olmadığını kontrol eder.
# DİKKAT: Tek eşittir (=) 'atama' yapar, çift eşittir (==) 'karşılaştırma' yapar.

# (sayi_a == sayi_c) işlemi "20, 20'ye eşit mi?" diye sorar.
sonuc_esit_mi = (sayi_a == sayi_c)
print(f"{sayi_a} == {sayi_c} (Eşit mi?) : {sonuc_esit_mi}") # Çıktı: True

# (sayi_a == sayi_b) işlemi "20, 10'a eşit mi?" diye sorar.
sonuc_esit_mi_2 = (sayi_a == sayi_b)
print(f"{sayi_a} == {sayi_b} (Eşit mi?) : {sonuc_esit_mi_2}") # Çıktı: False

print("-" * 20)

# 2. Eşit değil mi? (!=)
# İki değerin birbirinden farklı olup olmadığını kontrol eder.
# '==' operatörünün tam tersi şekilde çalışır.

# (sayi_a != sayi_b) işlemi "20, 10'dan farklı mı?" diye sorar.
sonuc_farkli_mi = (sayi_a != sayi_b)
print(f"{sayi_a} != {sayi_b} (Eşit değil mi?) : {sonuc_farkli_mi}") # Çıktı: True

# (sayi_a != sayi_c) işlemi "20, 20'den farklı mı?" diye sorar.
sonuc_farkli_mi_2 = (sayi_a != sayi_c)
print(f"{sayi_a} != {sayi_c} (Eşit değil mi?) : {sonuc_farkli_mi_2}") # Çıktı: False

print("-" * 20)

# 3. Büyük mü? (>)
# Soldaki değerin, sağdaki değerden büyük olup olmadığını kontrol eder.

# (sayi_a > sayi_b) işlemi "20, 10'dan büyük mü?" diye sorar.
sonuc_buyuk_mu = (sayi_a > sayi_b)
print(f"{sayi_a} > {sayi_b} (Büyük mü?) : {sonuc_buyuk_mu}") # Çıktı: True

# (sayi_b > sayi_a) işlemi "10, 20'den büyük mü?" diye sorar.
sonuc_buyuk_mu_2 = (sayi_b > sayi_a)
print(f"{sayi_b} > {sayi_a} (Büyük mü?) : {sonuc_buyuk_mu_2}") # Çıktı: False

print("-" * 20)

# 4. Küçük mü? (<)
# Soldaki değerin, sağdaki değerden küçük olup olmadığını kontrol eder.

# (sayi_b < sayi_a) işlemi "10, 20'den küçük mü?" diye sorar.
sonuc_kucuk_mu = (sayi_b < sayi_a)
print(f"{sayi_b} < {sayi_a} (Küçük mü?) : {sonuc_kucuk_mu}") # Çıktı: True

# (sayi_a < sayi_b) işlemi "20, 10'dan küçük mü?" diye sorar.
sonuc_kucuk_mu_2 = (sayi_a < sayi_b)
print(f"{sayi_a} < {sayi_b} (Küçük mü?) : {sonuc_kucuk_mu_2}") # Çıktı: False

print("-" * 20)

# 5. Büyük veya Eşit mi? (>=)
# Soldaki değerin, sağdaki değerden 'büyük' VEYA 'eşit' olup olmadığını kontrol eder.
# İki koşuldan herhangi biri doğruysa (True) sonuç 'True' olur.

# (sayi_a >= sayi_b) işlemi "20, 10'dan büyük veya eşit mi?" diye sorar.
sonuc_buyuk_esit_1 = (sayi_a >= sayi_b)
print(f"{sayi_a} >= {sayi_b} (Büyük veya Eşit mi?) : {sonuc_buyuk_esit_1}") # Çıktı: True (Büyük koşulu sağlandı)

# (sayi_a >= sayi_c) işlemi "20, 20'den büyük veya eşit mi?" diye sorar.
sonuc_buyuk_esit_2 = (sayi_a >= sayi_c)
print(f"{sayi_a} >= {sayi_c} (Büyük veya Eşit mi?) : {sonuc_buyuk_esit_2}") # Çıktı: True (Eşit koşulu sağlandı)

# (sayi_b >= sayi_a) işlemi "10, 20'den büyük veya eşit mi?" diye sorar.
sonuc_buyuk_esit_3 = (sayi_b >= sayi_a)
print(f"{sayi_b} >= {sayi_a} (Büyük veya Eşit mi?) : {sonuc_buyuk_esit_3}") # Çıktı: False (İki koşul da sağlanmadı)

print("-" * 20)

# 6. Küçük veya Eşit mi? (<=)
# Soldaki değerin, sağdaki değerden 'küçük' VEYA 'eşit' olup olmadığını kontrol eder.

# (sayi_b <= sayi_a) işlemi "10, 20'den küçük veya eşit mi?" diye sorar.
sonuc_kucuk_esit_1 = (sayi_b <= sayi_a)
print(f"{sayi_b} <= {sayi_a} (Küçük veya Eşit mi?) : {sonuc_kucuk_esit_1}") # Çıktı: True (Küçük koşulu sağlandı)

# (sayi_a <= sayi_c) işlemi "20, 20'den küçük veya eşit mi?" diye sorar.
sonuc_kucuk_esit_2 = (sayi_a <= sayi_c)
print(f"{sayi_a} <= {sayi_c} (Küçük veya Eşit mi?) : {sonuc_kucuk_esit_2}") # Çıktı: True (Eşit koşulu sağlandı)

# (sayi_a <= sayi_b) işlemi "20, 10'dan küçük veya eşit mi?" diye sorar.
sonuc_kucuk_esit_3 = (sayi_a <= sayi_b)
print(f"{sayi_a} <= {sayi_b} (Küçük veya Eşit mi?) : {sonuc_kucuk_esit_3}") # Çıktı: False (İki koşul da sağlanmadı)

print("\n" + "-" * 30 + "\n") # Ayraç

# --- 'if' İfadelerinde Kullanım Örneği ---
print("--- 'if' İfadelerinde Kullanım ---")
# Bu 'True'/'False' sonuçları en çok 'if' bloklarının çalışıp
# çalışmayacağına karar vermek için kullanılır.

yas = 19
ehliyet_yasi_siniri = 18

print(f"Kişinin yaşı: {yas}, Ehliyet yaşı: {ehliyet_yasi_siniri}")

# Python burada 'yas >= ehliyet_yasi_siniri' (19 >= 18) işlemini yapar.
# Sonuç 'True' olduğu için 'if' bloğunun İÇİNDEKİ kod çalışır.
if yas >= ehliyet_yasi_siniri:
    print("SONUÇ: Ehliyet alabilirsiniz.")
else:
    # Eğer sonuç 'False' olsaydı bu blok çalışacaktı.
    print("SONUÇ: Ehliyet alamazsınız.")

print("-" * 20)

# Metin (String) Karşılaştırması
# Bu operatörler metinleri de alfabetik sıraya göre karşılaştırır.
kelime1 = "armut"
kelime2 = "elma"

# 'a' harfi 'e' harfinden alfabetik olarak önce (daha küçük) gelir.
if kelime1 < kelime2:
    print(f"'{kelime1}', '{kelime2}' kelimesinden alfabetik olarak öncedir.")