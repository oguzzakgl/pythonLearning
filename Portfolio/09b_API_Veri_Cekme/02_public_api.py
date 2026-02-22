# ============================================================
# DOSYA 2 — Ücretsiz & Kayıt Gerektirmeyen Gerçek API'ler
# ============================================================
#
# Bu dosyada kayıt veya API Key gerektirmeyen,
# tamamen ücretsiz ve açık API'leri kullanacağız.
#
# API'ler:
#   1. Open-Meteo  → Hava durumu (konum bazlı)
#   2. ExchangeRate-API → Döviz kurları
#   3. RestCountries → Ülke bilgileri
# ============================================================

import requests

# ─────────────────────────────────────────────
# 1. OPEN-METEO — Hava Durumu API'si
#    Belgeleri: https://open-meteo.com/
#    Tamamen ücretsiz, API key yok!
# ─────────────────────────────────────────────

print("=" * 55)
print("1) Open-Meteo — İstanbul Hava Durumu")
print("=" * 55)

URL_HAVA = "https://api.open-meteo.com/v1/forecast"

# İstanbul koordinatları
parametreler = {
    "latitude" : 41.0082,
    "longitude": 28.9784,
    "current"  : "temperature_2m,wind_speed_10m,precipitation",
    "timezone" : "Europe/Istanbul"
}

try:
    yanit = requests.get(URL_HAVA, params=parametreler, timeout=10)
    yanit.raise_for_status()
    veri = yanit.json()

    guncel = veri["current"]
    print(f"  🌡 Sıcaklık    : {guncel['temperature_2m']} °C")
    print(f"  💨 Rüzgar      : {guncel['wind_speed_10m']} km/h")
    print(f"  🌧 Yağış       : {guncel['precipitation']} mm")
except Exception as e:
    print(f"  Hata: {e}")

# ─────────────────────────────────────────────
# 2. EXCHANGERATE-API — Güncel Döviz Kurları
#    Belgeleri: https://open.er-api.com/
#    Ücretsiz, kayıt gerektirmiyor
# ─────────────────────────────────────────────

print("\n" + "=" * 55)
print("2) ExchangeRate-API — Döviz Kurları (USD bazlı)")
print("=" * 55)

URL_KUR = "https://open.er-api.com/v6/latest/USD"

try:
    yanit = requests.get(URL_KUR, timeout=10)
    yanit.raise_for_status()
    veri = yanit.json()

    kurlar = veri["rates"]
    ilgi_duydugumuz = ["TRY", "EUR", "GBP", "JPY", "BTC"]

    print(f"  Son güncelleme: {veri['time_last_update_utc'][:16]}")
    print(f"  Baz para birimi: {veri['base_code']}\n")

    for kod in ilgi_duydugumuz:
        if kod in kurlar:
            print(f"  1 USD = {kurlar[kod]:>12.4f}  {kod}")

except Exception as e:
    print(f"  Hata: {e}")

# ─────────────────────────────────────────────
# 3. RESTCOUNTRIES — Ülke Bilgileri
#    Belgeleri: https://restcountries.com/
# ─────────────────────────────────────────────

print("\n" + "=" * 55)
print("3) RestCountries — Türkiye Bilgileri")
print("=" * 55)

URL_ULKE = "https://restcountries.com/v3.1/name/turkey"

try:
    yanit = requests.get(URL_ULKE, timeout=10)
    yanit.raise_for_status()
    veri = yanit.json()[0]  # Liste döner, ilk elemanı al

    print(f"  Ülke      : {veri['name']['common']}")
    print(f"  Başkent   : {veri['capital'][0]}")
    print(f"  Nüfus     : {veri['population']:,}")
    print(f"  Para Bir. : {list(veri['currencies'].keys())[0]}")
    print(f"  Bölge     : {veri['region']} / {veri['subregion']}")

except Exception as e:
    print(f"  Hata: {e}")

# ─────────────────────────────────────────────
# GENEL NOT: Yanıtı nasıl keşfedersin?
# ─────────────────────────────────────────────
print("\n" + "=" * 55)
print("💡 Yeni bir API'yi keşfetme taktikleri:")
print("=" * 55)
print("""
  1. yanit.json() ile tüm yanıtı print et
  2. type(veri) ile dict mi list mi anla
  3. Eğer dict ise: veri.keys() ile anahtarlara bak
  4. Eğer list ise: veri[0] ile ilk elemanı incele
  5. json.dumps(veri, indent=2) ile güzel yazdır

  Örnek keşif kodu:
    import json
    print(json.dumps(yanit.json(), indent=2, ensure_ascii=False))
""")

print("Sıradaki dosya: 03_yfinance_temeller.py")
