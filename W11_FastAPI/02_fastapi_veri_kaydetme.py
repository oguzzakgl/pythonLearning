# KONU: FastAPI ile Veri Kaydetme ve Listeleme (Simülasyon)
# Amaç: Bir "Sahte Veritabanı" oluşturup içine veri eklemek (POST) ve okumak (GET).

from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

# ---------------------------------------------------------
# 1. SAHTE VERİTABANI (Liste)
# ---------------------------------------------------------
# Gerçek hayatta burada SQL olur, şimdilik listeyi veritabanı gibi kullanacağız.
kullanici_db = [
    {"id": 1, "isim": "Ahmet", "soyisim": "Yılmaz", "sifre": "1234"},
    {"id": 2, "isim": "Ayşe", "soyisim": "Demir", "sifre": "abcd"},
    {"id": 3, "isim": "Mehmet", "soyisim": "Kaya", "sifre": "5678"},
]

# ---------------------------------------------------------
# 2. VERİ DOĞRULAMA (Pydantic Model)
# ---------------------------------------------------------
class KullaniciKayit(BaseModel):
    isim: str
    soyisim: str
    sifre: str

# ---------------------------------------------------------
# 3. ENDPOINTLER (API Uçları)
# ---------------------------------------------------------

# A) TÜM KULLANICILARI GETİR (GET)
@app.get("/kullanicilar")
async def kullanicilari_getir():
    return {"toplam_kayit": len(kullanici_db), "veriler": kullanici_db}

# B) YENİ KULLANICI EKLE (POST)
# Pydantic modeli (KullaniciKayit) sayesinde gelen veriyi otomatik kontrol ederiz.
@app.post("/kullanici-ekle")
async def kullanici_ekle(yeni_kullanici: KullaniciKayit):
    # Yeni bir ID üretelim (Listenin sonundaki ID + 1)
    yeni_id = kullanici_db[-1]["id"] + 1 if kullanici_db else 1
    
    # Kullanıcı verisini sözlüğe çevirip ID ekle
    kayit = yeni_kullanici.model_dump() # Pydantic modelini dict'e çevirir
    kayit["id"] = yeni_id
    
    # "Veritabanına" ekle
    kullanici_db.append(kayit)
    
    return {"mesaj": "Kullanıcı başarıyla kaydedildi!", "yeni_kayit": kayit}

# C) RASTGELE KULLANICI EKLE (TEST AMAÇLI)
@app.post("/rastgele-ekle")
async def rastgele_ekle():
    isimler = ["Ali", "Veli", "Can", "Zeynep", "Elif"]
    soyisimler = ["Yıldız", "Öztürk", "Çelik", "Arslan"]
    
    secilen_isim = random.choice(isimler)
    secilen_soyisim = random.choice(soyisimler)
    secilen_sifre = str(random.randint(1000, 9999))
    
    yeni_id = kullanici_db[-1]["id"] + 1 if kullanici_db else 1
    
    yeni_kayit = {
        "id": yeni_id,
        "isim": secilen_isim,
        "soyisim": secilen_soyisim,
        "sifre": secilen_sifre
    }
    
    kullanici_db.append(yeni_kayit)
    return {"mesaj": "Rastgele kullanıcı oluşturuldu", "kayit": yeni_kayit}

# Çalıştırmak için:
# uvicorn 02_fastapi_veri_kaydetme:app --reload
