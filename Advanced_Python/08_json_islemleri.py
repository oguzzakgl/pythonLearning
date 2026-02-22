# Konu: JSON İşlemleri
# Amaç: Veriyi JSON formatında kaydetmek ve okumak.
# JSON: JavaScript Object Notation (Web'in evrensel veri formatı)

import json

# ---------------------------------------------------------
# 1. PYTHON OBJESINI JSON'A ÇEVİRME (Serialization)
# ---------------------------------------------------------
# Python dictionary'sini JSON string'e çevir

kullanici = {
    "isim": "Ali",
    "yas": 25,
    "sehir": "İstanbul",
    "aktif": True,
    "hobiler": ["Kitap", "Müzik", "Spor"]
}

# json.dumps() = Dictionary'yi JSON string'e çevirir
# Parametreler:
#   - indent=2: Her satırı 2 boşluk girintili yazar (okunabilir hale getirir)
#   - ensure_ascii=False: Türkçe karakterleri düzgün gösterir (ş, ğ, ü vb.)
#   - sort_keys=True: Anahtarları alfabetik sıraya koyar
json_string = json.dumps(kullanici, indent=2, ensure_ascii=False, sort_keys=True)
print("--- Python → JSON ---")
print(json_string)


# ---------------------------------------------------------
# 2. JSON'U PYTHON OBJESINE ÇEVİRME (Deserialization)
# ---------------------------------------------------------
# JSON string'i Python dictionary'sine çevir

json_veri = '{"isim": "Ayşe", "yas": 30, "sehir": "Ankara"}'

# json.loads() = JSON string'i Python objesine çevirir
# "loads" = "load string" anlamına gelir
python_obj = json.loads(json_veri)
print("\n--- JSON → Python ---")
print(f"İsim: {python_obj['isim']}")
print(f"Yaş: {python_obj['yas']}")


# ---------------------------------------------------------
# 3. DOSYAYA KAYDETME (dump)
# ---------------------------------------------------------
# Python objesini JSON dosyasına kaydet

veriler = {
    "kullanicilar": [
        {"id": 1, "isim": "Ali", "email": "ali@gmail.com"},
        {"id": 2, "isim": "Veli", "email": "veli@hotmail.com"}
    ],
    "toplam": 2
}

# json.dump() = Python objesini DOSYAYA yazar
# "dump" = "dumps" ile aynı ama dosyaya direkt yazar (string döndürmez)
# Parametreler:
#   - veriler: Kaydedilecek Python objesi
#   - f: Dosya objesi (with open ile açılan)
#   - indent=2: Girintili (okunabilir) format
#   - ensure_ascii=False: Türkçe karakter desteği
#   - sort_keys=True: Anahtarları alfabetik sıralar
with open("kullanicilar.json", "w", encoding="utf-8") as f:
    json.dump(veriler, f, indent=2, ensure_ascii=False, sort_keys=True)

print("\n--- Dosyaya Kaydedildi ---")
print("kullanicilar.json dosyası oluşturuldu.")


# ---------------------------------------------------------
# 4. DOSYADAN OKUMA (load)
# ---------------------------------------------------------
# JSON dosyasını oku ve Python objesine çevir

# json.load() = DOSYADAN okur ve Python objesine çevirir
# "load" = "loads" ile aynı ama dosyadan okur (string almaz)
with open("kullanicilar.json", "r", encoding="utf-8") as f:
    okunan_veri = json.load(f)

print("\n--- Dosyadan Okundu ---")
print(f"Toplam Kullanıcı: {okunan_veri['toplam']}")
for kullanici in okunan_veri['kullanicilar']:
    print(f"- {kullanici['isim']} ({kullanici['email']})")


# ---------------------------------------------------------
# 5. GERÇEK HAYAT ÖRNEĞİ: API YANITI
# ---------------------------------------------------------
# Web API'lerden gelen veri genelde JSON formatındadır
# Örnek: Hava durumu API'si, Twitter API'si, Google Maps API'si

api_yaniti = """
{
    "durum": "basarili",
    "veri": {
        "hava_durumu": "Güneşli",
        "sicaklik": 25,
        "nem": 60
    }
}
"""

hava = json.loads(api_yaniti)
print("\n--- API Yanıtı ---")
print(f"Durum: {hava['durum']}")
print(f"Hava: {hava['veri']['hava_durumu']}")
print(f"Sıcaklık: {hava['veri']['sicaklik']}°C")


# ---------------------------------------------------------
# ÖZET: HANGI METODU NE ZAMAN KULLANMALIYIM?
# ---------------------------------------------------------
# json.dumps()  → Python → JSON string (Bellekte)
# json.loads()  → JSON string → Python (Bellekte)
# json.dump()   → Python → JSON dosyası (Dosyaya yaz)
# json.load()   → JSON dosyası → Python (Dosyadan oku)
