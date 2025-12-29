# ============================================
# KOŞULLU İFADELER — TEK DOSYALIK ÖZET + ÖRNEKLER
# if / elif / else, karşılaştırmalar, mantıksal bağlaçlar, üyelik/kimlik,
# zincirli karşılaştırma, ternary, truthiness ve mini alıştırmalar (çözümler).
# Not: try/except yok. Hatalı girişte program hata verebilir.
# ============================================

print("== Temel if/elif/else ==")
x = 18
if x > 18:
    print("büyüksün")
elif x == 18:
    print("tam 18")
else:
    print("küçüksün")

print("\n== Karşılaştırmalar ==")
a, b = 5, 3
print("a==b:", a == b)
print("a!=b:", a != b)
print("a<b :", a < b)
print("a<=b:", a <= b)
print("a>b :", a > b)
print("a>=b:", a >= b)

print("\n== Mantıksal bağlaçlar ==")
age = 20
vip = False
if (age >= 18) and (not vip):
    print("giriş serbest (and/not)")
if (age < 18) or vip:
    print("istisna (or)")

print("\n== Üyelik ve kimlik ==")
s = "python"
if "py" in s:
    print("'py' alt dizisi var")
y = None
if y is None:
    print("y None (kimlik kontrolü)")

print("\n== Zincirli karşılaştırma ==")
n = 7
if 1 < n < 10:
    print("n 1 ile 10 arasında")

print("\n== Kısa (ternary) ifade ==")
puan = 75
sonuc = "geçti" if puan >= 60 else "kaldı"
print("sonuç:", sonuc)

print("\n== Truthiness ==")
# Boş değerler False kabul edilir: 0, 0.0, '', [], {}, set(), None
val = []
if not val:
    print("val boş kabul edilir")

# ============================================
# MINI ALIŞTIRMALAR — ÇÖZÜMLER
# ============================================

print("\n[1] Pozitif/Negatif/Sıfır")
sayi1 = float(input("Sayı gir (1): "))
if sayi1 > 0:
    print("pozitif")
elif sayi1 < 0:
    print("negatif")
else:
    print("sıfır")

print("\n[2] Not harf karşılığı (0–100)")
notu = int(input("Puan (0-100): "))
if notu >= 90:
    print("AA")
elif notu >= 80:
    print("BA")
elif notu >= 70:
    print("BB")
elif notu >= 60:
    print("CB")
elif notu >= 50:
    print("CC")
else:
    print("FF")

print("\n[3] Kullanıcı doğrulama")
k_adi = input("Kullanıcı adı: ")
sifre = input("Şifre: ")
# Örnek sabitler (gerçekte dosyadan/DB'den gelir)
dogru_ad = "kaan"
dogru_sifre = "1234"
if (k_adi == dogru_ad) and (sifre == dogru_sifre):
    print("giriş başarılı")
else:
    print("hatalı kullanıcı adı veya şifre")

print("\n[4] Metinde 'python' geçiyor mu? (case-insensitive)")
metin = input("Metin: ")
if "python" in metin.lower():
    print("bulundu")
else:
    print("yok")

print("\n[5] 2 ve 3'e aynı anda bölünebilirlik")
sayi2 = int(input("Sayı gir (2): "))
if (sayi2 % 2 == 0) and (sayi2 % 3 == 0):
    print("OK (hem 2 hem 3)")
else:
    print("YOK")

# ---------------------------------
# 🧠 NOTLAR
# - if/elif/else sıralı çalışır; ilk sağlanan koşul yürür.
# - and/or/not kısa devre yapar; ikinci taraf gerekirse değerlendirilir.
# - 'in' üyelik kontrolü; 'is' kimlik kontrolü (None denetimi için kullan).
# - 1 < n < 10 zincirli karşılaştırma, Python’a özgü kısalık sağlar.
# - Ternary: x if koşul else y — tek satır karar.
# - Boş değerler False kabul edilir; koşullarda doğrudan kullanılabilir.
# ---------------------------------
