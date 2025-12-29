# Konu: Asynchronous Programming (Eş Zamansız Programlama)
# Amaç: Bir işlem bitmeden diğerine geçebilmek (Hız ve Performans).
# Özellikle Web Scraping, API İstekleri ve Veritabanı işlemlerinde kullanılır.

import asyncio
import time

# ---------------------------------------------------------
# 1. SENKRON (KLASİK) YAKLAŞIM - SIRAYLA YAPAR
# ---------------------------------------------------------
# Bir iş bitmeden diğerine geçmez. Bloklar.

def dosya_indir_senkron(dosya_adi):
    print(f"⬇️  {dosya_indir_senkron.__name__}: {dosya_adi} indiriliyor...")
    time.sleep(2) # 2 saniye bekle (Bloklar)
    print(f"✅ {dosya_indir_senkron.__name__}: {dosya_adi} İNDİ.")

def senkron_calistir():
    print("\n--- SENKRON (SIRAYLA) BAŞLADI ---")
    baslangic = time.time()
    
    dosya_indir_senkron("Resim1.jpg")
    dosya_indir_senkron("Resim2.jpg")
    dosya_indir_senkron("Resim3.jpg")
    
    bitis = time.time()
    print(f"⏳ Senkron Toplam Süre: {bitis - baslangic:.2f} saniye")


# ---------------------------------------------------------
# 2. ASENKRON (MODERN) YAKLAŞIM - AYNI ANDA YAPAR
# ---------------------------------------------------------
# Bir işi beklerken diğerine geçer. Bloklamaz.
# async def: Bu fonksiyonun asenkron olduğunu belirtir.
# await: "Bu işlemin bitmesini bekle ama o sırada boş durma, başka iş varsa yap" der.

async def dosya_indir_asenkron(dosya_adi):
    print(f"⬇️  {dosya_indir_asenkron.__name__}: {dosya_adi} indiriliyor...")
    await asyncio.sleep(2) # 2 saniye bekle (Bloklamaz, diğerine geçer)
    print(f"✅ {dosya_indir_asenkron.__name__}: {dosya_adi} İNDİ.")

async def asenkron_calistir():
    print("\n--- ASENKRON (AYNI ANDA) BAŞLADI ---")
    baslangic = time.time()
    
    # gather: Tüm görevleri topla ve aynı anda başlat
    await asyncio.gather(
        dosya_indir_asenkron("Resim1.jpg"),
        dosya_indir_asenkron("Resim2.jpg"),
        dosya_indir_asenkron("Resim3.jpg")
    )
    
    bitis = time.time()
    print(f"⚡ Asenkron Toplam Süre: {bitis - baslangic:.2f} saniye")


# ---------------------------------------------------------
# ÇALIŞTIRMA
# ---------------------------------------------------------
if __name__ == "__main__":
    # 1. Senkron Test
    senkron_calistir()
    
    # 2. Asenkron Test
    # Asenkron fonksiyonlar direkt çağrılmaz, asyncio.run() ile çalıştırılır.
    asyncio.run(asenkron_calistir())
