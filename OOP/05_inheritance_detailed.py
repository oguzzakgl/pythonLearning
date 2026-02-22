# Konu: Kalıtım (Inheritance)
# Amaç: Bir sınıfın özelliklerini başka bir sınıfa aktarma (Miras Alma), super() ve metot ezme (override).

# --- PUPA (ANA) SINIF ---
# Diğer sınıfların miras alacağı temel 'Person' şablonu.
class Person():
    # 1. Yapıcı Metot (Constructor)
    # Her 'Person' nesnesi oluşturulurken çalışır.
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        print("person created")

    # 2. Standart Metot
    def who_am_i(self):
        print("I am a person")

    # 3. Miras Alınacak Metot
    def eat(self):
        print("I am eating")

# --- ÇOCUK (ALT) SINIF 1: Student ---
# 'Student' sınıfı, 'Person' sınıfından miras alır.
# Artık 'Student' bir 'Person'dır ve onun metotlarına sahiptir.
class Student(Person): 
    # 1. 'Student'ın Kendi Yapıcı Metodu
    # Bu metot, 'Person'dan Gelenlere EK olarak 'number' da alır.
    def __init__(self, fname, lname, number):
        
        # Pupa (Person) sınıfının __init__'ini çağırarak 
        # 'firstname' ve 'lastname' özelliklerini ayarlar.
        # super() -> Miras alınan (Person) sınıfı temsil eder.
        super().__init__(fname, lname) 
        
        # 'Student' sınıfına özel yeni özellik (Uzmanlaşma)
        self.studentNumber = number 
        print("student created")

    # 2. METOT EZME (OVERRIDE)
    # 'Person'daki 'who_am_i' metodu 'Student' için artık geçersiz.
    # Bu metot çağrıldığında 'Person'daki değil, BU metot çalışır.
    def who_am_i(self):
        print("I am a student")

    # 3. 'Student'a Özel Metot
    def sayHello(self):
        print("Hi, I am a student")

# --- ÇOCUK (ALT) SINIF 2: Teacher ---
# 'Teacher' sınıfı da 'Person' sınıfından miras alır.
class Teacher(Person):
    def __init__(self, fname, lname, branch):
        # Pupa (Person) sınıfının __init__'i 'super()' ile ÇAĞRILDI.
        # Artık 'Teacher' nesneleri de 'firstname' ve 'lastname' niteliklerine sahip olacak.
        super().__init__(fname, lname)
        
        # 'Teacher' sınıfına özel yeni özellik
        self.branch = branch
        print("teacher created")

    # 2. METOT EZME (OVERRIDE)
    # 'who_am_i' metodu 'Teacher' için de yeniden tanımlandı.
    def who_am_i(self):
        # f-string (f"...") ile değişkeni metne ekliyoruz
        print(f"I am a {self.branch} teacher")

# --- NESNE OLUŞTURMA (INSTANCE) ---

p2 = Person('ali', 'yilmaz')          # Temel 'Person' nesnesi
s2 = Student('cinar', 'turan', 456)   # 'Student' nesnesi
t2 = Teacher('Oguz', 'Akgul' , 'Math')  # 'Teacher' nesnesi

print("--- Niteliklere Erişim ---")
print(p2.firstname + ' ' + p2.lastname)
print(s2.firstname + ' ' + s2.lastname + ', Numara: ' + str(s2.studentNumber))
# Artık 't2.firstname' de 'super()' sayesinde düzgün çalışır
print(t2.firstname + ' ' + t2.lastname + ', Branş: ' + t2.branch)

print("--- Override (Metot Ezme) Kanıtı ---")
# Her nesne KENDİ 'who_am_i' metodunu çağırır.
p2.who_am_i() # Çıktı: I am a person
s2.who_am_i() # Çıktı: I am a student
t2.who_am_i() # Çıktı: I am a Math teacher

print("--- Kalıtım (Inheritance) Kanıtı ---")
# 'eat()' metodu 'Person'da tanımlandı, ama hepsi miras aldı.
p2.eat() # Çıktı: I am eating
s2.eat() # Çıktı: I am eating
t2.eat() # Çıktı: I am eating

print("--- Alt Sınıfa Özel Metot Kanıtı ---")
# 'sayHello()' sadece 'Student' sınıfında var.
s2.sayHello() # Çıktı: Hi, I am a student
# p2.sayHello() # HATA VERİR: 'Person' nesnesinin bu metodu yok
# t2.sayHello() # HATA VERİR: 'Teacher' nesnesinin bu metodu yok