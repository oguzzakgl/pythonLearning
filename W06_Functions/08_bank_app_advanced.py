# Konu: Bankamatik Uygulaması (Gelişmiş)
# Amaç: Kapsamlı bir banka sistemi; hesap açma, para yatırma/çekme, silme ve hata yönetimi.

BANKA_HESAPLARİ = {}
SON_HESAP_NO = 1000

def hesap_ac():
    global SON_HESAP_NO

    print("\n--- YENİ HESAP AÇMA ---")
    
    name = input("Lütfen tam adınızı giriniz: ").strip() 
    
    while True:
        try:
            giris = input("Başlangıç bakiyesini giriniz (Min 0): ").replace(',', '.')
            ilk_bakiye = float(giris)
            
            if ilk_bakiye < 0:
                print("Başlangıç bakiyesi negatif olamaz. Lütfen tekrar girin.")
                continue
            break
        except ValueError:
            print("Geçersiz bakiye formatı. Lütfen sadece sayı girin.")

    SON_HESAP_NO += 1
    yeni_no = str(SON_HESAP_NO)
    
    BANKA_HESAPLARİ[yeni_no] = {
        'ad': name,
        'bakiye': ilk_bakiye,
        'hesapNo': yeni_no
    }
    
    print("\n" + "="*40)
    print(f"✅ HESAP BAŞARIYLA AÇILDI! Hesap Numaranız: {yeni_no}")
    print(f"Hesap Sahibi: {name}")
    print(f"Mevcut Bakiye: {ilk_bakiye:.2f} TL")
    print("="*40)


def para_cek():
    print("\n--- PARA ÇEKME ---")
    islemYapilacakHesapNo = input("Lütfen işlem yapmak istediğiniz hesap numarasını giriniz: ").strip()
    
    if islemYapilacakHesapNo not in BANKA_HESAPLARİ:
        print("\n❌ Hata: Hesap numarası sistemde bulunamadı.")
        return

    hesap = BANKA_HESAPLARİ[islemYapilacakHesapNo]
    mevcut_bakiye = hesap['bakiye']

    while True:
        try:
            miktar_str = input(f"Lütfen çekmek istediğiniz tutarı giriniz (Mevcut: {mevcut_bakiye:.2f} TL): ").replace(',', '.')
            cekilen_para = float(miktar_str)
             
            if cekilen_para <= 0:
                print("Çekilen tutar pozitif bir sayı olmalıdır.")
                continue

            if cekilen_para > mevcut_bakiye:
                print("\n❌ Yetersiz bakiye!")
                print(f"Mevcut Bakiye: {mevcut_bakiye:.2f} TL")
                continue 

            hesap['bakiye'] -= cekilen_para
            
            print("\n" + "="*40)
            print(f"✅ İşleminiz tamamlanmıştır. Çekilen Tutar: {cekilen_para:.2f} TL")
            print(f"Kalan Bakiyeniz: {hesap['bakiye']:.2f} TL")
            print("="*40)
            break
            
        except ValueError:
            print("Geçersiz tutar formatı. Lütfen sadece sayı girin (Örn: 150.0).") 


def para_yatir():
    print("\n--- PARA YATIRMA ---")
    islemYapilacakHesapNo = input("Lütfen işlem yapmak istediğiniz hesap numarasını giriniz: ").strip()
    
    if islemYapilacakHesapNo not in BANKA_HESAPLARİ:
        print("\n❌ Hata: Hesap numarası sistemde bulunamadı.")
        return

    hesap = BANKA_HESAPLARİ[islemYapilacakHesapNo]
    mevcut_bakiye = hesap['bakiye']

    while True:
        try:
            miktar_str = input(f"Lütfen yatırmak istediğiniz miktarı giriniz. (Mevcut: {mevcut_bakiye:.2f} TL): ").replace(',', '.')
            yatirilan_para = float(miktar_str)
            
            if yatirilan_para <= 0:
                print("Yatırılacak tutar pozitif bir sayı olmalıdır.")
                continue

            hesap['bakiye'] += yatirilan_para

            print("\n" + "="*40)
            print(f"✅ İşleminiz tamamlanmıştır. Yatırılan Tutar: {yatirilan_para:.2f} TL") 
            print(f"Yeni Bakiyeniz: {hesap['bakiye']:.2f} TL")
            print("="*40)
            break
            
        except ValueError:
            print("Geçersiz tutar formatı. Lütfen sadece sayı girin (Örn: 150.0).") 


def bakiye_sorgula():
    print("\n--- BAKİYE SORGULAMA ---")
    sorgu = input("Lütfen hesap numaranızı giriniz: ").strip()

    if sorgu not in BANKA_HESAPLARİ:
        print("\n❌ Hata: Hesap numarası sistemde bulunamadı.")
        return

    hesap = BANKA_HESAPLARİ[sorgu]

    print("\n" + "-"*30)
    print(f"Hesap Sahibi: {hesap['ad']}")
    print(f"Hesap No: {sorgu}")
    print(f"**Güncel Bakiye: {hesap['bakiye']:.2f} TL**")
    print("-"*30)


def hesap_sil():
    print("\n--- HESAP SİLME ---")
    sorgu = input("Lütfen silmek istediğiniz hesap numarasını giriniz: ").strip()

    if sorgu not in BANKA_HESAPLARİ:
        print("\n❌ Hata: Hesap numarası sistemde bulunamadı.")
        return 

    hesap = BANKA_HESAPLARİ[sorgu]
    
    print(f"\nUYARI: '{hesap['ad']}' adlı kişiye ait {sorgu} numaralı hesap silinmek üzeredir.")
    onay = input("Bu hesabı silmek istediğinizden emin misiniz? (E/H): ").strip().upper()
    
    if onay == 'E':
        del BANKA_HESAPLARİ[sorgu] 
        
        print("\n" + "="*40)
        print(f"✅ Hesap numarası {sorgu} başarıyla silinmiştir.")
        print("="*40)
    else:
        print("\nİşlem iptal edildi. Hesap silinmedi.")


def ana_menu():
    while True:
        print("\n\n" + "#"*40)
        print("####### BANKAMATİK UYGULAMASI MENÜSÜ #######")
        print("#"*40)
        print("1: Yeni Hesap Aç")
        print("2: Para Çek") 
        print("3: Para Yatır")
        print("4: Bakiye Sorgula")
        print("5: Hesap Sil")
        print("6: Çıkış")
        print("----------------------------------------")

        secim_str = input("Lütfen yapmak istediğiniz işlemi seçin (1-7): ").strip()

        try:
            islem = int(secim_str)
        except ValueError:
            print("\n Geçersiz giriş. Lütfen menüdeki rakamlardan birini giriniz.")
            continue

        if islem == 1:
            hesap_ac()
        elif islem == 2:
            para_cek() 
        elif islem == 3:
            para_yatir()
        elif islem == 4:
            bakiye_sorgula()
        elif islem == 5:
            hesap_sil()
        elif islem == 6:
            print("\nUygulamadan çıkılıyor. İyi günler!")
            break
        else: 
            print("\n❗ Geçersiz seçim. Lütfen 1 ile 7 arasında bir sayı giriniz.")


ana_menu()