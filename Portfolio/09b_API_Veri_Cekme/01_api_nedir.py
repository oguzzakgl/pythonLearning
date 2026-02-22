# ============================================================
# DOSYA 1 — API Nedir? requests Kütüphanesi ile İlk İstek
# ============================================================
#
# API (Application Programming Interface):
#   İki uygulamanın birbiriyle konuşmasını sağlayan "köprü".
#
# Biz ne yapacağız?
#   → İnternetteki bir sunucuya HTTP isteği göndereceğiz.
#   → Sunucu bize JSON formatında veri döndürecek.
#   → Biz de o veriyi Python'da kullanacağız.
#
# Kurulum (terminalde bir kez çalıştır):
#   pip install requests
# ============================================================

import requests  # HTTP istekleri için standart kütüphane
import json      # JSON verisini güzel yazdırmak için

# ─────────────────────────────────────────────
# BÖLÜM A — En Basit API İsteği
# ─────────────────────────────────────────────

# Kullanacağımız API: JSONPlaceholder (sahte test verisi sunar)
URL = "https://jsonplaceholder.typicode.com/todos/1"

print("=" * 50)
print("A) En basit GET isteği")
print("=" * 50)

# requests.get() → sunucuya GET isteği gönderir
yanit = requests.get(URL)

# Durum kodu kontrol et
# 200 → Başarılı  |  404 → Bulunamadı  |  500 → Sunucu Hatası
print(f"Durum Kodu : {yanit.status_code}")
print(f"İçerik Tipi: {yanit.headers['Content-Type']}")

# Yanıtı JSON'a çevir (dict gibi kullanabiliriz)
veri = yanit.json()
print(f"Gelen Veri : {veri}")
print(f"Başlık     : {veri['title']}")
print(f"Tamamlandı : {veri['completed']}")

# ─────────────────────────────────────────────
# BÖLÜM B — Hata Yönetimi (try-except)
# ─────────────────────────────────────────────

print("\n" + "=" * 50)
print("B) Hata yönetimi ile güvenli istek")
print("=" * 50)

YANLIS_URL = "https://jsonplaceholder.typicode.com/todos/99999"

try:
    yanit = requests.get(YANLIS_URL, timeout=10)  # 10 sn bekle
    yanit.raise_for_status()                        # 4xx/5xx → hata fırlat
    veri = yanit.json()
    print(f"Veri bulundu: {veri}")
except requests.exceptions.Timeout:
    print("HATA: Sunucu 10 saniyede yanıt vermedi!")
except requests.exceptions.HTTPError as e:
    print(f"HTTP Hatası: {e}")
except requests.exceptions.ConnectionError:
    print("HATA: İnternet bağlantısı yok!")

# ─────────────────────────────────────────────
# BÖLÜM C — Query Parametresi Göndermek
# ─────────────────────────────────────────────
# Bazı API'ler URL sonuna ?param=deger şeklinde parametre ister.
# requests bunu params= ile otomatik oluşturur.

print("\n" + "=" * 50)
print("C) Query parametresi ile filtreleme")
print("=" * 50)

URL_TUTTI = "https://jsonplaceholder.typicode.com/todos"
parametreler = {
    "userId": 1,       # sadece userId=1 olanlari getir
    "_limit": 3        # en fazla 3 kayıt
}

yanit = requests.get(URL_TUTTI, params=parametreler)
liste  = yanit.json()

print(f"Toplam gelen kayıt: {len(liste)}")
for todo in liste:
    durum = "✔" if todo["completed"] else "✘"
    print(f"  {durum} [{todo['id']}] {todo['title'][:40]}")

# ─────────────────────────────────────────────
# BÖLÜM D — API Anahtarı (header ile kimlik doğrulama)
# ─────────────────────────────────────────────
# Çoğu gerçek API kayıt sonrası "API Key" verir.
# Bu anahtarı genellikle header içinde gönderirsin.
#
# Örnek (gerçek bir API için — şu an çalıştırma):
#
# HEADERS = {"Authorization": "Bearer SENIN_API_KEYIN"}
# yanit = requests.get(URL, headers=HEADERS)
#
# GÜVENLİK: API anahtarını asla kod içine yazmayın!
# Bunun yerine .env dosyası ve python-dotenv kütüphanesi kullanın.
# Örnek:
#   .env dosyasında → API_KEY=abc123
#   Python'da       → import os; key = os.getenv("API_KEY")

print("\n" + "=" * 50)
print("D) API Key kullanımı — güvenli yöntem (örnek)")
print("=" * 50)
print("API Key hiçbir zaman kod içine yazılmaz!")
print("Bunun yerine .env dosyasına yaz, os.getenv() ile oku.")

# ─────────────────────────────────────────────
# ÖZET
# ─────────────────────────────────────────────
print("\n🎯 ÖĞRENDİKLERİN:")
print("  1. requests.get(url)            → GET isteği")
print("  2. yanit.status_code            → 200 = başarılı")
print("  3. yanit.json()                 → dict'e çevir")
print("  4. params={}                    → filtre/parametre")
print("  5. try-except + raise_for_status → hata yönetimi")
print("\nSıradaki dosya: 02_public_api.py")
