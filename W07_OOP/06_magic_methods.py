# Konu: Özel Metotlar (Magic/Dunder Methods)
# Amaç: __init__, __str__, __len__, __del__ gibi özel metotların kullanımı ve özelleştirilmesi.

# Kendi oluşturduğumuz 'Movie' sınıfının, 'print()' ve 'len()' gibi
# Python'un yerleşik fonksiyonlarıyla nasıl çalışacağını tanımlamak için
# "Özel Metotlar" (çift alt çizgili __metotlar__) kullanırız.

class Movie():
    
    # 1. __init__: Yapıcı Metot
    # 'm = Movie(...)' gibi bir nesne oluşturulduğu an ilk bu metot çalışır.
    # Nesnenin temel özelliklerini (niteliklerini) ayarlar.
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print("movie objesi olusturuldu")

    # 2. __str__: String Temsili Metodu
    # 'print(m)' komutu çağrıldığında ne yazdırılacağını belirler.
    # Bu metot olmasaydı, Python <...Movie object...> gibi bir hafıza adresi yazdırırdı.
    def __str__(self):
        return f"{self.title} by {self.director}"
    
    # 3. __len__: Uzunluk Metodu
    # 'len(m)' komutu çağrıldığında hangi değerin döndürüleceğini belirler.
    def __len__(self):
        # Bu 'Movie' sınıfı için "uzunluk" kavramının,
        # filmin süresi (duration) olmasını biz seçtik.
        return self.duration
    
    # 4. __del__: Yıkıcı Metot
    # Nesne hafızadan silinirken (genellikle programın en sonunda)
    # Python tarafından otomatik olarak çağrılır.
    def __del__(self):
        print("film silindi")

# --- Sınıfı Test Etme ---

# 1. 'm' nesnesini oluşturuyoruz.
#    Bu satır, __init__ metodunu tetikler.
print("Nesne oluşturuluyor...")
m = Movie('film adı', 'yonetmen adı', 123)

# 2. Nesneyi doğrudan yazdırıyoruz.
#    Bu satır, __str__ metodunu tetikler.
print("--- print(m) ---")
print(m)

# 3. Nesnenin "uzunluğunu" alıyoruz.
#    Bu satır, __len__ metodunu tetikler.
print("--- len(m) ---")
print(len(m))

# 4. Program bittiğinde __del__ metodu otomatik olarak tetiklenecek.
print("Program sonlanıyor...")