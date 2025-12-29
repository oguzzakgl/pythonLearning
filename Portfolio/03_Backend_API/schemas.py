from pydantic import BaseModel

# VERİ ŞEMALARI (Pydantic)
# Kullanıcıdan gelen veriyi kontrol etmek için kullanılır.

# 1. Kayıt Modeli (Kullanıcı yeni ürün eklerken)
class ProductCreate(BaseModel):
    # name: str
    # price: float
    # stock: int (Varsayılan 0 olabilir)
    pass

# 2. Okuma Modeli (Kullanıcıya veri gösterirken)
class ProductOut(ProductCreate):
    # id: int
    pass
