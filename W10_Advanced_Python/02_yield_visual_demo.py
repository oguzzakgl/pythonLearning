import time

# ---------------------------------------------------------
# YÖNTEM 1: KLASİK LİSTE (RETURN) -> "HEPSİNİ PİŞİR ÖYLE VER"
# ---------------------------------------------------------
def firinci_klasik():
    print("🍞 Fırıncı: Tamam, bekle hepsini pişirip pakete koyacağım...")
    paket = []
    for i in range(1, 6):
        time.sleep(1) # Pişirme süresi (1 saniye)
        print(f"   (Mutfakta {i}. ekmek pişti...)")
        paket.append(f"Ekmek {i}")
    
    print("🍞 Fırıncı: Hepsi bitti! Al bakalım paketi.")
    return paket

# ---------------------------------------------------------
# YÖNTEM 2: GENERATOR (YIELD) -> "PİŞTİKÇE VER"
# ---------------------------------------------------------
def firinci_modern():
    print("✨ Modern Fırıncı: Tamam, piştikçe tezgaha koyacağım, sen al.")
    for i in range(1, 6):
        time.sleep(1) # Pişirme süresi
        # YIELD BURADA! "Al bunu, ben diğerini yapmaya dönüyorum" diyor.
        yield f"Ekmek {i}" 

# =========================================================
# HADİ DENEYELİM (ÇALIŞTIR VE HIZA BAK)
# =========================================================

print("\n--- SENARYO 1: KLASİK FIRIN (LİSTE) ---")
print("Sen: Ekmekleri bekliyorum...")
# Burada 5 saniye boyunca HİÇBİR ŞEY alamazsın, beklersin.
ekmekler = firinci_klasik()
print(f"Sen: Sonunda aldım! {ekmekler}")
print("Sen: (5 saniye aç bekledim!)")


print("\n\n--- SENARYO 2: MODERN FIRIN (YIELD) ---")
print("Sen: Ekmekleri bekliyorum...")
# Burada bekleme yok! İlk ekmek pişince hemen elinde.
for ekmek in firinci_modern():
    print(f"Sen: Oh mis gibi! {ekmek} geldi, yiyorum.")
    
print("Sen: (Hiç aç beklemedim, piştikçe yedim!)")
