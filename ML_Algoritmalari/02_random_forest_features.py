import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

# ==========================================
# DERS 2: RANDOM FOREST - HANGİ ÖZELLİK DAHA ÖNEMLİ? 🌲🕵️‍♂️
# ==========================================
# Random Forest sadece tahmin yapmaz, aynı zamanda hangi özelliğin (feature)
# sonuca ne kadar etkisi olduğunu da söyler. Buna "Feature Importance" denir.
# Emlakçılar için altın değerinde bir bilgidir!
# ==========================================

# 1. VERİ HAZIRLIĞI (Daha Gerçekçi Emlak Verisi)
# ------------------------------------------
# Bu sefer sadece m2 değil, oda sayısı ve bina yaşını da ekliyoruz.

data = {
    'Metrekare': [80, 100, 120, 150, 200, 85, 110, 140, 180, 250],
    'Oda_Sayisi': [2, 3, 3, 4, 5, 2, 3, 4, 4, 6],
    'Bina_Yasi': [10, 5, 0, 15, 2, 30, 20, 10, 5, 1],
    'Fiyat': [2000, 3000, 3500, 4000, 6000, 1800, 2800, 3800, 5000, 7500] 
    # Fiyatlar bin TL cinsinden (Örn: 2000 -> 2 Milyon TL)
}

df = pd.DataFrame(data)

print("--- Veri Setinin İlk 5 Satırı ---")
print(df.head())
print("\n")

# Hedef (y) ve Özellikler (X) ayrımı
X = df[['Metrekare', 'Oda_Sayisi', 'Bina_Yasi']]
y = df['Fiyat']

# 2. MODEL EĞİTİMİ
# ------------------------------------------
# random_state=42: Her çalıştırdığımızda aynı sonuçları almak için (Ders notlarında işlemiştik)
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X, y)

# 3. FEATURE IMPORTANCE (Özellik Önem Düzeyleri)
# ------------------------------------------
# Model kurulduktan sonra, hangi özelliğin kararı ne kadar etkilediğini sorabiliriz.

onem_dereceleri = rf_model.feature_importances_
ozellik_isimleri = X.columns

# Daha okunaklı olması için DataFrame yapalım
onem_df = pd.DataFrame({
    'Ozellik': ozellik_isimleri,
    'Onem_Derecesi': onem_dereceleri
}).sort_values(by='Onem_Derecesi', ascending=False) # En önemlisi en üstte olsun

print("--- Özelliklerin Fiyata Etkisi (%) ---")
print(onem_df)

# 4. GÖRSELLEŞTİRME
# ------------------------------------------
plt.figure(figsize=(10, 6))
plt.barh(onem_df['Ozellik'], onem_df['Onem_Derecesi'], color='teal')
plt.xlabel('Önem Derecesi (0-1 Arası)')
plt.title('Hangi Özellik Ev Fiyatını Daha Çok Etkiliyor?')
plt.gca().invert_yaxis() # En önemli özellik en üstte görünsün
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()

# ==========================================
# SONUÇ YORUMU:
# Muhtemelen "Metrekare" en önemli özellik çıkacak.
# Ama "Bina Yaşı"nın da etkisi azımsanmayacak kadar olabilir.
# Random Forest bunu otomatik olarak hesaplar!
# ==========================================
