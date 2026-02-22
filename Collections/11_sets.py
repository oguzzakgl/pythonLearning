# Konu: Küme (Set) Kapsamlı Örnek
# Amaç: Set veri yapısının benzersizlik, sırasızlık özellikleri ve küme işlemleri (birleşim, kesişim vb.).

# --- Python Küme (Set) Kapsamlı Örnek ---
# Amaç: 'set' veri yapısının "benzersiz" (unique) ve "indekssiz"
# olduğunu, nasıl değiştirilebildiğini ve küme işlemlerini görmektir.

# --- 1. Başlangıç (Benzersizlik Özelliği) ---
# 1. Başlangıç set'imizi oluşturalım.
# 'set'ler süslü parantez { } ile oluşturulur.
# DİKKAT: Yinelenen öğeler ("Moda", 10) otomatik olarak atılır.
kategoriler = {"Elektronik", "Moda", "Kitap", "Moda", 10, "Ev", 10}

# Çıktıda "Moda" ve 10 sadece BİR kez yer alacaktır.
print(f"1. Orijinal Set (Yinelenenler Atıldı): {kategoriler}")
# Not: Çıktı sırası sizin çalıştırdığınızdan farklı olabilir, çünkü set'ler SIRASIZDIR.
print("=" * 40)


# --- 2. Erişim Denemesi (İndeks YOKTUR) ---
print("--- 2. Erişim İşlemleri (Hata) ---")

# 2a. İndeks ile öğeye ERİŞİLEMEZ.
# 'set'lerin sırası olmadığı için [0] gibi bir kavram yoktur.
# Aşağıdaki satırın yorumunu kaldırırsanız 'TypeError' hatası alırsınız:
# print(kategoriler[0])
# TypeError: 'set' object is not subscriptable
print("  -> Set'lerde indeks yoktur, 'kategoriler[0]' HATA verir.")

# 2b. Doğru Erişim Yöntemi: 'in' ile kontrol
# Bir öğenin sette olup olmadığını 'in' ile kontrol ederiz.
print(f"  -> 'Moda' bu sette var mı? : {'Moda' in kategoriler}") # Çıktı: True
print(f"  -> 'Spor' bu sette var mı? : {'Spor' in kategoriler}") # Çıktı: False
print("=" * 40)


# --- 3. Ekleme İşlemleri (Set DEĞİŞECEK) ---
print("--- 3. Ekleme İşlemleri ---")

# 3a. 'add()' metodu ile sete BİR öğe eklenir.
print(f"  -> Önceki hali: {kategoriler}")
kategoriler.add("Müzik")
print(f"  -> add('Müzik') sonrası: {kategoriler}")
print("-" * 30)

# 3b. 'add()' ile ZATEN VAR OLAN bir öğeyi eklemeyi denemek
# "Moda" zaten sette olduğu için HİÇBİR ŞEY değişmez. Hata da vermez.
kategoriler.add("Moda")
print(f"  -> add('Moda') denendi (Değişiklik YOK): {kategoriler}")
print("=" * 40)


# --- 4. Silme İşlemleri (Set DEĞİŞECEK) ---
print("--- 4. Silme İşlemleri ---")

# 4a. 'remove()' ile DEĞERE göre silme
# Sette "Kitap" öğesini bulur ve siler.
print(f"  -> Önceki hali: {kategoriler}")
kategoriler.remove("Kitap")
print(f"  -> remove('Kitap') sonrası: {kategoriler}")
print("-" * 30)

# 4b. 'remove()' ile olmayan öğeyi silme (HATA Verir)
# 'remove()' metodu, olmayan bir öğeyi silmeye çalışırsa 'KeyError' verir.
# Aşağıdaki satırın yorumunu kaldırırsanız program çöker:
# kategoriler.remove("Sinema")
# KeyError: 'Sinema'
print("  -> remove('Sinema') denendi (Hata vermemesi için yorumda)...")
print("-" * 30)

# 4c. 'discard()' ile GÜVENLİ silme
# 'discard()', 'remove()' gibidir ancak öğe sette YOKSA hata VERMEZ.
kategoriler.discard("Sinema") # 'Sinema' yok, ama program çökmedi.
print(f"  -> discard('Sinema') denendi (Hata VERMEZ): {kategoriler}")
print("-" * 30)

# 4d. 'pop()' ile RASTGELE öğe silme
# 'set'ler sırasız olduğu için 'pop()' listenin sonundan değil,
# RASTGELE bir öğeyi siler ve sildiği öğeyi döndürür.
silinen_oge = kategoriler.pop()
print(f"  -> pop() ile silinen RASTGELE öğe: {silinen_oge}")
print(f"  -> pop() sonrası set: {kategoriler}")
print("=" * 40)


# --- 5. Küme İşlemleri (Set'lerin Asıl Gücü) ---
print("--- 5. Matematiksel Küme İşlemleri ---")
set_A = {1, 2, 3, 4}
set_B = {3, 4, 5, 6}
print(f"  -> Set A: {set_A}")
print(f"  -> Set B: {set_B}")

# 5a. Birleşim (Union |): İki setteki tüm benzersiz öğeler
birlesim = set_A | set_B
print(f"  -> Birleşim (A | B): {birlesim}") # Çıktı: {1, 2, 3, 4, 5, 6}

# 5b. Kesişim (Intersection &): İki sette ORTAK olan öğeler
kesisim = set_A & set_B
print(f"  -> Kesişim (A & B): {kesisim}") # Çıktı: {3, 4}

# 5c. Fark (Difference -): A'da olup B'de OLMAYAN öğeler
fark = set_A - set_B
print(f"  -> Fark (A - B): {fark}") # Çıktı: {1, 2}
print("=" * 40)


# --- 6. Set'i Temizleme ---
print("--- 6. Temizleme İşlemi ---")
kategoriler.clear()
print(f"  -> clear() sonrası set: {kategoriler}") # Çıktı: set()
print(kategoriler)
