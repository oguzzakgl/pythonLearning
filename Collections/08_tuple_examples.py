# Konu: Tuple (Demet) Kapsamlı Örnek
# Amaç: Tuple'ın değiştirilemez yapısını ve çalışan/çalışmayan metotları örneklerle göstermek.

# --- Python Tuple (Demet) Örneği - DEĞİŞTİRİLEMEZLİK ---

# 1. Başlangıç tuple'ımızı (demet) oluşturalım
# 'tuple'lar normal parantez () ile oluşturulur.
mevsimler = ("İlkbahar", "Yaz", "Sonbahar", "Kış")
print(f"Orijinal Tuple: {mevsimler}")
print("=" * 30)

# --- Tuple ile ÇALIŞAN İşlemler (Erişim) ---
# 'tuple'ın içeriğini okuyabiliriz, ancak değiştiremeyiz.

# 2. İndeks ile öğeye erişebiliriz (Tıpkı listedeki gibi)
print(f"0. indeksteki mevsim: {mevsimler[0]}") # Çıktı: İlkbahar

# 3. 'index' ile bir öğenin yerini bulabiliriz
print(f"'Yaz' mevsiminin indeksi: {mevsimler.index('Yaz')}") # Çıktı: 1

# 4. 'count' ile bir öğenin kaç kez geçtiğini sayabiliriz
print(f"'Kış' mevsimi kaç kez geçiyor: {mevsimler.count('Kış')}") # Çıktı: 1

print("=" * 30)


# --- Tuple ile ÇALIŞMAYAN İşlemler (HATA VERENLER) ---

# DİKKAT:
# Aşağıdaki kod satırlarının başındaki '#' yorum işaretini
# kaldırırsan, programın o satırda HATA VEREREK DURACAKTIR.
# Çünkü 'tuple'lar değiştirilemez.

# 5. 'del' ile 0. indeksi silmeyi deneme (Listenizde 'del fruits[0]' yapmıştınız)
print(f"Tuple'ın şu anki hali: {mevsimler}")
# del mevsimler[0]
# YUKARIDAKİ SATIRI ÇALIŞTIRIRSAN ALACAĞIN HATA:
# TypeError: 'tuple' object doesn't support item deletion
print("...del ile silme denendi (Hata vermemesi için kod yorumda)...")
print("-" * 30)


# 6. 'remove' metodunu deneme (Listenizde 'fruits.remove("cherry")' yapmıştınız)
print(f"Tuple'ın şu anki hali: {mevsimler}")
# mevsimler.remove("Yaz")
# YUKARIDAKİ SATIRI ÇALIŞTIRIRSAN ALACAĞIN HATA:
# AttributeError: 'tuple' object has no attribute 'remove'
# (Tuple'ın 'remove' diye bir metodu bile yoktur, çünkü silme yapamaz)
print("...remove denendi (Hata vermemesi için kod yorumda)...")
print("-" * 30)


# 7. 'pop' metodunu deneme (Listenizde 'fruits.pop(1)' yapmıştınız)
print(f"Tuple'ın şu anki hali: {mevsimler}")
# mevsimler.pop(1)
# YUKARIDAKİ SATIRI ÇALIŞTIRIRSAN ALACAĞIN HATA:
# AttributeError: 'tuple' object has no attribute 'pop'
print("...pop denendi (Hata vermemesi için kod yorumda)...")
print("-" * 30)


# 8. 'append' metodunu deneme (Listenizde 'fruits.append("grape")' yapmıştınız)
print(f"Tuple'ın şu anki hali: {mevsimler}")
# mevsimler.append("YeniMevsim")
# YUKARIDAKİ SATIRI ÇALIŞTIRIRSAN ALACAĞIN HATA:
# AttributeError: 'tuple' object has no attribute 'append'
print("...append denendi (Hata vermemesi için kod yorumda)...")
print("-" * 30)


# 9. 'insert' metodunu deneme (Listenizde 'fruits.insert(1, "kiwi")' yapmıştınız)
print(f"Tuple'ın şu anki hali: {mevsimler}")
# mevsimler.insert(1, "Aralık")
# YUKARIDAKİ SATIRI ÇALIŞTIRIRSAN ALACAĞIN HATA:
# AttributeError: 'tuple' object has no attribute 'insert'
print("...insert denendi (Hata vermemesi için kod yorumda)...")
print("=" * 30)

print("ÖZET: 'tuple' oluşturulduktan sonra değiştirilemez (immutable).")