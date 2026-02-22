# KONU: İleri Seviye Veri Doğrulama (Advanced Validation)
# Amaç: Kullanıcının girdiği verileri "daha kodun içine girmeden" filtrelemek.
# Şifre kısa mı? E-posta formatı yanlış mı? Fiyat negatif mi girilmiş? Bunları Pydantic halleder.

from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr

app = FastAPI()

# ---------------------------------------------------------
# 1. GELİŞMİŞ MODEL (Kurallı)
# ---------------------------------------------------------
class UrunKayit(BaseModel):
    # Field(...) sayesinde kurallar ekliyoruz.
    
    # Kural 1: İsim boş olamaz, en az 3, en fazla 50 karakter olmalı.
    isim: str = Field(..., min_length=3, max_length=50, title="Ürün Adı")
    
    # Kural 2: Fiyat 0'dan büyük olmalı (gt = greater than).
    fiyat: float = Field(..., gt=0, description="Ürünün satış fiyatı")
    
    # Kural 3: Stok negatif olamaz ama 0 olabilir (ge = greater or equal).
    stok: int = Field(default=0, ge=0)
    
    # Kural 4: Kategori opsiyoneldir (zorunlu değil), varsayılanı "Genel" dir.
    kategori: str | None = Field(default="Genel", max_length=20)

# Kullanıcı Modeli (Regex Örneği)
class KullaniciKayit(BaseModel):
    # Kural 5: E-posta formatı kontrolü (EmailStr için 'email-validator' kütüphanesi gerekir)
    # Şimdilik basit String yapalım, Regex ile kontrol edelim.
    # Regex: Sadece harf ve sayılardan oluşsun (Örnek).
    kullanici_adi: str = Field(..., pattern="^[a-zA-Z0-9_]+$")
    
    # Kural 6: Şifre en az 8 karakter.
    sifre: str = Field(..., min_length=8)

@app.post("/urun-ekle")
async def urun_ekle(urun: UrunKayit):
    # Eğer buraya girdiyse, Pydantic tüm kuralları (min_length, gt vs.) ZATEN KONTROL ETMİŞTİR.
    # if urun.fiyat < 0: ... diye kod yazmana GEREK YOK!
    return {"mesaj": "Ürün kurallara uygun!", "veri": urun}

@app.post("/kullanici-ekle")
async def kullanici_ekle(kullanici: KullaniciKayit):
    return {"mesaj": "Kullanıcı adı ve şifre geçerli!", "kullanici": kullanici.kullanici_adi}

# Çalıştırma:
# uvicorn 04_fastapi_validation:app --reload

# Test ederken:
# 1. Fiyatı -10 gönderin -> Hata verir.
# 2. İsmi "A" gönderin -> Hata verir.
# 3. İşi FastAPI sizin yerinize yapar!
