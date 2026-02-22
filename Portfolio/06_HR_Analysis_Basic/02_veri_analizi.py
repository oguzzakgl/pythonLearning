import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# İK Performans Projesi - Analiz ve Görselleştirme

# 1. Veri Yükleme ve İnceleme
print("--- 1. VERI YUKLEME VE INCELEME ---")

current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, 'ik_performans.csv')

try:
    df = pd.read_csv(csv_path)
    print("Veri basariyla yuklendi.")
except FileNotFoundError:
    print(f"HATA: '{csv_path}' dosyasi bulunamadi. Lutfen once '01_veri_olusturma.py' calistirin.")
    exit()

print(f"\nSatir/Sutun Sayisi: {df.shape}")
print("\n--- Veri Seti Bilgileri ---")
print(df.info())

print("\n--- Temel Istatistikler ---")
print(df.describe().T)

print("\n--- Eksik Deger Kontrolu ---")
eksik_kontrol = df.isnull().sum()
if eksik_kontrol.sum() == 0:
    print("Eksik veri yok.")
else:
    print(eksik_kontrol)

# 2. Departman Bazlı Analiz
print("\n--- 2. DEPARTMAN BAZLI ANALIZ ---")
dept_analiz = df.groupby("Departman")[["Maas", "Performans"]].mean()
print("\nDepartman Bazli Ortalamalar:\n")
print(dept_analiz.round(2))

en_yuksek_maas_dept = dept_analiz["Maas"].idxmax()
en_yuksek_maas_deger = dept_analiz["Maas"].max()
print(f"\nEn Yuksek Maas Ortalamasi: {en_yuksek_maas_dept} ({en_yuksek_maas_deger:.2f} TL)")

dept_nufus = df["Departman"].value_counts()
en_kalabalik_dept = dept_nufus.idxmax()
print(f"En Kalabalik Departman: {en_kalabalik_dept} ({dept_nufus.max()} kisi)")

print("\n--- Departman Nufuslari ---")
print(dept_nufus)

# 3. Görselleştirme: Maaş Dağılımı
print("\n--- 3. GORSELLESTIRME: MAAS DAGILIMI ---")
plt.figure(figsize=(14, 6))

# Histogram
plt.subplot(1, 2, 1)
sns.histplot(df["Maas"], kde=True, color="skyblue")
plt.title("Sirket Genelinde Maas Dagilimi")
plt.xlabel("Maas (TL)")
plt.ylabel("Calisan Sayisi")

# Box Plot
plt.subplot(1, 2, 2)
sns.boxplot(x="Departman", y="Maas", data=df, palette="Set2")
plt.title("Departmanlara Gore Maas Araliklari")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
print("Maas dagilim grafikler cizildi.")

# 4. Görselleştirme: Tecrübe ve Maaş İlişkisi
print("\n--- 4. GORSELLESTIRME: TECRUBE VE MAAS ILISKISI ---")
plt.figure(figsize=(10, 6))

sns.scatterplot(x="Tecrube", y="Maas", data=df, hue="Departman", alpha=0.7)
plt.title("Tecrube Arttikca Maas Nasil Degisiyor?")
plt.xlabel("Tecrube (Yil)")
plt.ylabel("Maas (TL)")
plt.legend(title="Departman")
plt.grid(True, linestyle="--", alpha=0.5)

plt.show()
print("Tecrube-Maas grafigi cizildi.")

# 5. Görselleştirme: Korelasyon Haritası
print("\n--- 5. GORSELLESTIRME: KORELASYON HARITASI ---")
sayisal_veriler = df.select_dtypes(include=['float64', 'int64'])
corr_matrix = sayisal_veriler.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Hangi Ozellikler Birbiriyle Iliskili?")
plt.show()
print("Korelasyon haritasi cizildi.")

# 6. Bonus: Yıldız Çalışanlar
print("\n--- 6. BONUS: YILDIZ CALISANLAR LISTESI ---")

yildizlar = df[
    (df["Departman"] == "IT") & 
    (df["Tecrube"] > 5) & 
    (df["Performans"] > 80)
]

print(f"Toplam {len(yildizlar)} adet yildiz calisan bulundu.")
print("\nIlk 10 Yildiz Calisan:")
print(yildizlar[["Isim", "Maas", "Performans"]].head(10))

yildizlar.to_csv(os.path.join(current_dir, "yildiz_calisanlar.csv"), index=False)
print(f"\nYildiz calisanlar listesi 'yildiz_calisanlar.csv' olarak kaydedildi.")
print("\nProje basariyla tamamlandi.")
