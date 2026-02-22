# KONU: Yanıt Modelleri (Response Models)
# Amaç: API'den kullanıcıya dönerken HANGİ verilerin gideceğini seçmek.
# Problem: Veritabanında "şifre" var ama biz kullanıcıya şifresini geri göndermemeliyiz!

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

# ---------------------------------------------------------
# 1. MODELLER
# ---------------------------------------------------------

# A) KULLANICININ BİZE GÖNDERDİĞİ (İçinde şifre var)
class KullaniciKayit(BaseModel):
    isim: str
    email: EmailStr
    sifre: str  # <--- Bu çok gizli!

# B) BİZİM KULLANICIYA DÖNDÜĞÜMÜZ (Şifre YOK)
class KullaniciBilgi(BaseModel):
    isim: str
    email: EmailStr
    # Sifre alanını buraya kasten koymadık.

# ---------------------------------------------------------
# 2. ENDPOINT
# ---------------------------------------------------------

# response_model=KullaniciBilgi -> "Fonksiyon ne döndürürse döndürsün,
# sen sadece KullaniciBilgi içindeki alanları (isim, email) al, gerisini at!"
@app.post("/kullanici-kayit", response_model=KullaniciBilgi)
async def kullanici_kayit(kullanici: KullaniciKayit):
    
    # Simülasyon: Veriyi veritabanına kaydettik (Şifreyle beraber)
    kaydedilen_veri = kullanici.model_dump()
    print(f"Veritabanına Kaydedilen: {kaydedilen_veri}") 
    # Terminalde şifreyi görebilirsiniz, veritabanına tam gider.
    
    # AMA kullanıcıya yanıt dönerken:
    return kaydedilen_veri 
    # Biz burada "sifre"yi de gönderiyoruz ASLINDA...
    # FAKAT FastAPI (response_model sayesinde) o şifreyi "süzgeçten geçirip" silecek.

# Çalıştırmak için:
# uvicorn 05_fastapi_response_model:app --reload

# Test:
# 1. Swagger'dan bir kullanıcı oluşturun (şifre yazın).
# 2. "Response body" kısmına bakın. Şifre alanı YOK UÇMUŞ! 🎩✨
