# Konu: Python Veri Koleksiyonları (List, Tuple, Set, Dict)
# Amaç: Temel veri yapılarının (List, Tuple, Set, Dict) özellikleri, farkları ve kullanım alanları.

# --- Python'un Temel Veri Koleksiyonları: List, Tuple, Set, Dict ---

print("--- 1. BÖLÜM: Liste (List) ---")
# -----------------------------------
# Tanım: Python'daki en esnek ve en yaygın kullanılan veri koleksiyonudur.
# Özellikler:
# 1. Gösterim: Köşeli parantez [ ] ile oluşturulur.
# 2. Sıralıdır (Ordered): Öğeler eklendikleri sırada kalır ve indeks (0, 1, 2...) ile erişilir.
# 3. Değiştirilebilir (Mutable): Oluşturulduktan sonra içeriği (öğeler) değiştirilebilir, eklenebilir veya silinebilir.
# 4. Yinelenen Değerlere İzin Verir: Aynı öğeyi birden fazla kez içerebilir.

# 1.1. Liste Oluşturma
meyveler_listesi = ["elma", "armut", "kiraz", "elma"] # "elma" yineleniyor
print(f"Orijinal Liste: {meyveler_listesi}")

# 1.2. Öğeye Erişim (İndeks ile)
# İndeksler 0'dan başlar
print(f"İlk öğe (indeks 0): {meyveler_listesi[0]}") # Çıktı: elma
print(f"Son öğe (indeks -1): {meyveler_listesi[-1]}") # Çıktı: elma

# 1.3. Değiştirme (Mutable)
# 'armut' yerine 'vişne' atayalım (indeks 1)
meyveler_listesi[1] = "vişne"
print(f"Değiştirilmiş Liste: {meyveler_listesi}")

# 1.4. Öğle Ekleme (.append() ile sona ekler)
meyveler_listesi.append("çilek")
print(f"Ekleme yapılmış Liste: {meyveler_listesi}")

# 1.5. Öğle Silme (.remove() ile değeri siler)
meyveler_listesi.remove("elma") # Bulduğu İLK "elma"yı siler
print(f"Silme yapılmış Liste: {meyveler_listesi}")

# 1.6. Uzunluk Kontrolü
print(f"Listenin mevcut uzunluğu: {len(meyveler_listesi)}")


print("\n" + "-" * 40 + "\n") # Ayraç


print("--- 2. BÖLÜM: Tuple (Demet) ---")
# ------------------------------------
# Tanım: "Değiştirilemez" (sabit) bir listedir.
# Özellikler:
# 1. Gösterim: Normal parantez ( ) ile oluşturulur.
# 2. Sıralıdır (Ordered): Tıpkı listeler gibi öğelerin bir sırası ve indeksi vardır.
# 3. Değiştirilemez (Immutable): Oluşturulduktan sonra ASLA değiştirilemez. Ekleme, silme veya güncelleme yapılamaz.
# 4. Yinelenen Değerlere İzin Verir: Aynı öğeyi birden fazla kez içerebilir.

# 2.1. Tuple Oluşturma
# Genellikle (x, y) koordinatları, sabit ayarlar gibi veriler için kullanılır
koordinatlar_tuple = (10.5, 20.0, 10.5) # 10.5 yineleniyor
# Tek öğeli tuple oluşturmak için sona virgül koymak zorunludur: tek_ogeli = (10,)
print(f"Orijinal Tuple: {koordinatlar_tuple}")

# 2.2. Öğeye Erişim (İndeks ile)
print(f"X koordinatı (indeks 0): {koordinatlar_tuple[0]}") # Çıktı: 10.5

# 2.3. Değiştirme Girişimi (HATA verir)
# Aşağıdaki satırların yorumunu kaldırırsanız program 'TypeError' hatası vererek çöker.
# koordinatlar_tuple[0] = 15.0 # HATA! 'tuple' object does not support item assignment
# koordinatlar_tuple.append(5.0) # HATA! 'tuple' object has no attribute 'append'

print("Tuple değiştirilemez, bu yüzden ekleme/silme/güncelleme yapılamaz.")

# 2.4. Kullanım Alanı
# İçeriğinin değişmeyeceğinden emin olmak istediğimizde kullanırız.
# Listelerden biraz daha hızlıdırlar.


print("\n" + "-" * 40 + "\n") # Ayraç


print("--- 3. BÖLÜM: Set (Küme) ---")
# ---------------------------------
# Tanım: Matematikteki "kümeler" gibidir. Temel özelliği benzersiz (tekrarsız) olmasıdır.
# Özellikler:
# 1. Gösterim: Süslü parantez { } ile oluşturulur (ancak sözlükten farklıdır).
# 2. Sırasızdır (Unordered): Öğelerin belirli bir sırası veya indeksi YOKTUR. (Bu nedenle indeksle erişilemez).
# 3. Değiştirilebilir (Mutable): Kümeye yeni öğeler ekleyebilir veya çıkarabilirsiniz.
# 4. Yinelenen Değerlere İzin VERMEZ: Bir öğeyi birden fazla kez eklerseniz bile sadece bir kopyasını tutar.

# 3.1. Set Oluşturma (Yinelenenler otomatik atılır)
sayilar_seti = {10, 20, 30, 20, 10, 40, 50}
print(f"Orijinal Set: {sayilar_seti}") # Çıktı: {10, 20, 30, 40, 50} (Sırası garanti değildir)

# 3.2. Öğeye Erişim (İndeks ile YAPILAMAZ)
# Aşağıdaki satırın yorumunu kaldırırsanız 'TypeError' hatası verir.
# print(sayilar_seti[0]) # HATA! 'set' object is not subscriptable

# 3.3. Öğle Kontrolü ('in' operatörü ile)
# Bir öğenin kümede olup olmadığını kontrol etmenin en hızlı yoludur.
print(f"30, bu sette var mı? : {30 in sayilar_seti}") # Çıktı: True
print(f"99, bu sette var mı? : {99 in sayilar_seti}") # Çıktı: False

# 3.4. Öğle Ekleme (.add() ile)
sayilar_seti.add(60)
sayilar_seti.add(10) # 10 zaten var, hiçbir şey değişmez
print(f"Ekleme yapılmış Set: {sayilar_seti}")

# 3.5. Öğle Silme (.remove() ile)
sayilar_seti.remove(20) # 20'yi siler
print(f"Silme yapılmış Set: {sayilar_seti}")

# 3.6. Kullanım Alanı: Yinelenenleri Temizleme
bir_liste = [1, 1, 2, 2, 3, 4, 5, 5, 5, 6]
temiz_set = set(bir_liste)
print(f"Listeden {bir_liste} oluşturulan temiz set: {temiz_set}")


print("\n" + "-" * 40 + "\n") # Ayraç


print("--- 4. BÖLÜM: Dictionary (Sözlük - Dict) ---")
# ------------------------------------------------
# Tanım: Verileri 'Anahtar: Değer' (Key: Value) çiftleri halinde saklar.
# Özellikler:
# 1. Gösterim: Süslü parantez { } içinde anahtar:değer çiftleri ile oluşturulur.
# 2. Sıralıdır (Ordered): (Python 3.7 ve sonrası için) Eklendikleri sırada kalırlar.
# 3. Değiştirilebilir (Mutable): Öğeler eklenebilir, silinebilir ve güncellenebilir.
# 4. Benzersiz Anahtarlar (Keys): Anahtarlar benzersiz olmalıdır. Değerler (Values) yinelenebilir.

# 4.1. Sözlük Oluşturma
# Verilere etiket (anahtar) vererek saklamak için kullanılır.
kullanici_bilgileri = {
    "kullanici_adi": "ahmet123",
    "yas": 30,
    "email": "ahmet@mail.com",
    "aktif_mi": True,
    "notu": 80
}
print(f"Orijinal Sözlük: {kullanici_bilgileri}")

# 4.2. Değere Erişim (İndeks yerine ANAHTAR ile)
print(f"Kullanıcının yaşı: {kullanici_bilgileri['yas']}") # Çıktı: 30
# Alternatif yol: .get() metodu (Anahtar yoksa hata vermez, None döner)
print(f"Kullanıcının emaili: {kullanici_bilgileri.get('email')}")
print(f"Kullanıcının şehri: {kullanici_bilgileri.get('sehir')}") # Çıktı: None

# 4.3. Değer Değiştirme
kullanici_bilgileri["yas"] = 31 # 'yas' anahtarının değerini güncelle
print(f"Değiştirilmiş Sözlük (yaş güncellendi): {kullanici_bilgileri}")

# 4.4. Yeni Anahtar-Değer Ekleme
kullanici_bilgileri["sehir"] = "Ankara" # Yeni bir anahtar ve değer ekle
print(f"Ekleme yapılmış Sözlük (şehir eklendi): {kullanici_bilgileri}")

# 4.5. Silme (del ile)
del kullanici_bilgileri["email"] # 'email' anahtarını ve değerini siler
print(f"Silme yapılmış Sözlük (email silindi): {kullanici_bilgileri}")

# 4.6. Anahtarlara veya Değerlere Bakma
print(f"Tüm Anahtarlar: {kullanici_bilgileri.keys()}")
print(f"Tüm Değerler: {kullanici_bilgileri.values()}")


# --- ÖZET KARŞILAŞTIRMA TABLOSU ---
#
# | Özellik                    | Liste (List)       | Tuple (Demet)    | Küme (Set)           | Sözlük (Dict)        |
# | :------------------------  | :----------------  | :--------------- | :------------------- | :------------------- |
# | Gösterim                   | [1, 2, 3]          | (1, 2, 3)        | {1, 2, 3}            | {"a": 1, "b": 2}   |
# | Değiştirilebilir? (Mutable)| ✅ Evet           | ❌ Hayır         | ✅ Evet              | ✅ Evet              |
# | Sıralı mı?                 | ✅ Evet           | ✅ Evet          | ❌ Hayır (İndekssiz) | ✅ Evet (3.7+)       |
# | Yinelenen Öğeler           | ✅ Evet           | ✅ Evet          | ❌ Hayır (Benzersiz) | ✅ (Değerler evet, Anahtarlar hayır) |
# | Erişim Yöntemi             | İndeks ile ([0])   | İndeks ile ([0]) | 'in' ile (İndeks yok)| Anahtar ile (['key'])|
#