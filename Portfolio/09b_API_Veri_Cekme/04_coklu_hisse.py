# ============================================================
# DOSYA 4 — Çoklu Hisse Senedi: Döngü + Birleştirme
# ============================================================
#
# Bu dosyada birden fazla hisseyi aynı anda çekip
# tek bir DataFrame'de birleştirmeyi öğreneceğiz.
# ============================================================

import yfinance as yf
import pandas as pd

# ─────────────────────────────────────────────
# YÖNTEM 1 — for döngüsü ile tek tek çek, birleştir
# ─────────────────────────────────────────────

print("=" * 55)
print("Yöntem 1: for döngüsü")
print("=" * 55)

hisseler = ["AAPL", "TSLA", "GOOGL"]
sonuclar = {}  # Her hissenin verisini bir dict'te tut

for sembol in hisseler:
    df = yf.Ticker(sembol).history(period="1mo", interval="1d")
    sonuclar[sembol] = df["Close"]   # Sadece kapanış fiyatını al
    print(f"  {sembol}: {len(df)} günlük veri çekildi")

# Tüm serileri birleştir → Her sütun bir hisse
df_birlestir = pd.DataFrame(sonuclar)
df_birlestir.index = df_birlestir.index.tz_localize(None)  # saat dilimini temizle

print("\nBirleşik DataFrame (son 5 satır):")
print(df_birlestir.tail().round(2))

# ─────────────────────────────────────────────
# YÖNTEM 2 — yf.download() ile hepsini bir anda çek
# ─────────────────────────────────────────────

print("\n" + "=" * 55)
print("Yöntem 2: yf.download() — daha hızlı!")
print("=" * 55)

df_toplu = yf.download(
    tickers  = ["AAPL", "MSFT", "AMZN"],
    period   = "3mo",
    interval = "1d",
    progress = False   # yükleme çubuğunu kapat
)

# Sadece Close fiyatlarını al
kapanis = df_toplu["Close"]
print("Kapanis fiyatlari (ilk 3 satır):")
print(kapanis.head(3).round(2))

# ─────────────────────────────────────────────
# BÖLÜM B — Türk hisseleri karşılaştırması
# ─────────────────────────────────────────────

print("\n" + "=" * 55)
print("Türk Hisseleri — 6 Aylık Karşılaştırma")
print("=" * 55)

turk_hisseler = ["THYAO.IS", "ASELS.IS", "BIMAS.IS", "SISE.IS"]
turk_df       = {}

for sembol in turk_hisseler:
    try:
        df = yf.Ticker(sembol).history(period="6mo", interval="1d")
        if not df.empty:
            turk_df[sembol] = df["Close"]
            ilk   = df["Close"].iloc[0]
            son   = df["Close"].iloc[-1]
            degisim = ((son / ilk) - 1) * 100
            print(f"  {sembol:<12} | {ilk:>8.2f} → {son:>8.2f} TRY | %{degisim:+.1f}")
        else:
            print(f"  {sembol:<12} | Veri bulunamadı")
    except Exception as e:
        print(f"  {sembol:<12} | Hata: {e}")

# ─────────────────────────────────────────────
# BÖLÜM C — Basit analizler
# ─────────────────────────────────────────────

print("\n" + "=" * 55)
print("Basit Analizler (toplanan veriler üzerinde)")
print("=" * 55)

if turk_df:
    df_turk = pd.DataFrame(turk_df)
    df_turk.index = df_turk.index.tz_localize(None)

    print("\n1) Korelasyon matrissi (1.0 = mükemmel pozitif ilişki):")
    print(df_turk.pct_change().corr().round(3))

    print("\n2) 6 ay içindeki en yüksek kapanış fiyatları:")
    print(df_turk.max().round(2))

    print("\n3) Ortalama günlük değişim (%):")
    gunluk_getiri = df_turk.pct_change() * 100
    print(gunluk_getiri.mean().round(3))

# ─────────────────────────────────────────────
# ÖZET
# ─────────────────────────────────────────────
print("\n🎯 ÖĞRENDİKLERİN:")
print("  sonuclar = {}                → dict ile çoklu veri topla")
print("  pd.DataFrame(sonuclar)       → dict'i DataFrame'e çevir")
print("  yf.download(tickers=[...])   → toplu indirme")
print("  .pct_change()                → günlük % değişim")
print("  .corr()                      → korelasyon matrisi")
print("\nSıradaki dosya: 05_kaydet_yukle.py")
