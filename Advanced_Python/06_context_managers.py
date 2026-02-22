# Konu: Context Managers (with İfadesi)
# Amaç: Kaynakları (Dosya, Veritabanı) güvenli bir şekilde açıp kapatmak.
# "Açtığını kapatmayı unutma" kuralını otomatikleştirir.

# ---------------------------------------------------------
# 1. ESKİ YÖNTEM (GÜVENSİZ)
# ---------------------------------------------------------
# Eğer işlem sırasında hata çıkarsa, dosya açık kalır!
# Bu da belleği şişirir ve dosyayı bozar.

print("--- 1. Eski Yöntem ---")
try:
    dosya = open("notlar.txt", "w", encoding="utf-8")
    dosya.write("Bu eski yöntemle yazıldı.")
    # Burada hata olsa dosya.close() çalışmazdı!
finally:
    dosya.close() # Kapatmayı biz manuel yapıyoruz.
    print("Dosya manuel kapatıldı.")


# ---------------------------------------------------------
# 2. MODERN YÖNTEM (WITH - GÜVENLİ)
# ---------------------------------------------------------
# Blok bitince dosya OTOMATİK kapanır. Hata olsa bile kapanır.

print("\n--- 2. Modern Yöntem (with) ---")
with open("notlar.txt", "w", encoding="utf-8") as dosya:
    dosya.write("Bu modern yöntemle (with) yazıldı.")
    print("Dosya şu an açık ve yazılıyor...")

# Blok bittiği an dosya kapandı.
print("Dosya otomatik kapatıldı.")


# ---------------------------------------------------------
# 3. KENDİ CONTEXT MANAGER'IMIZI YAZALIM
# ---------------------------------------------------------
# Magic Methods: __enter__ (Giriş) ve __exit__ (Çıkış)

class DosyaAcici:
    def __init__(self, dosya_adi):
        self.dosya_adi = dosya_adi
    
    def __enter__(self):
        print(f"\n📂 {self.dosya_adi} açılıyor...")
        self.dosya = open(self.dosya_adi, "w", encoding="utf-8")
        return self.dosya
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.dosya.close()
        print(f"🔒 {self.dosya_adi} güvenle kapatıldı.")
        # Hata varsa True döndürerek hatayı yutabiliriz (Genelde yapılmaz)

print("\n--- 3. Kendi Context Manager'ımız ---")
with DosyaAcici("ozel_dosya.txt") as f:
    f.write("Kendi yazdığımız sınıf ile dosya açtık!")
    print("İşlem yapılıyor...")
