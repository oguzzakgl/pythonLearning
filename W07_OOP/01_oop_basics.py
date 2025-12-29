# Konu: OOP Temelleri (Sınıf ve Nesne)
# Amaç: Class (Sınıf) tanımlama, Instance (Nesne) oluşturma, Attribute (Nitelik) ve Method (Metot) kavramları.

# 'Person' adında bir sınıf (şablon) tanımlıyoruz
class Person:

    # CLASS ATTRIBUTE (Sınıf Niteliği)
    # Bu özellik, tüm 'Person' nesneleri için ortaktır ve aynıdır.
    address = "no information"

    # CONSTRUCTOR (Yapıcı Metot)
    # Bir nesne (p1) oluşturulduğu an otomatik olarak ilk çalışan metottur.
    # Nesneye ait ilk özellikleri (name, year) ayarlar.
    def __init__(self, name, year):
        
        # OBJECT / INSTANCE ATTRIBUTES (Nesne Nitelikleri)
        # 'self', o an oluşturulan nesnenin (p1'in) kendisini temsil eder.
        # Bu özellikler (name, birthyear) her nesne için farklı olabilir.
        self.name = name
        self.birthyear = year 

    # INSTANCE METHODS (Nesne Metotları)
    # Nesnelerin yapabileceği eylemlerdir (fonksiyonlardır).
    
    # 'intro' metodu, nesnenin 'name' özelliğini kullanarak kendini tanıtır.
    def intro(self):
        # 'self.name', bu nesnenin (p1'in) ismine erişir.
        print("hello there. I am " + self.name)

    # 'calculateAge' metodu, nesnenin 'birthyear' özelliğini kullanarak yaşını hesaplar.
    def calculateAge(self):
        # Yaşı hesaplamak için şu anki yılı (2025) sabit olarak kullanıyoruz.
        current_year = 2025 
        return current_year - self.birthyear 
    
# OBJECT / INSTANCE (Nesne Oluşturma)
# 'Person' şablonunu kullanarak 'p1' adında gerçek bir nesne oluşturuyoruz.
# "oguz" -> name parametresine, 2004 -> year parametresine gider.
p1 = Person("oguz", 2004)

# Nesnenin metotlarını çağırma
p1.intro() # p1 nesnesi kendini tanıtır.

# Nesnenin metodunu çağırıp dönen değeri yazdırma
# Sonuç: 2025 - 2004 = 21
print(f"yasim: {p1.calculateAge()}")


# 'Circle' adında bir sınıf (şablon) tanımlıyoruz
class Circle:
    
    # CLASS OBJECT ATTRIBUTE (Sınıf Niteliği)
    # Pi sayısı, oluşturulacak tüm daireler (c1, c2...) için ortak bir sabittir.
    pi = 3.14

    # CONSTRUCTOR (Yapıcı Metot)
    # 'yaricap=1' -> Eğer kullanıcı yarıçap vermezse, varsayılan olarak 1 kullan demektir.
    def __init__(self, yaricap=1):
        
        # OBJECT ATTRIBUTE (Nesne Niteliği)
        # 'self.yaricap', bu daire nesnesine ait yarıçapı saklar.
        self.yaricap = yaricap

    # INSTANCE METHODS (Nesne Metotları)

    # Dairenin çevresini hesaplayan metot
    def cevreHesapla(self):
        # Hem sınıf özelliğine (self.pi) hem de nesne özelliğine (self.yaricap) erişir
        return 2 * self.pi * self.yaricap
    
    # Dairenin alanını hesaplayan metot
    def alanHesapla(self):
        # 'yaricap**2' yarıçapın karesini alır (yaricap * yaricap)
        return self.pi * (self.yaricap**2)

# --- SINIF TANIMI BİTTİ ---

# INSTANCE (Nesne Oluşturma)
# Yarıçapı 5 olan bir 'c1' dairesi oluşturuyoruz.
c1 = Circle(5) 

# 'c1' nesnesinin metotlarını kullanarak hesaplama yapıp yazdırma
print(f'c1 : alan = {c1.alanHesapla()} çevre : {c1.cevreHesapla()}')

# Varsayılan yarıçapı (1) kullanan bir daire
c2 = Circle()
print(f'c2 : alan = {c2.alanHesapla()} çevre : {c2.cevreHesapla()}')