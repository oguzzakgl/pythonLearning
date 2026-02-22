# Konu: String Temelleri
# Amaç: String uzunluğu, arama, döngü ile gezme ve temel işlemler.

metin = "Merhaba Python dünyası"

# 1) Uzunluk
uz = len(metin)
print("Uzunluk:", uz)  # karakter sayısı (boşluklar dahil)

# 2) Arama (bulma)
print("Bul 'Py':", metin.find("Py"))      # varsa başlangıç indeksi, yoksa -1
print("Kaç 'a' var:", metin.count("a"))   # toplam eşleşme sayısı
print("'Mer' ile başlar mı:", metin.startswith("Mer"))
print("'yası' ile biter mi:", metin.endswith("yası"))
print("'Python' içinde mi:", "Python" in metin)  # membership

# 3) Döngü ile karakter gezme
sayaç_sesli = 0
sesliler = "aeıioöuüAEIİOÖUÜ"

for ch in metin:
    if ch in sesliler:
        sayaç_sesli += 1
print("Sesli harf sayısı:", sayaç_sesli)

# 4) Döngü + indeks (enumerate)
for i, ch in enumerate(metin):
    if ch == "a":
        print("a bulundu, indeks:", i)

# 5) Kelime kelime gezinme
kelimeler = metin.split()           # boşluğa göre ayır
for k in kelimeler:
    print("Kelime:", k, "- Uzunluk:", len(k))

# 6) İlk geçen alt dizenin tüm konumlarını bulma (manuel)
aranan = "an"
i = 0
while True:
    i = metin.find(aranan, i)
    if i == -1:
        break
    print(f"'{aranan}' bulundu indeks:", i)
    i += 1  # bir sonraki konumdan devam

# ---------------------------------
# 🧠 NOTLAR
# - len(s) tüm karakterleri sayar (boşluklar dahil).
# - find() yoksa -1 döner; index() yoksa hata fırlatır.
# - count() örtüşmeyen eşleşmeleri sayar.
# - startswith/endswith hızlı ön/son kontrolüdür.
# - "alt" in s → True/False membership testi.
# - enumerate(s) ile (indeks, karakter) döner.
# - while + find(start) ile tüm konumları tarayabilirsin.