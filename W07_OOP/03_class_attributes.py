# Konu: Sınıf Nitelikleri (Class Attributes)
# Amaç: Sınıf seviyesindeki değişkenler ve nesne seviyesindeki değişkenlerin farkı.

class calisan:
    zam_orani=1.1
    personel_sayisi=0
    def __init__(self,isim,maas):
        self.isim=isim
        self.maas=maas
        calisan.personel_sayisi +=1


print(calisan.personel_sayisi)
calisan1=calisan("oguz",5000)
print(calisan.personel_sayisi)
calisan2=calisan("ali",6000)
print(calisan.personel_sayisi)


# print(calisan1.__dict__)
# print(calisan2.__dict__)

calisan.zam_orani=1.2
calisan2.zam_orani=1.3

print(calisan.zam_orani)
print(calisan1.zam_orani)
print(calisan2.zam_orani)


print(calisan1.__dict__)
print(calisan2.__dict__)