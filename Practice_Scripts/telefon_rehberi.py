# Telefon Rehberi Uygulaması
rehber = {
    "Oğuz Kaan": "5519406834",
    "Bora Caba": "5377281647",
    "Ahmet Yılmaz": "5321234567",
    "Mehmet Demir": "5459876543"
}

print("Telefon Rehberi Uygulamasına Hoşgeldiniz!")
print("-----------------------------------")

while True:
    print("\nLutfen yapmak istediğiniz işlemi seçiniz:")
    print("1: Rehberdeki kişileri gör")
    print("2: Yeni kişi ekle / Numara güncelle")
    print("3: Kişi ara") 
    print("4: Kişi sil") 
    print("5: Çıkış")   
    
    secim = input("Seçiminiz (1-5): ")

    if secim == '1':
        print("\n--- Rehberdeki Kişiler ---")
        if not rehber:
            print("Rehber boş.")
        else:
            for isim, numara in rehber.items():
                print(f"{isim}: {numara}")
    
    elif secim == '2':
        isim = input("Eklemek/güncellemek istediğiniz kişinin ismi: ")
        
        while True:
            numara = input(f"{isim} için telefon numarası girin (Sadece 10 haneli rakam): ")
            
            if not numara.isdigit():
                print("HATA: Telefon numarası sadece rakamlardan oluşmalıdır.")
            
            elif len(numara) != 10:
                print(f"HATA: Numara 10 haneli olmalıdır (Siz {len(numara)} hane girdiniz).")
            
            else:
                rehber[isim] = numara
                print(f"{isim} rehbere başarıyla eklendi/güncellendi.")
                break
            
            print("-----------------------------------")
            tekrar_dene = input("Hatalı giriş. Tekrar denemek ister misiniz? (e/h): ").lower()
            
            if tekrar_dene == "h":
                print("İşlem iptal edildi, ana menüye dönülüyor.")
                break
            
    elif secim == '3':
        aranan_isim = input("Aramak istediğiniz kişinin ismi: ")
        if aranan_isim in rehber:
            bulunan_numara = rehber[aranan_isim]
            print(f"\n--- Bulunan Kayıt ---")
            print(f"{aranan_isim}: {bulunan_numara}")
        else:
            print(f"{aranan_isim} rehberde bulunamadı.")
            
    elif secim == '4':
        isim = input("Silmek istediğiniz kişinin ismi: ")
        if isim in rehber:
            del rehber[isim]
            print(f"{isim} rehberden silindi.")
        else:
            print(f"{isim} rehberde bulunamadı.")
    
    elif secim == '5':
        print("Uygulamadan çıkılıyor. İyi günler!")
        break 
        
    else:
        print("Geçersiz seçim, lütfen 1-5 arası bir sayı deneyiniz.")