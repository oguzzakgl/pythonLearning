# Mantıksal Operatörler
print("--- Mantıksal Operatörler ---")

# Örneklerde kullanmak için değişkenlerimizi (koşullarımızı) tanımlayalım
# Bu değişkenler bir karşılaştırma sonucu 'True' veya 'False' olmuş gibi davranacaklar.

kosul_A = True  # Örn: yas > 18 (yaş 20 ise True)
kosul_B = False # Örn: mezun_mu == True (mezun değilse False)
kosul_C = True  # Örn: saglik_durumu_iyi_mi == True (iyiyse True)

print(f"Koşullarımız: A = {kosul_A}, B = {kosul_B}, C = {kosul_C}")
print("-" * 30) # Ayraç

# --- 1. 'and' (ve) Operatörü ---
# Bu operatör, birleştirilen TÜM koşullar 'True' ise 'True' sonucunu verir.
# Bir tanesi bile 'False' ise sonuç 'False' olur.
# Kullanım: "Hem A DOĞRU OLMALI hem de B DOĞRU OLMALI"

print("--- 1. 'and' (ve) Operatörü ---")
# (True and False) -> İkisi de True değil.
sonuc_and_1 = kosul_A and kosul_B
print(f"{kosul_A} and {kosul_B} : {sonuc_and_1}") # Çıktı: False

# (True and True) -> İkisi de True.
sonuc_and_2 = kosul_A and kosul_C
print(f"{kosul_A} and {kosul_C} : {sonuc_and_2}") # Çıktı: True

# (False and False) -> İkisi de True değil.
sonuc_and_3 = kosul_B and kosul_B
print(f"{kosul_B} and {kosul_B} : {sonuc_and_3}") # Çıktı: False

print("-" * 20)

# 'and' ile if Kullanım Örneği (İşe alım)
# Kural: Aday hem 18 yaşından büyük (kosul_A) hem de mezun (kosul_B) olmalı.
yas = 20
mezun_mu = False
print(f"İşe alım örneği: Yaş = {yas}, Mezun mu = {mezun_mu}")

# (yas > 18) -> True
# (mezun_mu == True) -> False
# (True and False) -> False
if (yas > 18) and (mezun_mu == True):
    print("SONUÇ: İşe alındınız.") # Bu satır çalışmaz
else:
    print("SONUÇ: İşe alınmadınız (Koşullardan en az biri sağlanmadı).")

print("-" * 30) # Ayraç

# --- 2. 'or' (veya) Operatörü ---
# Bu operatör, birleştirilen koşullardan EN AZ BİRİ 'True' ise 'True' sonucunu verir.
# Sonucun 'False' olması için TÜM koşulların 'False' olması gerekir.
# Kullanım: "A DOĞRU olsa da olur, B DOĞRU olsa da olur (ya da ikisi birden)."

print("--- 2. 'or' (veya) Operatörü ---")
# (True or False) -> En az biri (kosul_A) True.
sonuc_or_1 = kosul_A or kosul_B
print(f"{kosul_A} or {kosul_B} : {sonuc_or_1}") # Çıktı: True

# (True or True) -> İkisi de True.
sonuc_or_2 = kosul_A or kosul_C
print(f"{kosul_A} or {kosul_C} : {sonuc_or_2}") # Çıktı: True

# (False or False) -> Hiçbiri True değil.
sonuc_or_3 = kosul_B or kosul_B
print(f"{kosul_B} or {kosul_B} : {sonuc_or_3}") # Çıktı: False

print("-" * 20)

# 'or' ile if Kullanım Örneği (İndirim)
# Kural: Müşteri 65 yaş üstü VEYA öğrenci ise indirim alır.
musteri_yas = 30
ogrenci_mi = True
print(f"İndirim örneği: Yaş = {musteri_yas}, Öğrenci mi = {ogrenci_mi}")

# (musteri_yas > 65) -> False
# (ogrenci_mi == True) -> True
# (False or True) -> True
if (musteri_yas > 65) or (ogrenci_mi == True):
    print("SONUÇ: İndirim alabilirsiniz.")
else:
    print("SONUÇ: İndirim alamazsınız.") # Bu satır çalışmaz

print("-" * 30) # Ayraç

# --- 3. 'not' (değil) Operatörü ---
# Bu operatör tek bir 'bool' değeri alır ve onu TERSİNE çevirir.
# 'True' ise 'False' yapar.
# 'False' ise 'True' yapar.
# Kullanım: "Koşulun sağlanmadığı durumu kontrol etmek" (Örn: "mezun DEĞİLSE").

print("--- 3. 'not' (değil) Operatörü ---")

# kosul_A True idi. 'not' onu False yapar.
sonuc_not_1 = not kosul_A
print(f"not {kosul_A} : {sonuc_not_1}") # Çıktı: False

# kosul_B False idi. 'not' onu True yapar.
sonuc_not_2 = not kosul_B
print(f"not {kosul_B} : {sonuc_not_2}") # Çıktı: True

print("-" * 20)

# 'not' ile if Kullanım Örneği (Sistem Kilidi)
# Kural: Sistem kilitli DEĞİLSE (kilitli = False) giriş yap.
sistem_kilitli_mi = False
print(f"Sistem kilidi örneği: Kilitli mi = {sistem_kilitli_mi}")

# (not sistem_kilitli_mi) -> (not False) -> True
if not sistem_kilitli_mi:
    print("SONUÇ: Giriş yapılıyor...")
else:
    print("SONUÇ: Sistem kilitli, giriş yapılamaz.")

print("\n" + "-" * 30 + "\n") # Ayraç

# --- KARMAŞIK KULLANIM (Operatörleri Birleştirme) ---
# Operatörler parantezler kullanılarak birleştirilebilir.
# Kural: (A ve C doğruysa) VEYA (B yanlışsa (yani 'not B' ise))

print("--- Karmaşık Kullanım Örneği ---")
# kosul_A = True
# kosul_B = False
# kosul_C = True

# 1. Parantez içi: (kosul_A and kosul_C) -> (True and True) -> True
# 2. Parantez içi: (not kosul_B) -> (not False) -> True
# 3. Sonuç: (True or True) -> True
karma_sonuc = (kosul_A and kosul_C) or (not kosul_B)

print(f"({kosul_A} and {kosul_C}) or (not {kosul_B}) = {karma_sonuc}") # Çıktı: True