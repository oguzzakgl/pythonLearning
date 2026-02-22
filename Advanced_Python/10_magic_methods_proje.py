# PROJE: Süper Kahraman Takımı Yönetimi
# Konu: Magic Methods (__init__, __str__, __len__, __add__, __getitem__)
# Amaç: Kendi 'Takim' sınıfımızı yazıp, Python'un yerleşik listeleri gibi davranmasını sağlamak.

class Kahraman:
    def __init__(self, isim, guc):
        self.isim = isim
        self.guc = guc
    
    def __str__(self):
        return f"🦸‍♂️ {self.isim} (Güç: {self.guc})"

class Takim:
    def __init__(self, takim_adi):
        self.takim_adi = takim_adi
        self.kahramanlar = []
    
    # GÖREV 1: __str__ metodu
    def __str__(self):
        return f"{self.takim_adi} ({len(self.kahramanlar)} Kahraman)"

    # GÖREV 2: __len__ metodu
    def __len__(self):
        return len(self.kahramanlar)

    # GÖREV 3: __add__ metodu (GÜNCELLENDİ)
    # Hem Kahraman ekleyebilsin, hem de başka bir Takım ile birleşebilsin.
    def __add__(self, diger):
        # Eğer eklenen şey bir Kahraman ise:
        if isinstance(diger, Kahraman):
            self.kahramanlar.append(diger)
            return self
        
        # Eğer eklenen şey başka bir Takım ise:
        elif isinstance(diger, Takim):
            # Yeni bir "Süper Takım" oluştur
            yeni_takim = Takim(f"{self.takim_adi} & {diger.takim_adi}")
            # İki takımın kahramanlarını birleştir
            yeni_takim.kahramanlar = self.kahramanlar + diger.kahramanlar
            return yeni_takim
        
        else:
            print("Hata: Sadece Kahraman veya Takım ekleyebilirsin!")
            return self

    # GÖREV 4: __getitem__ metodu
    def __getitem__(self, index):
        return self.kahramanlar[index]

# ---------------------------------------------------------
# TEST KODLARI (Buralara Dokunma, Sadece Çalıştır)
# ---------------------------------------------------------

# 1. Takım Oluşturma
avengers = Takim("Avengers")

# 2. Kahramanları Oluşturma
iron_man = Kahraman("Iron Man", 95)
thor = Kahraman("Thor", 98)
hulk = Kahraman("Hulk", 99)

# 3. Ekleme Testi (__add__)
print("\n--- Ekleme Testi ---")
avengers + iron_man
avengers + thor
avengers + hulk
print("Kahramanlar eklendi.")

# 4. Yazdırma Testi (__str__)
print("\n--- Yazdırma Testi ---")
print(avengers) # Beklenen: Avengers (3 Kahraman)

# 5. Uzunluk Testi (__len__)
print("\n--- Uzunluk Testi ---")
print(f"Takımdaki kişi sayısı: {len(avengers)}") # Beklenen: 3

# 6. Erişim Testi (__getitem__)
print("\n--- Erişim Testi ---")
print(f"Lider: {avengers[0]}") # Beklenen: Iron Man
print(f"En Güçlü: {avengers[2]}") # Beklenen: Hulk

# 7. Takım Birleştirme Testi (YENİ)
print("\n--- Takım Birleştirme Testi ---")
justice_league = Takim("Justice League")
batman = Kahraman("Batman", 90)
superman = Kahraman("Superman", 100)

justice_league + batman
justice_league + superman

print(f"Takım 1: {avengers}")
print(f"Takım 2: {justice_league}")

# İki takımı toplayalım!
mega_takim = avengers + justice_league
print(f"Birleşmiş Takım: {mega_takim}")
print(f"Mega Takım Lideri: {mega_takim[0]}")
print(f"Mega Takım Son Üyesi: {mega_takim[-1]}")
