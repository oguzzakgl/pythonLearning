# PROJE: Mini Log Kaydedici
# Konu: Async/Await ve Context Managers (with)
# Amaç: 3 farklı "sahte" sunucudan veri geliyormuş gibi yapıp, bunları aynı anda (asenkron) dosyaya kaydetmek.

import asyncio
import time

# GÖREV 1: Veri Getiren Asenkron Fonksiyon
# Bu fonksiyon "sunucu_adi" ve "bekleme_suresi" alacak.
# Belirtilen süre kadar uyuyacak (asyncio.sleep).
# Sonra "Sunucu X verisi hazır!" diye string döndürecek.
async def veri_getir(sunucu_adi: str, sure: int) -> str:
    print(f"⏳ {sunucu_adi} verisi isteniyor... ({sure} sn sürecek)")
    await asyncio.sleep(sure)
    return f"{sunucu_adi} verisi: [OK]"

# GÖREV 2: Ana Çalıştırıcı Fonksiyon
# Bu fonksiyon 3 farklı sunucudan veriyi AYNI ANDA (gather) isteyecek.
# Gelen verileri "loglar.txt" dosyasına WITH ile kaydedecek.
async def ana_program():
    print("--- SİSTEM BAŞLATILIYOR ---")
    baslangic = time.time()

    # 1. Verileri Topla (gather kullan)
    # Sunucu 1 (2 saniye), Sunucu 2 (1 saniye), Sunucu 3 (3 saniye)
    # sonuclar = await asyncio.gather( ... )

    sonuclar = await asyncio.gather(
        veri_getir("Sunucu 1", 2),
        veri_getir("Sunucu 2", 1),
        veri_getir("Sunucu 3", 3)
    )
    
    # 2. Dosyaya Kaydet (with open kullan)
    # "loglar.txt" dosyasını aç ve gelen sonuçları içine yaz.
    with open("loglar.txt", "w", encoding="utf-8") as dosya:
        for sonuc in sonuclar:
            dosya.write(f"{sonuc}\n")

    bitis = time.time()
    print(f"✅ Tüm işlemler bitti! Toplam Süre: {bitis - baslangic:.2f} saniye")

# ÇALIŞTIRMA
if __name__ == "__main__":
    asyncio.run(ana_program())
