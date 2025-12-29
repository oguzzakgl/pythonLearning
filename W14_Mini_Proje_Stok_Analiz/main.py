# Stok Takip ve Analiz Uygulaması - Ana Modül
import database 

while True:
    print("1- Ekle")
    print("2- Listele")
    print("3- Çıkış")
    secim = input("Seçim: ")
    if secim == "1":
        ad = input("Ad: ")
        fiyat = float(input("Fiyat: "))
        stok = int(input("Stok: "))
        database.urun_ekle(ad, fiyat, stok)
    elif secim == "2":
        urunler = database.urunleri_getir()
        print("\n--- ÜRÜN LİSTESİ ---")
        for urun in urunler:
            print(f"ID: {urun[0]}, Ad: {urun[1]}, Fiyat: {urun[2]}, Stok: {urun[3]}")
    elif secim == "3":
        break