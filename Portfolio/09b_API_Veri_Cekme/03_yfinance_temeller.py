# ============================================================
# DOSYA 3 — yfinance ile Yahoo Finance API'si
# ============================================================
#
# yfinance: Yahoo Finance'in gayri resmi Python sarmalayıcısı.
# API key gerektirmez, tamamen ücretsizdir.
#
# Kurulum:
#   pip install yfinance pandas
#
# Neler çekebilirsin?
#   • Hisse senedi geçmiş fiyatları (Open, High, Low, Close, Volume)
#   • Kripto para fiyatları (BTC-USD, ETH-USD, ...)
#   • Döviz çiftleri (EURUSD=X)
#   • ETF'ler, endeksler (SPY, QQQ, ^GSPC, XU100.IS)
# ============================================================

import yfinance as yf
import pandas as pd

# ─────────────────────────────────────────────
# BÖLÜM A — Tek Hisse: Temel Kullanım
# ─────────────────────────────────────────────

print("=" * 55)
print("A) Tek hisse — Apple (AAPL)")
print("=" * 55)

# Ticker nesnesi oluştur
hisse = yf.Ticker("AAPL")

# Geçmiş fiyatları çek
# period seçenekleri: "1d","5d","1mo","3mo","6mo","1y","2y","5y","max"
# interval seçenekleri: "1m","5m","15m","1h","1d","1wk","1mo"
df = hisse.history(period="1mo", interval="1d")

print(f"Veri şekli  : {df.shape}  (satır × sütun)")
print(f"Kolonlar    : {list(df.columns)}")
print(f"İlk tarih   : {df.index[0].date()}")
print(f"Son tarih   : {df.index[-1].date()}")
print("\nİlk 3 satır:")
print(df[["Open", "High", "Low", "Close", "Volume"]].head(3).round(2))

# ─────────────────────────────────────────────
# BÖLÜM B — Temel Bilgiler (info)
# ─────────────────────────────────────────────

print("\n" + "=" * 55)
print("B) Şirket temel bilgileri")
print("=" * 55)

bilgi = hisse.info

# Tüm anahtarları görmek için: print(bilgi.keys())
ilginc_alanlar = [
    "shortName", "sector", "industry",
    "marketCap", "trailingPE", "dividendYield",
    "fiftyTwoWeekHigh", "fiftyTwoWeekLow"
]

for alan in ilginc_alanlar:
    deger = bilgi.get(alan, "Mevcut değil")
    print(f"  {alan:<22}: {deger}")

# ─────────────────────────────────────────────
# BÖLÜM C — Türk Hisseleri (.IS uzantısı)
# ─────────────────────────────────────────────

print("\n" + "=" * 55)
print("C) Türk hissesi — THYAO (Türk Hava Yolları)")
print("=" * 55)

# ISE (İstanbul Menkul Kıymetler Borsası) için sembol sonuna .IS ekle
thy = yf.Ticker("THYAO.IS")
df_thy = thy.history(period="3mo", interval="1d")

print(f"THYAO — son {len(df_thy)} günlük veri")
print(f"3 ay önceki kapanış: {df_thy['Close'].iloc[0]:.2f} TRY")
print(f"Bugünkü kapanış    : {df_thy['Close'].iloc[-1]:.2f} TRY")
degisim = ((df_thy['Close'].iloc[-1] / df_thy['Close'].iloc[0]) - 1) * 100
print(f"3 aylık değişim    : %{degisim:.1f}")

# ─────────────────────────────────────────────
# BÖLÜM D — Kripto Para
# ─────────────────────────────────────────────

print("\n" + "=" * 55)
print("D) Kripto — Bitcoin (BTC-USD)")
print("=" * 55)

btc = yf.Ticker("BTC-USD")
df_btc = btc.history(period="7d", interval="1h")

print(f"Son 7 gün, saatlik: {len(df_btc)} satır")
print(f"En yüksek fiyat   : ${df_btc['High'].max():,.0f}")
print(f"En düşük fiyat    : ${df_btc['Low'].min():,.0f}")
print(f"Güncel fiyat      : ${df_btc['Close'].iloc[-1]:,.0f}")

# ─────────────────────────────────────────────
# BÖLÜM E — Güncel Fiyat (download yöntemi)
# ─────────────────────────────────────────────

print("\n" + "=" * 55)
print("E) yf.download() — alternatif veri çekme yöntemi")
print("=" * 55)

# download() hem tek hem çoklu hisse için çalışır
df_down = yf.download("MSFT", period="5d", progress=False)
print("Microsoft son 5 gün:")
print(df_down["Close"].round(2))

# ─────────────────────────────────────────────
# ÖZET
# ─────────────────────────────────────────────
print("\n🎯 ÖĞRENDİKLERİN:")
print("  yf.Ticker(sembol)          → hisse nesnesi")
print("  .history(period, interval) → OHLCV DataFrame")
print("  .info                      → temel bilgiler (dict)")
print("  yf.download(sembol)        → hızlı indirme")
print("  Sembol örnekleri:")
print("    ABD   : AAPL, TSLA, GOOGL, MSFT, AMZN")
print("    Türkiye: THYAO.IS, ASELS.IS, BIMAS.IS, SISE.IS")
print("    Kripto : BTC-USD, ETH-USD, BNB-USD")
print("    Endeks : ^GSPC (S&P500), ^IXIC (NASDAQ), XU100.IS")
print("\nSıradaki dosya: 04_coklu_hisse.py")
