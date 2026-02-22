# PROJE 2: Akıllı Cüzdan (Smart Wallet)
# Konu: Magic Methods (__init__, __str__, __add__, __sub__, __len__, __gt__)
# Amaç: Para ekleme, harcama ve cüzdanları kıyaslama işlemlerini sembollerle (+, -, >) yapmak.

class Cuzdan:
    def __init__(self, sahibi, bakiye=0):
        self.sahibi = sahibi
        self.bakiye = bakiye
        self.islem_gecmisi = [] # Yapılan her işlemi buraya string olarak ekle.
        print(f"💰 {sahibi} için cüzdan oluşturuldu. Bakiye: {bakiye} TL")

    # GÖREV 1: __str__ metodu
    # Ekrana "Ali'nin Cüzdanı: 500 TL" yazsın.
    def __str__(self):
        return f"{self.sahibi}'nin Cüzdanı: {self.bakiye} TL"


    # GÖREV 2: __add__ metodu (+)
    # İki senaryo var:
    # 1. cuzdan + 100  -> Bakiyeye 100 TL ekle, işlem geçmişine "100 TL eklendi" yaz.
    # 2. cuzdan1 + cuzdan2 -> İki cüzdanın bakiyesini toplayıp YENİ bir cüzdan döndür. (Sahibi: "Ali & Ayşe" olsun)
    def __add__(self, diger):
        if isinstance(diger, int):
            self.bakiye += diger
            self.islem_gecmisi.append(f"{diger} TL eklendi")
        elif isinstance(diger, Cuzdan):
            yeni_cuzdan = Cuzdan(f"{self.sahibi} & {diger.sahibi}", self.bakiye + diger.bakiye)
            return yeni_cuzdan
        else:
            print("Hata: Sadece sayı veya cüzdan ekleyebilirsin!")
        

    # GÖREV 3: __sub__ metodu (-)
    # cuzdan - 50 -> Bakiyeden 50 TL düş, işlem geçmişine "50 TL harcandı" yaz.
    # Eğer bakiye yetersizse "Yetersiz Bakiye" yazsın ve işlem yapmasın.
    def __sub__(self, miktar):
        if self.bakiye >= miktar:
            self.bakiye -= miktar
            self.islem_gecmisi.append(f"{miktar} TL harcandı")
        else:
            print("Yetersiz Bakiye")    

    # GÖREV 4: __len__ metodu
    # len(cuzdan) deyince kaç tane işlem yapıldığını (islem_gecmisi uzunluğunu) versin.
    def __len__(self):
        return len(self.islem_gecmisi)

    # GÖREV 5: __gt__ metodu (Greater Than >)
    # cuzdan1 > cuzdan2 deyince, kimin bakiyesi fazlaysa True döndürsün.
    def __gt__(self, diger):
        return self.bakiye > diger.bakiye

# ---------------------------------------------------------
# TEST KODLARI (Buralara Dokunma, Sadece Çalıştır)
# ---------------------------------------------------------

# 1. Cüzdan Oluşturma
ali_cuzdan = Cuzdan("Ali", 1000)
ayse_cuzdan = Cuzdan("Ayşe", 2000)

# 2. Para Ekleme Testi (+)
print("\n--- Para Ekleme Testi ---")
ali_cuzdan + 500  # Ali'nin parası 1500 olmalı
print(ali_cuzdan)

# 3. Para Harcama Testi (-)
print("\n--- Para Harcama Testi ---")
ali_cuzdan - 200  # Ali'nin parası 1300 olmalı
ali_cuzdan - 5000 # Yetersiz bakiye demeli
print(ali_cuzdan)

# 4. İşlem Sayısı Testi (len)
print("\n--- İşlem Sayısı Testi ---")
print(f"Ali'nin işlem sayısı: {len(ali_cuzdan)}") # Ekleme ve çıkarma yaptı, 2 olmalı.

# 5. Zenginlik Testi (>)
print("\n--- Zenginlik Testi ---")
if ayse_cuzdan > ali_cuzdan:
    print("Ayşe daha zengin!")
else:
    print("Ali daha zengin!")

# 6. Cüzdan Birleştirme Testi (+)
print("\n--- Cüzdan Birleştirme Testi ---")
ortak_cuzdan = ali_cuzdan + ayse_cuzdan
print(ortak_cuzdan) # Ali & Ayşe'nin Cüzdanı: 3300 TL (1300 + 2000)
