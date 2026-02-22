# Konu: Requests Modülü
# Amaç: İnternet üzerinden veri çekmek (API'lerle iletişim kurmak).
# NOT: Bu modül Python'la birlikte gelmez, yüklenmesi gerekir: pip install requests

import requests
import json

# ---------------------------------------------------------
# 1. TEMEL GET İSTEĞİ
# ---------------------------------------------------------
# Bir web sitesinden veri çek (GET request)

print("--- 1. Basit GET İsteği ---")
# JSONPlaceholder: Ücretsiz sahte API (test için)
url = "https://jsonplaceholder.typicode.com/users/1"

# GET isteği gönder
response = requests.get(url)

# Durum kodu kontrol et (200 = Başarılı)
print(f"Durum Kodu: {response.status_code}")

# Yanıtı JSON olarak al
veri = response.json()
print(f"Kullanıcı Adı: {veri['name']}")
print(f"E-mail: {veri['email']}")


# ---------------------------------------------------------
# 2. PARAMETRELERLE GET İSTEĞİ
# ---------------------------------------------------------
# URL'e parametre ekleyerek arama yap

print("\n--- 2. Parametreli GET İsteği ---")
url2 = "https://jsonplaceholder.typicode.com/posts"

# Parametreler (userId=1 olan postları getir)
params = {"userId": 1}

response2 = requests.get(url2, params=params)
posts = response2.json()
print(f"Kullanıcının {len(posts)} adet postu var.")
print(f"İlk Post Başlığı: {posts[0]['title']}")


# ---------------------------------------------------------
# 3. POST İSTEĞİ (Veri Gönderme)
# ---------------------------------------------------------
# Sunucuya yeni veri gönder

print("\n--- 3. POST İsteği (Veri Gönderme) ---")
url3 = "https://jsonplaceholder.typicode.com/posts"

# Gönderilecek veri
yeni_post = {
    "title": "Python ile API Kullanımı",
    "body": "Requests modülü çok kullanışlı!",
    "userId": 1
}

# POST isteği gönder
response3 = requests.post(url3, json=yeni_post)
print(f"Durum Kodu: {response3.status_code}")  # 201 = Created
print(f"Oluşturulan Post ID: {response3.json()['id']}")


# ---------------------------------------------------------
# 4. HEADER KULLANIMI
# ---------------------------------------------------------
# İsteklere özel başlıklar (headers) ekle
# Örnek: API anahtarı, içerik tipi belirtme

print("\n--- 4. Header Kullanımı ---")
url4 = "https://jsonplaceholder.typicode.com/posts/1"

# Özel başlıklar
headers = {
    "User-Agent": "Python-Requests/1.0",
    "Accept": "application/json"
}

response4 = requests.get(url4, headers=headers)
print(f"Başarılı! Durum: {response4.status_code}")


# ---------------------------------------------------------
# 5. HATA YÖNETİMİ
# ---------------------------------------------------------
# İstek başarısız olursa ne yapmalı?

print("\n--- 5. Hata Yönetimi ---")
url5 = "https://jsonplaceholder.typicode.com/users/999"  # Olmayan kullanıcı

try:
    response5 = requests.get(url5, timeout=5)  # 5 saniye timeout
    response5.raise_for_status()  # Hata varsa exception fırlat
    print("Başarılı!")
except requests.exceptions.HTTPError:
    print(f"HTTP Hatası! Durum Kodu: {response5.status_code}")
except requests.exceptions.Timeout:
    print("İstek zaman aşımına uğradı!")
except requests.exceptions.RequestException as e:
    print(f"Bir hata oluştu: {e}")


# ---------------------------------------------------------
# ÖZET: REQUESTS METODLARI
# ---------------------------------------------------------
# requests.get()     → Veri çek (Okuma)
# requests.post()    → Veri gönder (Oluşturma)
# requests.put()     → Veri güncelle (Tamamını)
# requests.patch()   → Veri güncelle (Kısmen)
# requests.delete()  → Veri sil

# ÖNEMLI PARAMETRELER:
# - url: İstek gönderilecek adres
# - params: URL parametreleri (dict)
# - json: JSON formatında gönderilecek veri (dict)
# - headers: Özel başlıklar (dict)
# - timeout: Maksimum bekleme süresi (saniye)
