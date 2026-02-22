# STREAMLIT NEDİR?
# ==============================================================================
# Streamlit, Python kodlarını SIFIR HTML/CSS bilgisiyle
# profesyonel web sitelerine dönüştüren bir kütüphanedir.
# Kod kaydedildiği an web sitesi güncellenir.

import streamlit as st

# 1. BAŞLIK VE YAZI
# ------------------------------------------------------------------------------
st.title("Merhaba! Bu Benim İlk Streamlit Sitem 👋")
st.write("Python yazıyorum, ama çıktısı Web Sitesi oluyor. Çok garip değil mi?")

st.header("1. Temel Bileşenler")
st.subheader("Burası bir alt başlık")
st.text("Bu da düz yazı (Text).")

# Markdown desteği de var (Kalın, İtalik, Liste vb.)
st.markdown("**Kalın yazı** ve _italik yazı_ yazabilirim.")

# 2. ETKİLEŞİM (BUTONLAR)
# ------------------------------------------------------------------------------
st.header("2. Kullanıcı ile Etkileşim")

# Bir butona basılıp basılmadığını if ile kontrol ederiz
if st.button("Bana Tıkla"):
    st.success("Tebrikler! Butona bastın. 🎉")
else:
    st.info("Henüz butona basmadın.")

# 3. VERİ GİRİŞİ (SLIDER, INPUT)
# ------------------------------------------------------------------------------
st.header("3. Veri Girişi")

# Kullanıcıdan ismini alalım
isim = st.text_input("Adın nedir?", placeholder="Örn: Oğuz")

if isim:
    st.write(f"Memnun oldum, **{isim}**!")

# Kaydırma çubuğu (Slider)
yas = st.slider("Kaç yaşındasın?", min_value=0, max_value=100, value=25)
st.write(f"Seçilen yaş: {yas}")

# 4. MEDYA (RESİM, VİDEO vb.)
# ------------------------------------------------------------------------------
st.header("4. Medya Gösterimi")
# İnternetten rastgele bir kedi resmi gösterelim
st.image("https://placekitten.com/400/200", caption="Rastgele Bir Kedi")

# SİDEBAR (YAN MENÜ)
# ------------------------------------------------------------------------------
st.sidebar.title("Yan Menü")
st.sidebar.write("Buraya ayarlar konulur.")
secim = st.sidebar.selectbox("Favori Rengin?", ["Mavi", "Kırmızı", "Yeşil"])
st.sidebar.write(f"Seçimin: {secim}")
