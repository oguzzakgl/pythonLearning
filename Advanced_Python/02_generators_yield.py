# Konu: Generators ve Yield
# Amaç: Büyük verileri belleği (RAM) şişirmeden parça parça işlemek.

import sys # Bellek boyutunu ölçmek için

# ---------------------------------------------------------
# 1. NORMAL FONKSİYON (RETURN)
# ---------------------------------------------------------
# Return, işlemi bitirir ve sonucu topluca verir.
# Sanki restoranda 1000 kişilik yemeği tek seferde masaya koymak gibi.

def normal_liste_olustur(adet):
    sonuc = []
    for i in range(adet):
        sonuc.append(i) # Hepsini hafızaya atıyor
    return sonuc

print("--- Normal Fonksiyon ---")
liste = normal_liste_olustur(5)
print(f"Liste: {liste}")


# ---------------------------------------------------------
# 2. GENERATOR FONKSİYONU (YIELD)
# ---------------------------------------------------------
# Yield, "Al bunu, ben diğerini hazırlayana kadar işini gör" der.
# İşlemi duraklatır, değeri verir, sonra kaldığı yerden devam eder.
# Sanki restoranda tabakları tek tek servis etmek gibi.

def generator_olustur(adet):
    for i in range(adet):
        yield i # Değeri üretir ve beklemeye geçer

print("\n--- Generator Fonksiyonu ---")
gen = generator_olustur(5)
print(f"Generator Objesi: {gen}") # Direkt listeyi göremezsin, o bir "üretici"dir.

# İçindeki değerleri almak için ya döngüye sokarsın ya da next() dersin.
print("Değerler:")
for sayi in gen:
    print(sayi)


# ---------------------------------------------------------
# 3. GENERATOR EXPRESSION (LİST COMPREHENSION İLE İLİŞKİSİ)
# ---------------------------------------------------------
# Soru: List Comprehension içinde yield kullanılır mı?
# Cevap: Hayır, ama List Comprehension'ı Generator'a dönüştürebilirsin.
# Tek yapman gereken KÖŞELİ PARANTEZ [] yerine NORMAL PARANTEZ () kullanmak.

print("\n--- Generator Expression ---")

# List Comprehension (Hepsini üretir, hafızaya atar)
liste_comp = [x*2 for x in range(5)] 
print(f"Liste Comp: {liste_comp}")

# Generator Expression (İhtiyaç oldukça üretir)
# Sanki içinde gizli bir 'yield' varmış gibi çalışır.
gen_comp = (x*2 for x in range(5)) 
print(f"Gen Comp: {gen_comp}")

print("Gen Comp Değerleri:")
for sayi in gen_comp:
    print(sayi)


# ---------------------------------------------------------
# 4. NEDEN KULLANALIM? (BELLEK FARKI)
# ---------------------------------------------------------
print("\n--- BELLEK (RAM) TESTİ ---")

# 1 Milyon sayı üretelim
buyuk_sayi = 1000000

# Normal Liste: Hepsini RAM'de tutar
normal_list = [i for i in range(buyuk_sayi)]
print(f"Normal Liste Boyutu: {sys.getsizeof(normal_list)} bytes")

# Generator: Sadece sıradaki sayıyı tutar (Formülü tutar)
generator_list = (i for i in range(buyuk_sayi)) # Köşeli parantez yerine normal parantez!
print(f"Generator Boyutu:  {sys.getsizeof(generator_list)} bytes")

# SONUÇ: Generator milyonlarca veri olsa bile hep aynı az yeri kaplar.
