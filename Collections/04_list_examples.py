# Konu: Liste (List) Kapsamlı Örnek
# Amaç: Listenin değiştirilebilir (mutable) yapısını; ekleme, silme, güncelleme ve sıralama ile göstermek.

# --- Python Liste (List) Kapsamlı Örnek - DEĞİŞTİRİLEBİLİRLİK ---

# Amaç: 'list' veri yapısının "değiştirilebilir" (mutable) olduğunu,
# yani içeriğinin eklenebilir, silinebilir, güncellenebilir ve
# sıralanabilir olduğunu adım adım görmektir.

# --- 1. Başlangıç ---
# 1. Başlangıç listemizi oluşturalım.
# 'list'ler köşeli parantez [ ] ile oluşturulur.
# İçinde yinelenen (tekrarlanan) öğeler olabilir.
gezegenler = ["Merkür", "Venüs", "Dünya", "Mars", "Jüpiter", "Dünya"]
print(f"1. Orijinal Liste: {gezegenler}")
print("=" * 40)


# --- 2. Erişim ve Okuma (Listeyi DEĞİŞTİRMEZ) ---
print("--- 2. Erişim ve Okuma İşlemleri ---")

# 2a. İndeks ile öğeye erişebiliriz
print(f"  -> 0. indeksteki gezegen: {gezegenler[0]}") # Çıktı: Merkür

# 2b. 'index' ile bir öğenin yerini bulabiliriz
print(f"  -> 'Mars' gezegeninin indeksi: {gezegenler.index('Mars')}") # Çıktı: 3

# 2c. 'count' ile bir öğenin kaç kez geçtiğini sayabiliriz
print(f"  -> 'Dünya' listede kaç kez geçiyor: {gezegenler.count('Dünya')}") # Çıktı: 2
print("=" * 40)


# --- 3. Ekleme İşlemleri (Liste DEĞİŞECEK) ---
print("--- 3. Ekleme İşlemleri ---")

# 3a. 'append()' metodu listenin SONUNA öğe ekler
print(f"  -> Önceki hali: {gezegenler}")
gezegenler.append("Satürn")
print(f"  -> append('Satürn') sonrası: {gezegenler}")
print("-" * 30)

# 3b. 'insert()' metodu BELİRLİ BİR İNDEKSE (araya) öğe ekler
# 1. indekse (Venüs'ün önüne) "ASTEROİD KUŞAĞI" ekleyelim
gezegenler.insert(1, "ASTEROİD KUŞAĞI")
print(f"  -> insert(1, ...) sonrası: {gezegenler}")
print("-" * 30)

# 3c. 'extend()' metodu listeye başka bir listeyi BİRLEŞTİRİR
diger_gezegenler = ["Uranüs", "Neptün"]
gezegenler.extend(diger_gezegenler)
print(f"  -> extend(...) sonrası: {gezegenler}")
print("=" * 40)


# --- 4. Güncelleme İşlemi (Liste DEĞİŞECEK) ---
print("--- 4. Güncelleme İşlemi ---")

# 4a. Öğeyi indeksi ile doğrudan GÜNCELLEME
# 1. indeksteki "ASTEROİD KUŞAĞI" yazımını düzeltelim
print(f"  -> Önceki hali (indeks 1): {gezegenler[1]}")
gezegenler[1] = "Asteroid Kuşağı" # 'ASTEROİD KUŞAĞI' yerine bunu atadık
print(f"  -> Güncelleme sonrası: {gezegenler}")
print("=" * 40)


# --- 5. Silme İşlemleri (Liste DEĞİŞECEK) ---
print("--- 5. Silme İşlemleri ---")

# 5a. 'remove()' ile DEĞERE göre silme (İlk bulduğunu siler)
# Listede 2 tane "Dünya" vardı. Bu komut sadece ilkini siler.
print(f"  -> Önceki hali: {gezegenler}")
gezegenler.remove("Dünya")
print(f"  -> remove('Dünya') sonrası: {gezegenler}")
print("-" * 30)

# 5b. 'pop()' ile İNDEKSE göre silme (ve sildiği öğeyi döndürme)
# 1. indeksteki "Asteroid Kuşağı"nı silelim
silinen_oge = gezegenler.pop(1)
print(f"  -> pop(1) ile silinen öğe: {silinen_oge}")
print(f"  -> pop(1) sonrası liste: {gezegenler}")
print("-" * 30)

# 5c. 'pop()' (parametresiz) ile SONDAN silme
# 'Neptün' gezegenini silecek
son_oge = gezegenler.pop()
print(f"  -> pop() ile sondan silinen: {son_oge}")
print(f"  -> pop() sonrası liste: {gezegenler}")
print("-" * 30)

# 5d. 'del' anahtar kelimesi ile İNDEKSE göre silme
# 0. indeksteki 'Merkür'ü silelim
print(f"  -> Önceki hali: {gezegenler}")
del gezegenler[0]
print(f"  -> del[0] sonrası: {gezegenler}")
print("=" * 40)


# --- 6. Sıralama ve Ters Çevirme (Liste DEĞİŞECEK) ---
print("--- 6. Sıralama İşlemleri ---")

# 6a. 'sort()' ile listeyi ALFABETİK olarak kalıcı sıralama
print(f"  -> Sıralamadan önce: {gezegenler}")
gezegenler.sort() # Kalıcı olarak sıralar
print(f"  -> sort() sonrası: {gezegenler}")
print("-" * 30)

# 6b. 'sort(reverse=True)' ile tersten sıralama
gezegenler.sort(reverse=True)
print(f"  -> sort(reverse=True) sonrası: {gezegenler}")
print("-" * 30)

# 6c. 'reverse()' ile listenin o anki sırasını ters çevirme
# (Bu alfabetik sıralamaz, sadece mevcut sırayı [Mars, ... Uranüs] tersine [Uranüs, ... Mars] çevirir)
gezegenler.reverse()
print(f"  -> reverse() sonrası: {gezegenler}")
print("=" * 40)


# --- 7. Kopyalama (Orijinali Korumak) ---
print("--- 7. Kopyalama İşlemi ---")
# 'copy()' metodu, listenin bağımsız bir kopyasını oluşturur.
# Bu sayede kopya üzerinde yapılan değişiklikler orijinali ETKİLEMEZ.
orijinal_liste_kopyasi = gezegenler.copy()
orijinal_liste_kopyasi.append("PLÜTON") # Sadece kopyaya ekledik
print(f"  -> Kopya liste: {orijinal_liste_kopyasi}")
print(f"  -> Orijinal liste: {gezegenler}") # Orijinal DEĞİŞMEDİ
print("=" * 40)


# --- 8. Listeyi Temizleme (Liste DEĞİŞECEK) ---
print("--- 8. Temizleme İşlemi ---")

# 8a. 'clear()' ile listenin İÇİNİ TAMAMEN boşaltma
print(f"  -> Temizlemeden önce: {gezegenler}")
gezegenler.clear()
print(f"  -> clear() sonrası: {gezegenler}") # Çıktı: []
print("=" * 40)

print("ÖZET: 'list' (liste) yapısı DEĞİŞTİRİLEBİLİR (mutable).")
print("Tüm ekleme, silme, güncelleme ve sıralama işlemleri kalıcı olarak listeyi etkiledi.")