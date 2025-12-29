# KONU: Dataclasses (Veri Sınıfları)
# Amaç: "Klasik Sınıf" yazmanın getirdiği hamallıktan kurtulmak.

from dataclasses import dataclass, field

# =============================================================================
# 1. KARŞILAŞTIRMA: KLASİK YÖNTEM vs DATACLASS
# =============================================================================
# Senaryo: Bir "Araba" verisini tutmak istiyoruz.

# --- YÖNTEM A: KLASİK (ESKİ) YÖNTEM ---
# Her şeyi (Constructor, yazdırma, kıyaslama) ELLE yazmak zorundayız.
class ArabaKlasik:
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil

    # Bunu yazmazsak ekranda saçma şeyler (örn: <__main__.Araba object at 0x...>) çıkar.
    def __repr__(self):
        return f"ArabaKlasik(marka='{self.marka}', model='{self.model}', yil={self.yil})"

    # Bunu yazmazsak iki aynı arabaya "eşit" diyemeyiz.
    def __eq__(self, diger):
        if not isinstance(diger, ArabaKlasik): return False
        return (self.marka == diger.marka and self.model == diger.model)

# --- YÖNTEM B: DATACLASS (YENİ) YÖNTEM ---
# Sadece değişkenleri tanımlarız. Python gerisini (__init__, __repr__, __eq__) HALLEDER.
@dataclass
class ArabaYeni:
    marka: str
    model: str
    yil: int
    renk: str = "Beyaz" # Varsayılan değer de verebiliriz.

# =============================================================================
# 2. DETAYLAR VE EKSTRA GÜÇLER
# =============================================================================

@dataclass
class Siparis:
    urun_adi: str
    miktar: int
    birim_fiyat: float
    # field(init=False) -> Kullanıcıdan isteme, biz hesaplayacağız.
    toplam_fiyat: float = field(init=False)
    # Liste için "field(default_factory=list)" kullanmak EN GÜVENLİ yoldur.
    hediyeler: list = field(default_factory=list)

    def __post_init__(self):
        # Sınıf oluştuktan hemen sonra çalışır. Hesaplamaları burada yaparız.
        self.toplam_fiyat = self.miktar * self.birim_fiyat

# =============================================================================
# TESTLER
# =============================================================================
if __name__ == "__main__":
    print("\n--- 1. GÖRÜNÜM FARKI ---")
    k1 = ArabaKlasik("Toyota", "Corolla", 2020)
    y1 = ArabaYeni("Toyota", "Corolla", 2020)
    
    print(f"Klasik: {k1}") # __repr__ metodunu biz yazdık diye düzgün çıktı.
    print(f"Yeni:   {y1}") # Hiçbir şey yazmadık ama Dataclass otomatik halletti!

    print("\n--- 2. KIYASLAMA FARKI ---")
    k2 = ArabaKlasik("Toyota", "Corolla", 2020)
    y2 = ArabaYeni("Toyota", "Corolla", 2020)

    print(f"Klasik Eşit mi? {k1 == k2}") # __eq__ yazdığımız için True (Yazmasaydık False olurdu!)
    print(f"Yeni Eşit mi?   {y1 == y2}") # Dataclass bunu da otomatik yaptı.

    print("\n--- 3. HESAPLAMA ÖRNEĞİ ---")
    siparis = Siparis("Laptop", 2, 15000)
    siparis.hediyeler.append("Mouse")
    print(siparis)
    print(f"Hesaplanan Tutar: {siparis.toplam_fiyat} TL")
