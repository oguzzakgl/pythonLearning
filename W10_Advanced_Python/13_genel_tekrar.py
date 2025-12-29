import time

# =========================================================
# 🔁 GENEL TEKRAR (ADIM ADIM)
# =========================================================
# Şu ana kadar öğrendiğimiz 7 konuyu sırayla pekiştireceğiz.
# Adım adım genel tekrar

# ---------------------------------------------------------
# KONU 1: LIST COMPREHENSIONS
# ---------------------------------------------------------
# Soru: Elimizde karışık bir veri listesi var.
# 1. Sadece sayıları (int) al.
# 2. Bu sayıların karesini al.
# 3. List Comprehension kullanarak tek satırda yap.

veriler = ["Ali", 10, "Veli", 5, True, 8, "Python", 3]

metinler = [x for x in veriler if isinstance(x, str)]
sayilar = [x for x in veriler if isinstance(x, int) and not isinstance(x, bool)]
kareler = [x**2 for x in sayilar]

print(f"Metinler: {metinler}")
print(f"Sayılar: {sayilar}")
print(f"Kareler: {kareler}")    


# Beklenen Sonuç: [100, 25, 64, 9]
# kareler = [ ... KODU BURAYA YAZ ... ]


# ---------------------------------------------------------
# KONU 2: GENERATORS (YIELD)
# ---------------------------------------------------------
# Soru: 1'den 10'a kadar olan sayıların karesini üreten bir Generator yaz.
# Yield kullanımı
# Sonra bu generator'ı bir döngü ile yazdır.

def kare_ureteci():
    for i in range(1, 11):
        # time.sleep(2)
        yield i**2

print("\n--- Generator Testi ---")
for sayi in kare_ureteci():
    print(sayi)


# ---------------------------------------------------------
# KONU 3: DECORATORS (@)
# ---------------------------------------------------------
# Soru: Bir fonksiyonun kaç saniye sürdüğünü ölçen bir decorator yaz.
# Zaman ölçümü

def zaman_olcer(func):
    def wrapper():
        baslangic = time.time()
        func()
        bitis = time.time()
        print(f"{func.__name__} fonksiyonu {bitis - baslangic} saniye sürdü.")
    return wrapper

@zaman_olcer
def yavas_islem():
    time.sleep(2)
    print("İşlem tamamlandı!")

print("\n--- Decorator Testi ---")
yavas_islem()


# ---------------------------------------------------------
# KONU 4: ASYNC/AWAIT
# ---------------------------------------------------------
# Soru: 3 farklı "sunucudan" veri çeken asenkron fonksiyonlar yaz.
# Her sunucu farklı sürede yanıt versin (1, 2, 3 saniye).
# Hepsini AYNI ANDA çalıştır ve toplam süreyi ölç.

import asyncio

async def sunucu_1():
    await asyncio.sleep(1)  # 1 saniye bekle
    return "Sunucu 1 hazır"

async def sunucu_2():
    await asyncio.sleep(2)  # 2 saniye bekle
    return "Sunucu 2 hazır"

async def sunucu_3():
    await asyncio.sleep(3)
    return "Sunucu 3 hazır"


async def ana_program():
    baslangic = time.time()
    await asyncio.gather(
        sunucu_1(),
        sunucu_2(),
        sunucu_3()
    )
    
    bitis = time.time()
    print(f"Toplam Süre: {bitis - baslangic:.2f} saniye")

print("\n--- Async/Await Testi ---")
asyncio.run(ana_program())


# ---------------------------------------------------------
# KONU 5: TYPE HINTING
# ---------------------------------------------------------
# Soru: Aşağıdaki fonksiyona tip ipuçları ekle.
# Fonksiyon: İki sayıyı alıp toplamını döndürür.

def topla(a, b):
    return a + b

# Şimdi tip ipuçlarıyla yeniden yaz:
def topla_typed(a: int, b: int) -> int:
    return a + b

# Test:
sonuc = topla_typed(10, 20)
print(f"\n--- Type Hinting Testi ---")
print(f"Toplam: {sonuc}")


# ---------------------------------------------------------
# KONU 6: CONTEXT MANAGERS (with)
# ---------------------------------------------------------
# Soru: "test.txt" dosyasını aç ve içine "Merhaba Dünya" yaz.
# WITH kullanarak yap (otomatik kapanması için).



print("\n--- Context Manager Testi ---")
# ... KODU BURAYA YAZ ...
with open("test.txt", "w") as f:
    f.write("Merhaba Dünya")
print("Dosya yazıldı ve otomatik kapandı!")


# ---------------------------------------------------------
# KONU 7: MAGIC METHODS
# ---------------------------------------------------------
# Soru: Bir "Sayac" sınıfı yaz.
# - __init__: Başlangıç değerini alsın (varsayılan 0)
# - __str__: print() ile yazdırınca "Sayaç: X" yazsın
# - __add__: sayac1 + sayac2 işlemi iki sayacın değerini toplasın

class Sayac:
    # ... KODU BURAYA YAZ ...
    def __init__(self, baslangic=0):
        self.deger = baslangic
    
    def __str__(self):
        return f"Sayaç: {self.deger}"
    
    def __add__(self, diger):
        return Sayac(self.deger + diger.deger)

print("\n--- Magic Methods Testi ---")
s1 = Sayac(10)
s2 = Sayac(20)
print(s1)  # Sayaç: 10
print(s2)  # Sayaç: 20
s3 = s1 + s2
print(s3)  # Sayaç: 30
