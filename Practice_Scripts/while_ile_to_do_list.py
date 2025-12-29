# Görev listemiz
gorevler = ["Çamaşırları yıka", "Python ödevini yap", "Markete git", "Arkadaşını ara"]

# Tamamlananlar listesi
tamamlanan_gorevler = []

print(f"Kontrol başlıyor. {len(gorevler)} adet görev var.")
print("---------------------------------")

# Görevleri döngüyle kontrol et
i = 0 
while i < len(gorevler):
    
    # Mevcut görev
    simdiki_gorev = gorevler[i]
    
    # Kullanıcı onayı
    print(f"\nSıradaki görev: {simdiki_gorev}")
    cevap = input("Bu görevi tamamladın mı? (e/h/q: çıkış): ")
    
    # Karar verme
    if cevap.lower() == 'e':
        # Görevi tamamlananlara taşı
        tamamlanan = gorevler.pop(i)
        tamamlanan_gorevler.append(tamamlanan)
        print(f"-> '{tamamlanan}' GÖREVİ TAMAMLANDI OLARAK İŞARETLENDİ.")
        
        # Eleman silindiği için index artmaz
        
    elif cevap.lower() == 'h':
        # Pas geç
        print(f"-> '{simdiki_gorev}' DAHA SONRAYA BIRAKILDI.")
        i += 1 
        
    elif cevap.lower() == 'q':
        # Çıkış seçeneği
        print("Kontrolden çıkılıyor...")
        break # while döngüsünü tamamen kırar
        
    else:
        # Geçersiz giriş
        print("Lütfen sadece 'e', 'h' veya 'q' giriniz.")
        # 'i' yi artırmıyoruz, böylece aynı soru tekrar sorulur.

# Sonuçları göster
print("---------------------------------")
print("GÖREV KONTROLÜ BİTTİ!")
print(f"Tamamlananlar: {tamamlanan_gorevler}")
print(f"Kalan Görevler: {gorevler}")