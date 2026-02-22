# ============================================================
# Plotly — İnteraktif Grafik Kütüphanesi
# ============================================================
#
# Plotly neden kullanılır?
#   • Tarayıcıda açılan, zoom/hover destekli interaktif grafikler
#   • Candlestick (mum grafiği) → borsa analizinin olmazsa olmazı
#   • Streamlit ve Dash ile mükemmel uyum
#
# Matplotlib vs Plotly:
#   Matplotlib → statik PNG/SVG    (rapor, PDF için)
#   Plotly     → interaktif HTML   (dashboard, web için)
#
# Kurulum:
#   pip install plotly pandas
# ============================================================

import plotly.express as px           # Hızlı ve kolay grafikler
import plotly.graph_objects as go     # Detaylı, özelleştirilebilir grafikler
import pandas as pd
import numpy as np

# ─────────────────────────────────────────────
# BÖLÜM A — plotly.express (px)
# En hızlı yol: tek satırda grafik
# ─────────────────────────────────────────────

print("=" * 55)
print("A) plotly.express — hızlı grafikler")
print("=" * 55)

# Örnek veri üret
np.random.seed(42)
tarihler = pd.date_range("2024-01-01", periods=60, freq="D")
fiyatlar = 100 + np.cumsum(np.random.randn(60) * 2)  # rastgele yürüyüş
df = pd.DataFrame({"Tarih": tarihler, "Fiyat": fiyatlar})

# Çizgi grafik
fig1 = px.line(
    df,
    x="Tarih",
    y="Fiyat",
    title="Örnek Hisse Fiyatı (px.line)",
    labels={"Fiyat": "Fiyat ($)", "Tarih": ""},
    template="plotly_dark"   # dark tema!
)
fig1.show()

# Bar grafik
kategori_df = pd.DataFrame({
    "Hisse" : ["AAPL", "TSLA", "GOOGL", "MSFT", "AMZN"],
    "Getiri": [15.2, -8.3, 22.1, 18.7, 5.4]
})
fig2 = px.bar(
    kategori_df,
    x="Hisse", y="Getiri",
    color="Getiri",                    # değere göre renk
    color_continuous_scale="RdYlGn",  # kırmızı-sarı-yeşil skalası
    title="Yıllık Getiri Karşılaştırması",
    template="plotly_dark"
)
fig2.show()

# Histogram
getiriler = np.random.normal(0, 1.5, 500)
fig3 = px.histogram(
    x=getiriler,
    nbins=40,
    title="Günlük Getiri Dağılımı",
    labels={"x": "Getiri (%)"},
    color_discrete_sequence=["#00CC96"],
    template="plotly_dark"
)
fig3.show()

# ─────────────────────────────────────────────
# BÖLÜM B — plotly.graph_objects (go)
# Daha fazla kontrol: birden fazla katman ekle
# ─────────────────────────────────────────────

print("\n" + "=" * 55)
print("B) plotly.graph_objects — katmanlı grafik")
print("=" * 55)

# Boş figür oluştur, üstüne katman ekle
fig4 = go.Figure()

# Ana çizgi
fig4.add_trace(go.Scatter(
    x=df["Tarih"],
    y=df["Fiyat"],
    mode="lines",
    name="Kapanış Fiyatı",
    line=dict(color="#636EFA", width=2)
))

# Hareketli ortalama (MA20)
ma20 = df["Fiyat"].rolling(20).mean()
fig4.add_trace(go.Scatter(
    x=df["Tarih"],
    y=ma20,
    mode="lines",
    name="MA20",
    line=dict(color="#FFA15A", width=1.5, dash="dot")
))

# Layout özelleştir
fig4.update_layout(
    title="Fiyat + Hareketli Ortalama",
    xaxis_title="Tarih",
    yaxis_title="Fiyat ($)",
    template="plotly_dark",
    hovermode="x unified",        # aynı x'teki tüm değerleri göster
    legend=dict(x=0.01, y=0.99)
)
fig4.show()

# ─────────────────────────────────────────────
# BÖLÜM C — Candlestick (Mum Grafiği) ⭐
# Borsa analizinin olmazsa olmazı!
# ─────────────────────────────────────────────

print("\n" + "=" * 55)
print("C) Candlestick — borsa mum grafiği ⭐")
print("=" * 55)

# OHLC (Open-High-Low-Close) verisi simüle et
np.random.seed(0)
n = 60
acilis  = 100 + np.cumsum(np.random.randn(n))
kapanis = acilis + np.random.randn(n) * 1.5
yuksek  = np.maximum(acilis, kapanis) + np.abs(np.random.randn(n))
dusuk   = np.minimum(acilis, kapanis) - np.abs(np.random.randn(n))

ohlc_df = pd.DataFrame({
    "Tarih"  : pd.date_range("2024-01-01", periods=n),
    "Open"   : acilis,
    "High"   : yuksek,
    "Low"    : dusuk,
    "Close"  : kapanis,
    "Volume" : np.random.randint(1_000_000, 10_000_000, n)
})

fig5 = go.Figure()

# Candlestick katmanı
fig5.add_trace(go.Candlestick(
    x    =ohlc_df["Tarih"],
    open =ohlc_df["Open"],
    high =ohlc_df["High"],
    low  =ohlc_df["Low"],
    close=ohlc_df["Close"],
    name ="Fiyat",
    increasing_line_color="#26A69A",  # yeşil → yükselen mum
    decreasing_line_color="#EF5350"   # kırmızı → düşen mum
))

# MA20 üstüne ekle
fig5.add_trace(go.Scatter(
    x=ohlc_df["Tarih"],
    y=ohlc_df["Close"].rolling(20).mean(),
    name="MA20",
    line=dict(color="#FFA726", width=1.5)
))

fig5.update_layout(
    title="Candlestick + MA20 Grafiği",
    template="plotly_dark",
    xaxis_rangeslider_visible=False,  # alt kaydırma çubuğunu kapat
    height=500
)
fig5.show()

# ─────────────────────────────────────────────
# BÖLÜM D — Subplot (Alt grafikler)
# Birden fazla grafiği aynı pencerede göster
# ─────────────────────────────────────────────

print("\n" + "=" * 55)
print("D) Subplot — fiyat + hacim aynı pencerede")
print("=" * 55)

from plotly.subplots import make_subplots

fig6 = make_subplots(
    rows=2, cols=1,
    shared_xaxes=True,        # x eksenini paylaş
    row_heights=[0.7, 0.3],   # üst %70, alt %30
    vertical_spacing=0.03
)

# Üst grafik: Candlestick
fig6.add_trace(go.Candlestick(
    x=ohlc_df["Tarih"],
    open=ohlc_df["Open"], high=ohlc_df["High"],
    low=ohlc_df["Low"], close=ohlc_df["Close"],
    name="Fiyat"
), row=1, col=1)

# Alt grafik: Hacim barları
renkler = ["#26A69A" if c >= o else "#EF5350"
           for c, o in zip(ohlc_df["Close"], ohlc_df["Open"])]
fig6.add_trace(go.Bar(
    x=ohlc_df["Tarih"],
    y=ohlc_df["Volume"],
    name="Hacim",
    marker_color=renkler
), row=2, col=1)

fig6.update_layout(
    title="Fiyat + Hacim Dashboard",
    template="plotly_dark",
    xaxis_rangeslider_visible=False,
    height=600
)
fig6.show()

# ─────────────────────────────────────────────
# ÖZET
# ─────────────────────────────────────────────
print("\n🎯 ÖĞRENDİKLERİN:")
print("  px.line / px.bar / px.histogram  → hızlı grafikler")
print("  go.Figure() + add_trace()        → katmanlı grafik")
print("  go.Candlestick()                 → mum grafiği ⭐")
print("  go.Scatter()                     → çizgi / nokta katmanı")
print("  make_subplots()                  → alt grafik düzeni")
print("  update_layout(template=...)      → tema ve özelleştirme")
print("\n  Borsa projesinde: veri_analizi.py ve app.py'de kullanacaksın!")
