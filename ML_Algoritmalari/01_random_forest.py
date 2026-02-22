import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV

# ==========================================
# DERS 1: RANDOM FOREST NEDİR? 🌲🌲🌲
# ==========================================
# Linear Regression (Düz Çizgi): Veriye dümdüz bir çizgi çeker. 
# "Metrekare artarsa fiyat da hep aynı oranda artar" diye düşünür.
#
# Random Forest (Rastgele Orman): Veriyi "Karar Ağaçları"na böler.
# "Metrekare 100'den büyükse şuna bak, küçükse buna bak" gibi SORGULAR yapar.
# ==========================================

# 1. VERİ HAZIRLIĞI (Basit Emlak Örneği)
# ------------------------------------------
# X: Evin metrekaresi (m2)
X = np.array([[50], [60], [80], [100], [120], [150], [200], [250], [300], [400]])

# y: Evin fiyatı (Bin TL)
# Dikkat: Fiyatlar dümdüz artmıyor! 
# 200 m2'den sonra lüks olduğu için fiyat aniden fırlıyor (Linear bunu yakalayamaz).
y = np.array([150, 180, 220, 300, 350, 450, 800, 900, 1100, 1500])

# 2. MODEL EĞİTİMİ (Yarıştırma)
# ------------------------------------------

# A) Linear Regression (Eski Dostumuz)
lin_model = LinearRegression()
lin_model.fit(X, y)

# B) Random Forest (Grid Search ile En İyisini Bulma)
# ---------------------------------------------------
# Bilgisayara "Şunları dene, hangisi iyiyse onu seç" diyoruz.
param_grid = {
    'n_estimators': [10, 50, 100],  # 10 ağaç mı, 50 mi, 100 mü?
    'random_state': [42]            # Her seferinde aynı sonucu versin
}

# cv=2 -> Veriyi 2'ye bölüp çapraz doğrulama yapar (Verimiz az olduğu için 2)
grid_search = GridSearchCV(RandomForestRegressor(), param_grid, cv=2)
grid_search.fit(X, y)

print(f"En İyi Ayarlar: {grid_search.best_params_}")
print(f"En İyi Skor: {grid_search.best_score_}")

# En iyi modeli seçiyoruz
rf_model = grid_search.best_estimator_

# 3. TAHMİN VE GÖRSELLEŞTİRME
# ------------------------------------------
# Grafiği çizmek için 50 m2'den 400 m2'ye kadar olan tüm noktaları soruyoruz.
X_test = np.arange(50, 400, 1).reshape(-1, 1)

y_pred_lin = lin_model.predict(X_test)
y_pred_rf = rf_model.predict(X_test)

plt.figure(figsize=(10, 6))

# Gerçek Veriler (Noktalar)
plt.scatter(X, y, color='red', label='Gerçek Fiyatlar', s=100)

# Linear Tahmini (Mavi Çizgi)
plt.plot(X_test, y_pred_lin, color='blue', linewidth=2, label='Linear Regression (Düz Mantık)')

# Random Forest Tahmini (Yeşil Çizgi)
# Dikkat: Çizgi dümdüz değil, merdiven gibi! 
# Çünkü ağaçlar "Eğer m2 şu aralıktaysa fiyat budur" diye karar verir.
plt.plot(X_test, y_pred_rf, color='green', linewidth=2, label='Random Forest (Karar Ağaçları)')

plt.title("Linear Regression vs Random Forest Farkı", fontsize=16)
plt.xlabel("Evin Büyüklüğü (m2)")
plt.ylabel("Fiyat (Bin TL)")
plt.legend()
plt.grid(True)
plt.show()

# ==========================================
# SONUÇ YORUMU:
# Linear Regression (Mavi): Veriyi ortalamaya çalışır, ani fiyat sıçramalarını kaçırır.
# Random Forest (Yeşil): Verinin içindeki "Kırılma Noktalarını" (Pattern) yakalar.
# ==========================================
