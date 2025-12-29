# FastAPI Stok Yönetim API'si
# Bu dosya, profesyonel bir REST API'nin temelini oluşturacak.

from fastapi import FastAPI

# 1. UYGULAMA OLUŞTURMA (App instance)
# ...

# 2. VERİ MODELİ (Pydantic)
# Hangi verileri alıp göndereceğiz? (Ürün adı, fiyatı vb.)
# ...

# 3. ENDPOINTLER (API Uçları)
# - Ürünleri Listele (GET)
# - Yeni Ürün Ekle (POST)
# - Ürün Sil (DELETE)
# ...

# 4. SUNUCU AYARLARI (Uvicorn ile çalıştırma)
# Komut: uvicorn main:app --reload
