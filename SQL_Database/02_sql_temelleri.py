# KONU: SQL (Structured Query Language) Temelleri - 0'dan
# Amaç: Veritabanı dünyasına giriş. Tablo nedir? Veri nasıl eklenir ve çekilir?

import sqlite3

print("--- SQL DERSİ BAŞLIYOR ---")

# 1. BAĞLANTI KURMA
# ------------------------------------------------------------------
# Bir dosya oluşturur (okul.db) ve ona bağlanır.
# Eğer dosya varsa bağlanır, yoksa oluşturur.
baglanti = sqlite3.connect("okul.db")
cursor = baglanti.cursor() # İmleç (Veritabanı üzerinde işlem yapan araç)

# 2. TABLO OLUŞTURMA (CREATE TABLE)
# ------------------------------------------------------------------
# Öğrenciler diye bir tablomuz olsun. İsim (Metin) ve Numara (Sayı) tutsun.
# "IF NOT EXISTS" -> Eğer tablo zaten varsa hata verme demektir.
cursor.execute("CREATE TABLE IF NOT EXISTS ogrenciler (isim TEXT, numara INTEGER, notu INTEGER)")

# 3. VERİ EKLEME (INSERT INTO)
# ------------------------------------------------------------------
# Tek Tek Ekleme
cursor.execute("INSERT INTO ogrenciler VALUES ('Ali', 101, 85)")
cursor.execute("INSERT INTO ogrenciler VALUES ('Veli', 102, 40)")

# Çoklu Ekleme (Liste ile)
yeni_ogrenciler = [
    ('Ayşe', 103, 95),
    ('Fatma', 104, 60),
    ('Mehmet', 105, 55)
]
cursor.executemany("INSERT INTO ogrenciler VALUES (?, ?, ?)", yeni_ogrenciler)

# Değişiklikleri Kaydet (Commit çok önemlidir, unutursan silinir!)
baglanti.commit()
print("✅ Veriler eklendi ve kaydedildi.")

# 4. VERİ ÇEKME (SELECT)
# ------------------------------------------------------------------
print("\n--- TÜM LİSTE ---")
# "*" işareti "Her şeyi getir" demektir.
cursor.execute("SELECT * FROM ogrenciler") 
tum_kayitlar = cursor.fetchall() # Hepsini alıp listeye koyar

for kayit in tum_kayitlar:
    print(kayit)

# 5. FİLTRELEME (WHERE)
# ------------------------------------------------------------------
print("\n--- SADECE GEÇENLER (Notu > 50) ---")
# "WHERE" şart demektir.
cursor.execute("SELECT * FROM ogrenciler WHERE notu > 50")
gecenler = cursor.fetchall()

for kayit in gecenler:
    print(f"Tebrikler: {kayit[0]} - Not: {kayit[2]}")

# Bağlantıyı kapat
baglanti.close()
