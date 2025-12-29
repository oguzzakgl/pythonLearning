# Konu: Kalıtım (Inheritance) Temelleri
# Amaç: Bir sınıfın başka bir sınıftan türetilmesi (miras alma) örneği.

class Calisan:
    def __init__(self, isim, soyisim, maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim + '.' + soyisim + '@firma.com'

calisan1 = Calisan('Ali', 'Veli', 5000)
calisan2 = Calisan('Ayse', 'Kara', 6000)

class Yazilimci(Calisan):
    pass

yazilimci1 = Yazilimci('Mehmet', 'Demir', 7000)
yazilimci2 = Yazilimci('Fatma', 'Sari', 8000)
print(yazilimci1.email)      # MehmetDemir@firma.com


print(calisan1.isim)        # Ali
print(calisan1.email)       #