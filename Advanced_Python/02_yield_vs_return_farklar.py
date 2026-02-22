# =========================================================
# 🆚 YIELD vs RETURN: NASIL AYIRT EDERİM?
# =========================================================

# 1. GÖRÜNÜŞ (SYNTAX) FARKI
# ---------------------------------------------------------
# Normal Fonksiyon: İçinde 'return' kelimesi geçer.
# Generator:        İçinde 'yield' kelimesi geçer.

def normal():
    return 1  # Bitti, dükkanı kapatıp gider.

def generator():
    yield 1   # "Al bunu" der, dükkanı açık tutar, bekler.


# 2. ÇALIŞMA MANTIGI FARKI
# ---------------------------------------------------------
# Normal:  Fonksiyonu çağırdığında sana SONUCU (Listeyi, Sayıyı) verir.
# Generator: Fonksiyonu çağırdığında sana bir OBJE (Üreteç) verir.

sonuc = normal()
print(f"Normal Sonuç: {sonuc}") # Çıktı: 1

gen_obje = generator()
print(f"Generator Sonuç: {gen_obje}") # Çıktı: <generator object ...>
# İçindekini almak için 'next()' veya 'for' döngüsü gerekir.
print(f"Generator İçindeki: {next(gen_obje)}") # Çıktı: 1


# 3. HAFIZA (RAM) FARKI
# ---------------------------------------------------------
# Normal:  1 Milyon veriyi hafızaya yazar, sonra verir. (RAM Şişer)
# Generator: 1 Milyon veriyi hafızada tutmaz, istedikçe üretir. (RAM Rahat)


# 4. ÖZET TABLO
# ---------------------------------------------------------
# | Özellik        | Normal (Return)       | Generator (Yield)    |
# |----------------|-----------------------|----------------------|
# | Anahtar Kelime | return                | yield                |
# | Ne Döndürür?   | Listenin tamamı       | Bir tane "Obje"      |
# | Hafıza         | Çok yer kaplar        | Çok az yer kaplar    |
# | Hız            | Bekletir (Hepsini yapar)| Bekletmez (Anında) |
# | Tekrar         | Tek seferliktir       | next() ile devam eder|
