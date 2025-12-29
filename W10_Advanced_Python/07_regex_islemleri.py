# Konu: Regex (Düzenli İfadeler - Regular Expressions)
# Amaç: Metin içinde belirli kalıpları (pattern) bulmak ve işlemek.
# Kullanım Alanı: E-mail bulma, telefon numarası bulma, veri temizleme.

import re

# ---------------------------------------------------------
# 1. TEMEL ARAMA (search)
# ---------------------------------------------------------
# Bir metin içinde belirli bir kelime var mı?

metin = "Python öğrenmek çok eğlenceli!"
sonuc = re.search("Python", metin)

if sonuc:
    print(f"Bulundu! Konum: {sonuc.start()}-{sonuc.end()}")
else:
    print("Bulunamadı.")


# ---------------------------------------------------------
# 2. TÜM EŞLEŞMELERİ BULMA (findall)
# ---------------------------------------------------------
# Metindeki tüm sayıları bul

metin2 = "Ali 25 yaşında, Ayşe 30 yaşında, Mehmet 28 yaşında."
sayilar = re.findall(r"\d+", metin2)  # \d+ = bir veya daha fazla rakam
print(f"\nBulunan Sayılar: {sayilar}")


# ---------------------------------------------------------
# 3. E-MAİL BULMA (Gerçek Hayat Örneği)
# ---------------------------------------------------------
# Bir metindeki tüm e-mail adreslerini bul

metin3 = """
İletişim: ali@gmail.com veya ayse@hotmail.com
Destek: info@firma.com.tr
"""

# Basit e-mail pattern'i
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
emailler = re.findall(email_pattern, metin3)
print(f"\nBulunan E-mailler: {emailler}")


# ---------------------------------------------------------
# 4. DEĞİŞTİRME (sub)
# ---------------------------------------------------------
# Metindeki tüm sayıları "X" ile değiştir

metin4 = "Telefon: 0555 123 45 67"
gizli = re.sub(r"\d", "X", metin4)
print(f"\nGizlenmiş: {gizli}")


# ---------------------------------------------------------
# 5. TELEFON NUMARASI BULMA
# ---------------------------------------------------------
# Türk telefon numarası formatı: 05XX XXX XX XX

metin5 = "Beni ara: 0532 123 45 67 veya 0555 987 65 43"
telefon_pattern = r"05\d{2}\s\d{3}\s\d{2}\s\d{2}"
telefonlar = re.findall(telefon_pattern, metin5)
print(f"\nBulunan Telefonlar: {telefonlar}")
