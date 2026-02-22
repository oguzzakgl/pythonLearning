# Konu: String Alıştırmaları
# Amaç: String metotlarını ve işlemlerini pekiştirmek için karışık örnekler.

import random

# 1) Ad-soyad düzeltme (strip + title)
ad = input("Ad: ")
soyad = input("Soyad: ")
print(f"{ad.strip().title()} {soyad.strip().title()} hoş geldiniz")

# 2) Metinde 'Python' arama: indeks veya -1
text = " Python is doing well "
idx = text.find("Python")          # yoksa -1 döner
print("Indeks:", idx)
if "Python" in text:
    print("Evet, 'Python' metin içinde bulunuyor.")
else:
    print("Hayır, 'Python' metin içinde bulunmuyor.")

# 3) "1,321" → "1.321" → float
number = "1,321"                    # string olmalı, tuple yapma
print(float(number.replace(",", ".")))

# 4) 1..100 içinden 5 tekrarsız sayı
print(sorted(random.sample(range(1, 101), 5)))

# 5) "Veri Bilimi" → "Veri-Bilimi"
text2 = "Veri Bilimi"
print(text2.title().replace(" ", "-"))  # Veri-Bilimi

# 6) Bonus: A..Z üret ve birleştir
harfler = [chr(k) for k in range(ord('A'), ord('Z')+1)]
print("".join(harfler))
