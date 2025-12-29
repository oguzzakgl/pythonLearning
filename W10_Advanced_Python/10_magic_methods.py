# Konu: Magic Methods (Dunder Methods)
# Amaç: Kendi oluşturduğumuz nesnelerin (Class), Python'un yerleşik özellikleri gibi davranmasını sağlamak.
# "Dunder" = Double Underscore (__init__ gibi)

class Sepet:
    def __init__(self, sahibi):
        self.sahibi = sahibi
        self.urunler = []
        print(f"🛒 {sahibi} için sepet oluşturuldu.")

    # 1. __str__: Nesneyi print() edince ne yazsın?
    # Eğer bunu yazmazsan ekranda <__main__.Sepet object at 0x...> yazar.
    def __str__(self):
        return f"{self.sahibi}'nin Sepeti ({len(self.urunler)} ürün var)"

    # 2. __len__: len(sepet) deyince ne döndürsün?
    def __len__(self):
        return len(self.urunler)

    # 3. __add__: İki sepeti toplayınca (+) ne olsun?
    # sepet1 + sepet2 işlemi için çalışır.
    def __add__(self, diger_sepet):
        yeni_sepet = Sepet(f"{self.sahibi} & {diger_sepet.sahibi}")
        yeni_sepet.urunler = self.urunler + diger_sepet.urunler
        return yeni_sepet
    
    # 4. __getitem__: Listeler gibi sepet[0] diyebilmek için.
    def __getitem__(self, index):
        return self.urunler[index]

    def urun_ekle(self, urun):
        self.urunler.append(urun)

# ---------------------------------------------------------
# TEST EDELİM
# ---------------------------------------------------------

# Sepetleri oluşturalım
sepet1 = Sepet("Ali")
sepet1.urun_ekle("Elma")
sepet1.urun_ekle("Armut")

sepet2 = Sepet("Ayşe")
sepet2.urun_ekle("Süt")

print("\n--- 1. __str__ Testi ---")
print(sepet1) # Ali'nin Sepeti (2 ürün var) yazar

print("\n--- 2. __len__ Testi ---")
print(f"Ali'nin sepetinde {len(sepet1)} ürün var.") # len() fonksiyonu artık çalışıyor!

print("\n--- 3. __add__ Testi ---")
# İki sepeti toplayalım (Python bunu normalde yapamaz, biz öğrettik)
ortak_sepet = sepet1 + sepet2 
print(ortak_sepet)
print(f"Ortak Ürünler: {ortak_sepet.urunler}")

print("\n--- 4. __getitem__ Testi ---")
# Sepetin içindeki ilk ürünü liste gibi çağıralım
print(f"Ali'nin ilk ürünü: {sepet1[0]}")
