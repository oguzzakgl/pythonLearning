# Konu: OOP Özet ve Uygulama
# Amaç: Sınıf, nesne, nitelik ve metot kavramlarının kapsamlı bir özeti ve araba örneği.

# ==========================================================
# 1. SINIF TANIMI (Class) 🏛️
# ==========================================================

# Sınıf, bir nesnenin nasıl olması gerektiğini belirten şablon veya plandır.
class Araba:
    # CLASS ATTRIBUTE (Sınıf Niteliği): Tüm arabalar için ortaktır (Örn: tekerlek sayısı).
    tekerlek_sayisi = 4 

    # CONSTRUCTOR (__init__): Nesne oluşturulduğu anda (bmw = Araba(...) ) ilk çalışan metot.
    def __init__(self, renk, model):
        # INSTANCE ATTRIBUTES (Örnek Nitelikleri): Nesneye özel veriler (self zorunlu).
        # self.renk, sadece bu nesneye (örneğin 'bmw'ye) aittir.
        self.renk = renk
        self.model = model
        self.hiz = 0  # Başlangıç hızı

    # INSTANCE METHOD (Örnek Metot): Nesnenin yapabileceği bir eylemdir.
    def gaz_ver(self):
        # self anahtarı ile nesnenin kendi niteliklerine (hiz ve renk) erişilir.
        self.hiz += 20
        print(f"✅ {self.renk} {self.model} hızlanıyor. Güncel Hız: {self.hiz}")

    # INSTANCE METHOD: Nesnenin bilgilerini okuma eylemi.
    def bilgileri_goster(self):
        print(f"Model: {self.model}, Renk: {self.renk}, Tekerlek Sayısı: {Araba.tekerlek_sayisi}")


# ==========================================================
# 2. NESNE OLUŞTURMA (Instantiation) 🚗
# ==========================================================

print("--- Nesne Oluşturma ve Özellik Atama ---")
# NESNE OLUŞTURMA: Araba sınıfından bir 'bmw' NESNESİ (gerçek bir varlık) ürettik.
# Bu satır __init__ metodunu tetikler.
bmw = Araba("Mavi", "3 Serisi")

# Aynı sınıftan farklı niteliklere sahip başka bir nesne oluşturma.
volvo = Araba("Kırmızı", "S90")

# Örnek Niteliklerine Doğrudan Erişim:
print(f"BMW'nin Rengi: {bmw.renk}")
print(f"Volvo'nun Modeli: {volvo.model}")


# ==========================================================
# 3. METOT ÇAĞIRMA VE NİTELİK ERİŞİMİ
# ==========================================================

print("\n--- Metot Çağırma ve Eylemler ---")
# bmw nesnesinin gaz_ver metodunu çağırarak hızını artırma eylemini gerçekleştirme.
bmw.gaz_ver()  # BMW hızlanır (hiz = 20)
bmw.gaz_ver()  # BMW tekrar hızlanır (hiz = 40)

# volvo nesnesinin gaz_ver metodunu çağırma. BMW'den bağımsız çalışır.
volvo.gaz_ver() # Volvo hızlanır (hiz = 20)

print("\n--- Sınıf Niteliğine Erişim ---")
# Sınıf niteliğine sınıf adı üzerinden erişilir, tüm nesneler için aynıdır.
print(f"BMW'nin Tekerlek Sayısı: {bmw.tekerlek_sayisi}")
print(f"Volvo'nun Tekerlek Sayısı: {Araba.tekerlek_sayisi}")

# Nesnenin metodunu çağırarak tüm bilgileri gösterelim.
bmw.bilgileri_goster()