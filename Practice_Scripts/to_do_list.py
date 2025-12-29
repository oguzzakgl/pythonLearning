# Görev listesi
yapilacaklar = []

# Ana döngü
while True:
    # Menü seçenekleri
    print("\nTo-Do List Uygulamasına Hoş Geldiniz!") # \n ile üstten bir satır boşluk bırakıldı
    print("1. Görev Ekle")
    print("2. Görevleri Görüntüle")
    print("3. Görev Sil")
    print("4. Çıkış")
    

    secim = input("Lütfen bir seçenek seçiniz: ")
    
    # 1. Görev Ekle
    if secim == '1':
        # Önce listenin mevcut halini göster
        print(f"Mevcut liste: {yapilacaklar}")
        # Kullanıcıdan yeni görev metnini al
        gorev = input("Eklemek istediğiniz görevi giriniz: ")
        
        # Listeye ekle
        yapilacaklar.append(gorev)
        
        # Başarı mesajı ver
        print(f'"{gorev}" görevi eklendi.')
        # Listenin son halini göster
        print(f"Listenin son hali: {yapilacaklar}")
    
    # 2. Görevleri Listele
    elif secim == '2':
        # Liste boş mu?
        if len(yapilacaklar) == 0:
            print("Görev listeniz boş.")
        else:
            # Liste boş değilse, başlık ve listeyi yazdır
            print("\nYapılacak Görevler:")
            print(f"{yapilacaklar}")
            print("--------------------")
        
        # Bekle
        input("\nAna menüye dönmek için Enter'a basın...")

    # 6. Koşul Bloğu (2. Seçenek: Görüntüleme) -
    elif secim == '2':
        # 'len()' ile listenin uzunluğunu (eleman sayısını) kontrol et.
        if len(yapilacaklar) == 0:
            # Eğer eleman sayısı 0 ise (liste boşsa), bu mesajı göster.
            print("Görev listeniz boş.")
        else:
            # Liste boş değilse, başlığı ve listenin kendisini yazdır.
            print("Yapılacak Görevler:")
            print(f"{yapilacaklar}")
            # (Bu blok bittikten sonra döngü başa döner)
    
    # 3. Görev Sil
    elif secim == '3':
        # Silme işlemi öncesi listenin güncel halini göster
        print(f"Mevcut liste: {yapilacaklar}")
        # Kullanıcıdan silmek istediği görevin tam adını al
        gorev = input("Silmek istediğiniz görevi giriniz: ")
        

        # Görev listede var mı?
        if gorev in yapilacaklar:
            # Eğer görev listede varsa, 'remove()' metodu ile o görevi sil.
            yapilacaklar.remove(gorev)
            print(f'"{gorev}" görevi silindi.')
        else:
            # Bulunamadı
            print(f'"{gorev}" görevi bulunamadı.')
    
    # 8. Koşul Bloğu (4. Seçenek: Çıkış)
    elif secim == '4':
        print("Uygulamadan çıkılıyor. İyi günler!")
        break
    
    # 9. 'else' Bloğu (Geçersiz Seçim)
    else:
        # Hatalı seçim
        print("Geçersiz seçenek, lütfen 1-4 arasında bir sayı girin.")
        
# 'break' çalıştırıldığında program döngüden çıkar