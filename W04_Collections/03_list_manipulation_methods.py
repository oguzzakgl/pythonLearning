# Konu: Liste Metotları (Silme, Bulma, Sayma)
# Amaç: remove, pop, del, clear ile silme; index, count ile arama işlemleri.

# --- Python Liste Metotları (Silme, Bulma, Sayma) ---

# Bu örnekte, bir listeden öğeleri nasıl sileceğimizi (remove, pop, del, clear)
# ve öğeleri nasıl arayacağımızı (index, count) göreceğiz.

# Örnek listemizi hazırlayalım:
# Bu listeyi aşağıdaki tüm metotları test etmek için kullanacağız.
hayvanlar = ["kedi", "köpek", "kuş", "balık", "köpek", "at"]
print(f"Listenin Orijinal Hali: {hayvanlar}")
print("=" * 40)


# --- 1. remove(deger) Metodu (Değere Göre Silme) ---
# Listede aradığı DEĞERİ bulur ve bulduğu İLK eşleşmeyi siler.
# Eğer değeri listede bulamazsa 'ValueError' hatası verir.
# Değeri DÖNDÜRMEZ, sadece siler.

print("--- 1. remove() ---")
# Listede iki tane "köpek" var. remove() sadece ilk bulduğunu (indeks 1) siler.
try:
    hayvanlar.remove("köpek")
    print(f"'köpek' silindikten sonra: {hayvanlar}")
except ValueError:
    print("Hata: Silmek istediğiniz değer listede bulunamadı.")

# Var olmayan bir şeyi silmeye çalışmak (Hata örneği):
try:
    hayvanlar.remove("tavşan")
except ValueError:
    print(f"'tavşan' listede bulunamadı, bu yüzden ValueError verdi.")
print("-" * 30)


# --- 2. pop(indeks) Metodu (İndekse Göre Silme ve Döndürme) ---
# Belirtilen İNDEKSteki öğeyi listeden SİLER ve sildiği öğeyi DÖNDÜRÜR.
# Bu sayede silinen öğeyi bir değişkende saklayabilirsiniz.
# Eğer 'pop()' içine indeks yazmazsanız, listenin SONUNDAKİ öğeyi siler.

print("--- 2. pop() ---")
# 'hayvanlar' listesinin güncel hali: ['kedi', 'kuş', 'balık', 'köpek', 'at']

# 2. indeksteki öğeyi ('balık') silelim ve saklayalım:
silinen_oge = hayvanlar.pop(2)
print(f"2. indeksten silinen öğe: {silinen_oge}")
print(f"'pop(2)' sonrası liste: {hayvanlar}")

# Parametresiz pop() kullanarak sondaki öğeyi ('at') silelim:
son_oge = hayvanlar.pop()
print(f"Sondan silinen öğe: {son_oge}")
print(f"'pop()' sonrası liste: {hayvanlar}")
print("-" * 30)


# --- 3. del Anahtar Kelimesi (Silme) ---
# 'del', bir metot değil, Python'un bir anahtar kelimesidir.
# 'pop' gibi indekse göre siler ama sildiği değeri DÖNDÜRMEZ.
# En büyük gücü, belirli bir İNDEKSi veya DİLİMİ (slice) silebilmesidir.

print("--- 3. del ---")
# 'hayvanlar' listesinin güncel hali: ['kedi', 'kuş', 'köpek']
sayilar = [10, 20, 30, 40, 50, 60]
print(f"'sayilar' listesi: {sayilar}")

# Tek bir indeksi silme (indeks 1, yani 20):
del sayilar[1]
print(f"'del sayilar[1]' sonrası: {sayilar}")

# Bir dilimi (slice) silme (indeks 2'den 4'e kadar; 40 ve 50):
# Güncel liste: [10, 30, 40, 50, 60]
del sayilar[2:4]
print(f"'del sayilar[2:4]' sonrası: {sayilar}") # Çıktı: [10, 30, 60]

# Değişkeni bellekten tamamen silme:
# del sayilar
# print(sayilar) # Bu satır çalıştırılırsa 'NameError' verir çünkü 'sayilar' artık yok.
print("-" * 30)


# --- 4. clear() Metodu (Listeyi Temizleme) ---
# Listenin KENDİSİNİ silmez, içindeki TÜM ÖĞELERİ siler.
# Sonuç olarak boş bir liste '[]' elde edilir.

print("--- 4. clear() ---")
gunler = ["Pazartesi", "Salı", "Çarşamba"]
print(f"'gunler' listesi: {gunler}")
gunler.clear()
print(f"'gunler.clear()' sonrası: {gunler}") # Çıktı: []
print("-" * 30)


# --- 5. index(deger) Metodu (İndeks Bulma) ---
# Bir DEĞERİN listede bulunduğu İLK İNDEKSİ döndürür.
# Eğer değeri listede bulamazsa 'ValueError' hatası verir.

print("--- 5. index() ---")
harfler = ['a', 'b', 'c', 'd', 'b', 'e']
print(f"'harfler' listesi: {harfler}")

# 'c' harfinin indeksini bulalım:
indeks_c = harfler.index('c')
print(f"'c' harfinin indeksi: {indeks_c}") # Çıktı: 2

# 'b' harfinin İLK indeksini bulalım:
indeks_b = harfler.index('b')
print(f"'b' harfinin İLK indeksi: {indeks_b}") # Çıktı: 1 (4 değil)

# Olmayan bir öğeyi aramak (Hata örneği):
try:
    harfler.index('z')
except ValueError:
    print(f"'z' harfi listede bulunamadı, bu yüzden ValueError verdi.")
print("-" * 30)


# --- 6. count(deger) Metodu (Sayma) ---
# Bir DEĞERİN liste içinde toplam KAÇ TANE olduğunu sayar.
# Değer listede olmasa bile hata VERMEZ, '0' (sıfır) döndürür.

print("--- 6. count() ---")
# 'harfler' listesi: ['a', 'b', 'c', 'd', 'b', 'e']

# 'b' harfinin sayısını bulalım:
b_sayisi = harfler.count('b')
print(f"'b' harfi listede {b_sayisi} kez geçiyor.") # Çıktı: 2

# 'a' harfinin sayısını bulalım:
a_sayisi = harfler.count('a')
print(f"'a' harfi listede {a_sayisi} kez geçiyor.") # Çıktı: 1

# 'z' harfinin sayısını bulalım:
z_sayisi = harfler.count('z')
print(f"'z' harfi listede {z_sayisi} kez geçiyor.") # Çıktı: 0
print("=" * 40)


# --- ÖZET: Silme Yöntemleri Arasındaki Farklar ---
# remove('değer'): Değere göre siler.
# pop(indeks): İndekse göre siler ve sildiği öğeyi döndürür.
# del liste[indeks]: İndekse/Dilime göre siler ve bir şey döndürmez.
# clear(): Listenin tamamının içini boşaltır.