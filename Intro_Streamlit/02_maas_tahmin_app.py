import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# SAYFA AYARLARI
st.set_page_config(page_title="Maaş Tahmin Sistemi", page_icon="💰")

# 1. BAŞLIK VE AÇIKLAMA
st.title("💰 Yapay Zeka Maaş Tahmin Sistemi")
st.write("""
Bu uygulama, **Makine Öğrenmesi (Linear Regression)** kullanarak deneyim yılınıza göre
tahmini maaşınızı hesaplar.
""")

# 2. MODEL EĞİTİMİ (Arka Planda)
# ------------------------------------------------------------------------------
# Gerçek hayatta bu kısım genelde "modeli yükle" şeklinde olur ama 
# eğitim amaçlı olduğu için anlık eğitiyoruz.
data = {
    'Deneyim': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Maas': [30000, 35000, 42000, 48000, 55000, 62000, 68000, 75000, 81000, 90000]
}
df = pd.DataFrame(data)

X = df[['Deneyim']]
y = df['Maas']

model = LinearRegression()
model.fit(X, y)

# Sidebar'a Bilgi Ekleme
st.sidebar.header("Model Bilgileri")
st.sidebar.text(f"Eğitim Verisi Sayısı: {len(df)}")
st.sidebar.text(f"Model: Linear Regression")
st.sidebar.markdown("---")
st.sidebar.write("Geliştirici: **Oğuz**")

# 3. KULLANICI GİRİŞİ (Input)
# ------------------------------------------------------------------------------
st.subheader("Deneyiminizi Girin")
deneyim = st.slider("Kaç yıllık tecrübeniz var?", min_value=0, max_value=30, value=5)

# 4. TAHMİN (Prediction)
# ------------------------------------------------------------------------------
tahmin = model.predict([[deneyim]])
tahmin_sonuc = tahmin[0]

# Sonucu Göster (Büyük ve Renkli)
st.markdown("---")
st.metric(label="Tahmini Maaşınız", value=f"{tahmin_sonuc:,.2f} TL")

# 5. GRAFİK GÖSTERİMİ
# ------------------------------------------------------------------------------
st.subheader("Grafik Üzerinde Konumunuz")

fig, ax = plt.subplots(figsize=(10, 5))

# Gerçek veriler (Mavi Noktalar)
ax.scatter(X, y, color='blue', label='Gerçek Veriler')

# Modelin Doğrusu (Kırmızı Çizgi)
ax.plot(X, model.predict(X), color='red', label='Trend Çizgisi')

# Kullanıcının Tahmini (Yeşil Büyük Nokta)
ax.scatter([[deneyim]], [tahmin_sonuc], color='green', s=200, label='Sizin Konumunuz', zorder=5)

ax.set_xlabel("Deneyim (Yıl)")
ax.set_ylabel("Maaş (TL)")
ax.legend()
ax.grid(True)

# Grafiği Streamlit'e bas
st.pyplot(fig)
