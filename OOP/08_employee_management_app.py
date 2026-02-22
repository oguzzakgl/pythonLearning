# Konu: Çalışan Yönetim Sistemi (OOP)
# Amaç: Sınıf yapısı, sınıf nitelikleri (class attributes) ve tarih işlemleri ile çalışan takibi.

from datetime import date, datetime

class Calisan:
    calisan_sayisi = 0
    def __init__(self, isim, soyisim, maas, ise_giris_tarihi):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.ise_giris_tarihi = ise_giris_tarihi
        self.calistigi_yil = date.today().year - ise_giris_tarihi.year 
        self.email = isim.lower() + '.' + soyisim.lower() + '@firma.com'
        
        Calisan.calisan_sayisi += 1 

    def bilgileri_goster(self):
        return (f'İsim: {self.isim} {self.soyisim}, Maaş: {self.maas:.2f} TL, '
                f'İşe Giriş Tarihi: {self.ise_giris_tarihi}, Çalıştığı Yıl: {self.calistigi_yil} yıl')
    
calisanlar_listesi = []

def calisan_ekle(calisanlar):
    input_isim = input("Çalışanın ismini girin: ")
    input_soyisim = input("Çalışanın soyismini girin: ")
    
    try:
        input_maas = float(input("Çalışanın maaşını girin (Örn: 50000.50): "))
    except ValueError:
        print("❌ Geçersiz maaş girdisi. Lütfen sayısal bir değer girin.")
        return
    
    input_tarih_str = input("İşe Giriş Tarihini girin (YYYY-MM-DD formatında): ")
    try:
        input_ise_giris_tarihi = datetime.strptime(input_tarih_str, '%Y-%m-%d').date()
    except ValueError:
        print("❌ Geçersiz tarih formatı. Lütfen YYYY-MM-DD formatında bir tarih girin.")
        return
        
    yeni_calisan = Calisan(input_isim, input_soyisim, input_maas, input_ise_giris_tarihi)
    
    calisanlar.append(yeni_calisan)
    print(f"✅ Çalışan {yeni_calisan.isim} başarıyla eklendi.")


def calisanlari_listele(calisanlar):
    """Tüm çalışanların bilgilerini ve toplam sayıyı listeler."""
    print("\n--- Kayıtlı Çalışanlar Listesi ---")
    if not calisanlar:
        print("Henüz kayıtlı çalışan bulunmamaktadır.")
        return
        
    for calisan in calisanlar:
        print(calisan.bilgileri_goster())

    print(f"\nToplam Şirket Çalışanı Sayısı: **{Calisan.calisan_sayisi}**")
    

while True:
    print("\n--- Çalışan Yönetim Sistemi ---")
    print("1. Yeni Çalışan Ekle")
    print("2. Çalışanları Listele")
    print("3. Çıkış")
    secim = input("Seçiminizi yapın (1-3): ")

    if secim == '1':
        calisan_ekle(calisanlar_listesi) 
    elif secim == '2':
        calisanlari_listele(calisanlar_listesi)
    elif secim == '3':
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")