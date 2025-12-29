# Kütüphane Yönetim Sistemi
veritabani = [
    { "id": 1, "isim": "Sefiller", "yazar": "Victor Hugo", "durum": "rafta" },
    { "id": 2, "isim": "Suç ve Ceza", "yazar": "Dostoyevski", "durum": "odunc_verildi" }
]


def kitap_listele():
    print("----- KÜTÜPHANE LİSTESİ -----")
    if not veritabani:
        print("Kütüphane şu an boş.")
        return
    for kitap in veritabani:
        print(f"ID: {kitap['id']} | Adı: {kitap['isim']} | Yazar: {kitap['yazar']} | Durum: {kitap['durum']}")
    print("---------------------------------")

def kitap_ekle():
    print("--- YENİ KİTAP EKLEME ---")
    isim_input = input("Kitabın adını girin: ")
    yazar_input = input("Kitabın yazarını girin: ")

    if len(veritabani) > 0:
        yeni_id = veritabani[-1]['id'] + 1
    else:
        yeni_id = 1
    
    yeni_kitap = {
        "id": yeni_id,
        "isim": isim_input,
        "yazar": yazar_input,
        "durum": "rafta"
    }
    
    veritabani.append(yeni_kitap)
    
    print(f"'{isim_input}' adlı kitap başarıyla kütüphaneye eklendi.")
    print("----------------------------")

def kitap_sil():
    print("\n--- KİTAP SİLME ---")
    id_input = input("Lutfen silmek istediginiz kitabın ID'sini giriniz: ")
    
    try:
        silinecek_id = int(id_input)
        kitap_bulundu = False

        for kitap in veritabani:
            
            if kitap['id'] == silinecek_id:
                kitap_bulundu = True
                
                karar = input(f"ID: {kitap['id']}, Ad: '{kitap['isim']}'. Bu kitabı silmek istiyor musunuz? (e/h): ")
                
                if karar.lower() == 'e':
                    
                    veritabani.remove(kitap)
                    print(f"'{kitap['isim']}' başarıyla silindi.")
                    
                else:
                    print("Silme işlemi iptal edildi. Ana menüye dönülüyor.")
                
                break

        if not kitap_bulundu:
            print(f"Hata: ID {silinecek_id} ile eşleşen bir kitap bulunamadı.")
            
    except ValueError:
        print(f"Hata: Geçersiz giriş. Lütfen '{id_input}' yerine sayısal bir ID girin.")
        
    print("---------------------------------")  

def kitap_durum_guncelle():
    print("--- KİTAP DURUM GÜNCELLEME ---")
    id_input = input("Durumunu değiştirmek istediğiniz kitabın ID'sini girin: ")
    
    try:
        guncellenecek_id = int(id_input)
        kitap_bulundu = False 
        
        for kitap in veritabani:
            if kitap['id'] == guncellenecek_id:
                kitap_bulundu = True 
                if kitap['durum'] == "rafta":
                    kitap['durum'] = "odunc_verildi"
                    print(f"'{kitap['isim']}' kitabı 'odunc_verildi' olarak güncellendi.")
                elif kitap['durum'] == "odunc_verildi":
                    kitap['durum'] = "rafta"
                    print(f"'{kitap['isim']}' kitabı 'rafta' olarak güncellendi.")
                print("---------------------------------")
                break 
        
        if not kitap_bulundu:
            print(f"Hata: ID {guncellenecek_id} ile eşleşen bir kitap bulunamadı.")
            print("---------------------------------")

    except ValueError:
        print(f"Hata: Geçersiz giriş. Lütfen '{id_input}' yerine sayısal bir ID girin.")
        print("---------------------------------")

def ana_menu():
    while True:
        print("\n--- KÜTÜPHANE YÖNETİM SİSTEMİ ---")
        print("1: Kitapları Listele")
        print("2: Yeni Kitap Ekle")
        print("3: Kitap Durum Güncelle")
        print("4: Kitap Sil")  
        print("5: Çıkış")      
        
        secim = input("Lütfen yapmak istediğiniz işlemin numarasını girin (1-5): ")
        
        if secim == "1":
            kitap_listele()
        elif secim == "2":
            kitap_ekle()
        elif secim == "3":
            kitap_durum_guncelle()
        elif secim == "4":  
            kitap_sil()
        elif secim == "5":  
            print("Programdan çıkılıyor. Hoşçakalın!")
            break 
        else:
            print("Hata: Geçersiz seçim! Lütfen 1, 2, 3, 4 veya 5 girin.")

ana_menu()