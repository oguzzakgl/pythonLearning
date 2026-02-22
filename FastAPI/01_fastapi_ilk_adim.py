# KONU: FastAPI'ye Giriş
# Amaç: İlk API'mizi ayağa kaldırmak ve Swagger arayüzünü görmek.

from fastapi import FastAPI

# 1. Uygulama Nesnesi (app) Oluşturulur
# Bu "app" nesnesi tüm API'mizin beyni olacak.
app = FastAPI()

# 2. Endpoint (Uç Nokta) Tanımlama
# @app.get("/") -> Site ana sayfasına (root) gelince burası çalışsın.
# async def -> FastAPI asenkron çalışmayı sever (artık biliyoruz!).
@app.get("/")
async def ana_sayfa():
    return {"mesaj": "FastAPI dünyasına hoş geldiniz!", "durum": "aktif"}

# 3. Parametre Alma
# URL üzerinden veri nasıl alınır? Örn: /urunler/5
@app.get("/urunler/{urun_id}")
async def urun_getir(urun_id: int):
    return {"urun_id": urun_id, "urun_adi": "Örnek Ürün"}

# ---------------------------------------------------------
# NASIL ÇALIŞTIRILIR? (Terminalden)
# ---------------------------------------------------------
# uvicorn 01_fastapi_ilk_adim:app --reload
#
# Açıklama:
# 01_fastapi_ilk_adim : Dosya adı (py olmadan)
# app                 : Dosya içindeki FastAPI nesnesinin adı
# --reload            : Kod değişince sunucuyu otomatik yeniden başlat
