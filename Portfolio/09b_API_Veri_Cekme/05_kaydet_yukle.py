# ============================================================
# DOSYA 5 — Veriyi Kaydetme ve Tekrar Yükleme
# ============================================================
#
# Her çalıştırmada API'ye istek atmak:
#   - Zaman kaybettirir
#   - Rate limit (istek sınırı) sorununa yol açabilir
#   - İnternet olmadan çalışmanı engeller
#
# Çözüm: Veriyi ilk çekişte kaydet, sonra diskten oku.
# ============================================================

import yfinance as yf
import pandas as pd
import os
import json
from datetime import date

# Kaydedilecek dosyaların klasörü (bu scriptin bulunduğu yer)
KLASOR = os.path.dirname(os.path.abspath(__file__))

# ─────────────────────────────────────────────
# BÖLÜM A — CSV kaydetme ve yükleme
# ─────────────────────────────────────────────

print("=" * 55)
print("A) CSV Kaydetme ve Yükleme")
print("=" * 55)

CSV_YOLU = os.path.join(KLASOR, "aapl_1y.csv")

if not os.path.exists(CSV_YOLU):
    print("  Veri yok, API'den çekiliyor...")
    df = yf.Ticker("AAPL").history(period="1y", interval="1d")
    # Saat dilimini kaldır (CSV kaydetmede sorun çıkmasın)
    df.index = df.index.tz_localize(None)
    df.to_csv(CSV_YOLU)
    print(f"  Kaydedildi: {CSV_YOLU}")
else:
    print(f"  Zaten var, diskten yükleniyor: {CSV_YOLU}")

# Yükle
df_yuklu = pd.read_csv(CSV_YOLU, index_col=0, parse_dates=True)
print(f"  Yüklenen veri: {len(df_yuklu)} satır, {df_yuklu.shape[1]} sütun")
print(f"  Kolonlar: {list(df_yuklu.columns)}")
print(df_yuklu[["Open", "Close", "Volume"]].tail(3).round(2))

# ─────────────────────────────────────────────
# BÖLÜM B — Akıllı güncelleme (tarih kontrolü)
# ─────────────────────────────────────────────

print("\n" + "=" * 55)
print("B) Akıllı Güncelleme — Sadece eksik günleri çek")
print("=" * 55)

def veriyi_guncelle(sembol: str, klasor: str) -> pd.DataFrame:
    """
    Dosya varsa diskten yükler, son tarihin üzerindeki
    günleri API'den çekip birleştirir.
    Dosya yoksa tüm 1 yıllık veriyi çeker.
    """
    dosya = os.path.join(klasor, f"{sembol.replace('.', '_')}.csv")

    if os.path.exists(dosya):
        df_mevcut = pd.read_csv(dosya, index_col=0, parse_dates=True)
        son_tarih = df_mevcut.index[-1].date()
        bugun     = date.today()

        if son_tarih >= bugun:
            print(f"  [{sembol}] Veri güncel, API isteği atlanıyor.")
            return df_mevcut

        print(f"  [{sembol}] Son güncelleme: {son_tarih} → yeni günler çekiliyor...")
        df_yeni = yf.Ticker(sembol).history(
            start=str(son_tarih), end=str(bugun), interval="1d"
        )
        df_yeni.index = df_yeni.index.tz_localize(None)

        # Binleştir ve tekrar kaydet
        df_birlestik = pd.concat([df_mevcut, df_yeni]).drop_duplicates()
        df_birlestik.to_csv(dosya)
        print(f"  [{sembol}] +{len(df_yeni)} satır eklendi, toplam: {len(df_birlestik)}")
        return df_birlestik

    else:
        print(f"  [{sembol}] Dosya yok, tüm 1 yıl çekiliyor...")
        df = yf.Ticker(sembol).history(period="1y", interval="1d")
        df.index = df.index.tz_localize(None)
        df.to_csv(dosya)
        print(f"  [{sembol}] Kaydedildi: {len(df)} satır")
        return df


df_thy = veriyi_guncelle("THYAO.IS", KLASOR)
print(f"\n  THYAO.IS son satır: {df_thy['Close'].iloc[-1]:.2f} TRY")

# ─────────────────────────────────────────────
# BÖLÜM C — JSON kaydetme (tek değerler, meta veri)
# ─────────────────────────────────────────────

print("\n" + "=" * 55)
print("C) JSON Kaydetme (meta veri, ayarlar)")
print("=" * 55)

META_YOLU = os.path.join(KLASOR, "meta.json")

# Kaydet
meta = {
    "son_cekme"  : str(date.today()),
    "hisseler"   : ["THYAO.IS", "ASELS.IS"],
    "period"     : "1y",
    "interval"   : "1d",
    "aciklama"   : "Borsa analizi projesi için çekilen ham veri"
}
with open(META_YOLU, "w", encoding="utf-8") as f:
    json.dump(meta, f, ensure_ascii=False, indent=2)
print(f"  meta.json kaydedildi: {META_YOLU}")

# Yükle
with open(META_YOLU, "r", encoding="utf-8") as f:
    yuklenen_meta = json.load(f)
print(f"  Son çekme tarihi: {yuklenen_meta['son_cekme']}")
print(f"  İzlenen hisseler: {yuklenen_meta['hisseler']}")

# ─────────────────────────────────────────────
# ÖZET
# ─────────────────────────────────────────────
print("\n🎯 ÖĞRENDİKLERİN:")
print("  df.to_csv('dosya.csv')           → kaydet")
print("  pd.read_csv('dosya.csv',          ")
print("    index_col=0, parse_dates=True)  → yükle")
print("  os.path.exists(yol)              → dosya var mı?")
print("  json.dump / json.load            → meta veri")
print("  Akıllı güncelleme                → sadece eksik günleri çek")
print("\n✅ Tüm eğitim tamamlandı!")
print("   Artık 10_Borsa_Analizi projesine geçebilirsin.")
