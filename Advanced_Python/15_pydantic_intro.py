# KONU: Pydantic (Veri Doğrulama ve Ayarlar)
# Amaç: Gelen verinin tipini kontrol etmek, dönüştürmek ve hata fırlatmak.
# FastAPI bu kütüphaneyi kullanır.

# ÖNCE KURULUM GEREKİR: pip install pydantic

from pydantic import BaseModel, ValidationError, Field
from typing import List, Optional

# =============================================================================
# 1. TEMEL KULLANIM (BaseModel)
# =============================================================================
# Dataclasses'a çok benzer ama "BaseModel"den miras alırız.
class Kullanici(BaseModel):
    ad: str
    yas: int
    email: str
    aktif_mi: bool = True # Varsayılan değer

# =============================================================================
# 2. DOĞRULAMA GÜCÜ (Validation)
# =============================================================================
# Pydantic, veri tiplerini otomatik zorlar ve dönüştürür.
try:
    print("\n--- 1. Başarılı Örnek ---")
    # "yas": "25" (string) yollasak bile int'e çevirir!
    k1 = Kullanici(ad="Ahmet", yas="25", email="ahmet@mail.com")
    print(k1)
    print(f"Yaş Tipi: {type(k1.yas)}") # <class 'int'> yazar!

    print("\n--- 2. Hatalı Örnek (Validation Error) ---")
    # "yas" yerine "yirmi" yazarsak ne olur?
    k2 = Kullanici(ad="Mehmet", yas="yirmi", email="mehmet@mail.com")

except ValidationError as e:
    print("HATA YAKALANDI! 🚨")
    print(e.json()) # Hatanın detayını JSON olarak verir.

# =============================================================================
# 3. DETAYLI KISITLAMALAR (Field)
# =============================================================================
class Urun(BaseModel):
    ad: str
    # gt=0: 0'dan büyük olmalı (Greater Than)
    # le=1000: 1000'den küçük veya eşit (Less Equals)
    fiyat: float = Field(gt=0, description="Ürün fiyatı pozitif olmalı")
    adet: int = Field(default=1, ge=1) # ge: Greater Equals (1 veya daha büyük)

try:
    print("\n--- 3. Field Kısıtlamaları ---")
    u1 = Urun(ad="Laptop", fiyat=15000, adet=1)
    print(u1)
    
    # Hatalı Fiyat Denemesi (-500)
    u2 = Urun(ad="Hatalı Ürün", fiyat=-500) 

except ValidationError as e:
    print("Fiyat Hatası Yakalandı!")
    print(e)



class Student(BaseModel):
    name: str
    age: int
    lectures: List[str]

data = {
    "name": "ouz",
    "age": 25,
    # "age": "25" (string) yollarsak bile int'e çevirir çünk gelen verinin int olması gerektiğini söylüyoruz.
    "lectures": ["Math", "Science", "History"],
    "no": 1384168 # fazla key gönderilse bile kabul etmez
}

student = Student(**data)
print(student)