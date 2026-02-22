# Konu: OOP Giriş (Sınıf ve Örnek)
# Amaç: Sınıf oluşturma, __init__ metodu ve nesne (instance) kavramına giriş.

# sınıf ve ornek kavramları (class and instance concepts)
# class olusturma
# özellik ve metotlar(attributes and methods)

class calisan:
    def __init__(self,name,surname,age): # self parametresi zorunludur. Değişkeni temsil eder(calisan1, calisan2).
        print("__init__ metodu calisti")
        self.name=name
        self.surname=surname
        self.age=age

    def calisan_bilgileri(self):
        print("Calisan bilgileri gosteriliyor")
        print("Ad:",self.name)
        print("Soyad:",self.surname)
        print("Yas:",self.age)


calisan1 = calisan("oguz","demir",20)
# print(calisan1.name,calisan1.surname,calisan1.age)

calisan2 = calisan("ali","veli",30)
# print(calisan2.name,calisan2.surname,calisan2.age)

calisan.calisan_bilgileri(calisan1)

# calisan1.calisan_bilgileri()
# calisan2.calisan_bilgileri()