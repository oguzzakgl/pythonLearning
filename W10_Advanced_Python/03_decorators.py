# Konu: Decorators (Dekoratörler)
# Amaç: Bir fonksiyonun kodunu değiştirmeden, ona yeni özellikler eklemek.
# Analoji: Bir hediye kutusunu (fonksiyonu) alıp, süslü bir pakete (decorator) sarmak gibi.

import time

# ---------------------------------------------------------
# 1. DECORATOR NEDİR? (MANTIK)
# ---------------------------------------------------------
# Decorator, bir fonksiyonu parametre olarak alan ve
# geriye yeni (geliştirilmiş) bir fonksiyon döndüren fonksiyondur.

def susleyici(fonksiyon):
    def wrapper(): # Paketleme (Sarma) işlemi
        print("--- 🎀 Paketleme Başladı ---")
        fonksiyon() # Asıl fonksiyonu çalıştır
        print("--- 🎀 Paketleme Bitti ---")
    return wrapper

# ---------------------------------------------------------
# 2. @ İŞARETİ OLMADAN KULLANIM (ESKİ YÖNTEM)
# ---------------------------------------------------------
def hediye():
    print("🎁 Hediye: Oyuncak Araba")

print("1. Normal Çağırma:")
hediye()

print("\n2. Süsleyerek Çağırma:")
suslu_hediye = susleyici(hediye) # Fonksiyonu süsleyiciye gönderdik
suslu_hediye()


# ---------------------------------------------------------
# 3. @ İŞARETİ İLE KULLANIM (MODERN YÖNTEM)
# ---------------------------------------------------------
# @susleyici yazmak, "bu fonksiyonu al, susleyici'ye gönder" demektir.

@susleyici
def pasta():
    print("🎂 Pasta: Çikolatalı Pasta")

print("\n3. Decorator (@) ile Çağırma:")
pasta() # Artık otomatik olarak süslü çalışır!


# ---------------------------------------------------------
# 4. GERÇEK HAYAT ÖRNEĞİ: ZAMAN ÖLÇME
# ---------------------------------------------------------
# Bir fonksiyonun ne kadar sürdüğünü ölçen bir decorator yazalım.

def zaman_olcer(func):
    def wrapper(*args, **kwargs): # Her türlü parametreyi kabul et
        baslangic = time.time()
        print(f"\n⏱️  '{func.__name__}' fonksiyonu çalışıyor...")
        
        sonuc = func(*args, **kwargs) # Asıl fonksiyonu çalıştır
        
        bitis = time.time()
        print(f"✅ Bitti! Süre: {bitis - baslangic:.5f} saniye")
        return sonuc
    return wrapper

@zaman_olcer
def islem_yap(sayi):
    time.sleep(1) # 1 saniye bekle (işlem yapıyormuş gibi)
    return sayi * sayi

print("\n4. Gerçek Hayat Örneği (Zaman Ölçer):")
islem_yap(10)
