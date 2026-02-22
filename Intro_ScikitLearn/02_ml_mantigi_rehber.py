# MAKİNE ÖĞRENMESİ (MACHINE LEARNING) NEDİR?
# ==============================================================================
# Bu kod, hiçbir proje senaryosu (maaş, ev fiyatı vb.) olmadan
# Makine Öğrenmesinin "SAF MANTIĞINI" anlatır.

# MANTIK: 
# Bilgisayara "Girdiler" (X) ve "Çıktılar" (y) verilir.
# Bilgisayardan aradaki FORMÜLÜ (kuralı) kendisinin bulması istenir.
# Buna "Eğitim" (Training) denir.

# ÖRNEK SENARYO:
# Bizim aklımızdaki kural: Sayıyı 2 ile çarpıp 5 eklemek. (y = 2x + 5)
# Ama bu kuralı bilgisayara SÖYLEMİYORUZ.
# Ona sadece örnekleri veriyoruz, kuralı o bulacak.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def main():
    # --------------------------------------------------------------------------
    # ADIM 1: VERİ HAZIRLAMA (Örnek Sorular ve Cevaplar)
    # --------------------------------------------------------------------------
    print("1. Veri Hazırlanıyor...")
    
    # X: Girdiler (Sorular) - 2 Boyutlu olmalı [[1], [2], ...]
    X = np.array([[1], [2], [3], [4], [5]])
    
    # y: Çıktılar (Cevaplar) - (Kuralımız 2x + 5 idi)
    # 1 -> 7
    # 2 -> 9
    # 3 -> 11
    # 4 -> 13
    # 5 -> 15
    y = np.array([7, 9, 11, 13, 15]) 
    
    # .flatten() NEDİR?
    # X verisi teknik sebeplerle [[1], [2], ...] diye kutu kutudur (2 Boyutlu).
    # .flatten() komutu bunu sadece ekranda güzel gözüksün diye [1, 2, ...] haline (Normal Liste) getirir.
    # Hesaplamaya bir etkisi yoktur, sadece çıktıyı temizler.
    print(f"   X (Girdiler): {X.flatten()}")
    print(f"   y (Cevaplar): {y}")
    print("-" * 50)

    # --------------------------------------------------------------------------
    # ADIM 2: MODEL SEÇİMİ VE EĞİTİM (Fit)
    # --------------------------------------------------------------------------
    print("2. Model Eğitiliyor (Bilgisayar kuralı arıyor)...")
    
    # LinearRegression: "Aradaki ilişki düz bir çizgi gibidir" diyen model.
    model = LinearRegression()
    
    # fit(X, y): "Bak X bu, y bu. Neyin neyle çarpılıp toplandığını bul." komutu.
    model.fit(X, y)
    
    print("   Eğitim Tamamlandı.")
    
    # Modelin bulduğu formül şu şekildedir: y = (Katsayı * x) + Sabit
    # KATSAYI ve SABİT NEDİR?
    # Matematikte Doğru Denklemi: y = mx + n
    # NEDEN [0] YAZDIK?
    # Çünkü model birden fazla girdiyle de çalışabilir (Örn: Maaş = Deneyim * A + Eğitim * B).
    # Bu yüzden coef_ bize her zaman bir LİSTE verir: [A, B, ...].
    # Bizim sadece 1 girdimiz (Deneyim) olduğu için listenin ilk elemanını [0] ile alıyoruz.
    bulunan_katsayi = model.coef_[0]

    # intercept_ (Intercept/Sabit): Formüldeki 'n' değeri. (Bias olarak da bilinir)
    #   -> "Girdi 0 olursa sonuç kaçtan başlar?" sorusunun cevabı. (Burada 5 olmalı)
    bulunan_sabit = model.intercept_
    
    print(f"   Modelin Bulduğu Kural: y = {bulunan_katsayi:.1f}x + {bulunan_sabit:.1f}")
    print("-" * 50)

    # --------------------------------------------------------------------------
    # ADIM 3: TAHMİN (Predict)
    # --------------------------------------------------------------------------
    print("3. Tahmin Yapılıyor (Test)...")
    
    # predict() NEDİR?
    # Modeli "Sınava sokmak" gibidir.
    # Ona daha önce cevabını söylemediğimiz bir soru sorarız.
    
    # NEDEN ÇİFT PARANTEZ [[10]]?
    # Eğitimde (fit) nasıl X'i [[1], [2]...] diye verdiysek, soruyu da aynı formatta sormalıyız.
    # [[10]] -> "1 tane soru soruyorum, değeri 10" demektir.
    yeni_veri = [[10]]
    
    # model.predict(): Öğrendiği formülde x yerine 10 koyar ve sonucu hesaplar.
    tahmin = model.predict(yeni_veri)
    
    # Bizim kuralımıza göre: 2*10 + 5 = 25 olmalı.
    print(f"   Soru: Girdi 10 olursa çıktı ne olur?")
    print(f"   Modelin Tahmini: {tahmin[0]:.1f}")
    
    if tahmin[0] == 25:
        print("   SONUÇ: Harika! Model kuralı birebir çözmüş.")
    else:
        print("   SONUÇ: Yaklaşmış.")
    
    # --------------------------------------------------------------------------
    # ADIM 4: GÖRSELLEŞTİRME
    # --------------------------------------------------------------------------
    plt.scatter(X, y, color='red', label='Örnek Veriler (Noktalar)')
    plt.plot(X, model.predict(X), color='blue', label='Modelin Bulduğu Kural (Çizgi)')
    plt.scatter(yeni_veri, tahmin, color='green', s=100, label='Tahmin (10 -> ?)')
    plt.legend()
    plt.title(f'Makine Öğrenmesi Mantığı\nGerçek: y = 2x + 5 | Bulunan: y = {bulunan_katsayi:.1f}x + {bulunan_sabit:.1f}')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
