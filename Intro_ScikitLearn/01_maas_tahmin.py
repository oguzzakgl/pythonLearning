# MAKİNE ÖĞRENMESİNE GİRİŞ DERSİ 1: Basit Doğrusal Regresyon
# Konu: Deneyim Yılına Göre Maaş Tahmini
# Amaç: Bilgisayara "tecrübe arttıkça maaş artar" kuralını ezberletmek değil, veriden öğrenmesini sağlamak.

# ADIM 1: Kütüphaneleri Çağırma
# ------------------------------------------------------------------
import pandas as pd  # Veriyi okumak ve tablo (DataFrame) haline getirmek için
import matplotlib.pyplot as plt  # Veriyi çizip gözle görmek için
from sklearn.linear_model import LinearRegression  # Yapay Zeka (Makine Öğrenmesi) modeli

# ADIM 2: Veriyi Hazırlama (Data Preparation)
# ------------------------------------------------------------------
# Bilgisayara ders çalışması için örnek sorular ve cevaplar veriyoruz.
# Soru (X): Deneyim Yılı
# Cevap (y): Maaş

data = {
    'Deneyim': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],   # X (Girdiler)
    'Maas': [30000, 35000, 42000, 48000, 55000, 62000, 68000, 75000, 81000, 90000] # y (Çıktılar)
}
df = pd.DataFrame(data)

# Bilgisayarın anlayacağı formata çeviriyoruz
X = df[['Deneyim']]  # Girdiler her zaman iki boyutlu tablo olmalı (Liste içinde liste gibi)
y = df['Maas']       # Çıktılar tek bir liste olabilir

print("--- VERİ SETİ ---")
print(df)
print("-" * 30)

# ADIM 3: Modeli Seçme ve Eğitme (Training)
# ------------------------------------------------------------------
# LinearRegression: Verilerin arasından en uygun düz çizgiyi çizen algoritmadır.
model = LinearRegression()

# .fit() komutu ile "Bu X değerlerine karşılık bu y değerleri gelmiş, aradaki bağlantıyı öğren" diyoruz.
model.fit(X, y)

print("Eğitim Tamamlandı! Bilgisayar artık deneyim ve maaş arasındaki ilişkiyi öğrendi.")
print("-" * 30)

# ADIM 4: Tahmin Yaptırma (Prediction)
# ------------------------------------------------------------------
# Artık görmediği bir soruyu sorabiliriz.
# Soru: "15 yıllık deneyimi olan biri ne kadar almalı?"

yeni_deneyim = [[15]]  # Çift parantez unutma (2 boyutlu olmalı)
tahmin = model.predict(yeni_deneyim)

print(f"SORU: 15 Yıllık deneyimim var, maaşım ne olur?")
print(f"YAPAY ZEKA CEVABI: {tahmin[0]:.2f} TL olmalı.")
print("-" * 30)

# ADIM 5: Görselleştirme (Ne Öğrendiğini Görelim)
# ------------------------------------------------------------------
plt.scatter(X, y, color='red', label='Gerçek Maaşlar')  # Gerçek verileri nokta olarak koy
plt.plot(X, model.predict(X), color='blue', label='Yapay Zekanın Tahmini') # Modelin kurduğu mantığı çizgi olarak çiz
plt.title('Deneyim vs Maaş Grafiği')
plt.xlabel('Deneyim (Yıl)')
plt.ylabel('Maaş (TL)')
plt.legend()
plt.show()
