
# Konu: Global ve Yerel Değişkenler
# Amaç: Değişken kapsamı (scope), global ve local değişken farkları ve 'global' anahtar kelimesi.

# **BLOK 1: Yerel (Local) ve Genel (Global) Kapsam Farkı**

x = 'global x' # Global kapsamda (programın en üst seviyesinde) tanımlanan değişken.

def function():
    # Yerel kapsam (Fonksiyonun içi)
    x = 'local x' # Aynı isimde yerel bir değişken tanımlanır. Bu, global 'x'i GÖLGELER.
    print(x)      # Fonksiyon içinde yerel 'x' kullanılır.

function() # Fonksiyon çağrılır. (Çıktı: local x)
# Fonksiyon dışında, program global 'x'i kullanmaya devam eder.
print(x)     # (Çıktı: global x)


###################

# **BLOK 2: Fonksiyonda Yerel Atama ve Global'in Korunması (Immutable Tipler)**

name = 'Cinar' # Global string değişkeni (değişmez/immutable tip).

def changeName(new_name):
    # Yerel kapsamda, global ile aynı isimde yeni bir değişken oluşturulur.
    # Bu, sadece fonksiyonun içinde geçerlidir.
    name = new_name 
    print(name)

changeName('ada') # Fonksiyon çağrılır. (Çıktı: ada)
# Fonksiyon dışında, global 'name' değişkeni etkilenmemiştir.
print(name)       # (Çıktı: Cinar)

###################

# **BLOK 3: İç İçe Kapsam (Enclosing Scope)**

name = 'global string' # Global değişken.

def greeting():
    # Kapsayıcı (Enclosing) fonksiyonun yerel değişkeni.
    name = 'cinar' 
    
    def hello():
        # İç fonksiyonun yerelinde 'name' yok, bu yüzden kapsayıcı fonksiyona bakar.
        print(f"hello {name}") # Enclosing kapsamdaki 'cinar' kullanılır.

    hello() # İç fonksiyon çağrılır.

greeting() # (Çıktı: hello cinar)

###################


# **BLOK 4: global Anahtar Kelimesi Kullanımı**

x = 50 # Global değişkenin ilk değeri.

# Yorum satırındaki ilk 'test' fonksiyonu, 'x'i parametre olarak alıp yerel olarak değiştirirdi.
# def test(x):
#     print(f"x : {x}")
#     x = 100
#     print(f"changed x to {x}")

def test():
    # 'global x' ifadesi, Python'a bu fonksiyonda yapılan 'x' atamalarının
    # yerel 'x'e değil, doğrudan en üst seviyedeki global 'x'e yapılacağını söyler.
    global x 
    print(f"x : {x}") # Global x'in o anki değerini basar (50).

    x = 100 # Global x'in değeri kalıcı olarak 100 olarak DEĞİŞTİRİLİR.
    print(f"changed x to {x}") # Yeni değeri basar (100).

test()
# Fonksiyon bittikten sonra bile global 'x' kalıcı olarak değişmiş durumdadır.
print(x) # (Çıktı: 100)