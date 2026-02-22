import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# ==========================================
# İLERİ SEVİYE SEABORN
# ==========================================
print("--- İLERİ SEVİYE SEABORN DERSLERİ ---\n")
print("Grafikler oluşturuluyor... (Pencere açılabilir)")

# Örnek Veri Seti (Iris veya Tips çok kullanılır ama biz rastgele üretelim)
# Not: Seaborn içinde hazır veri setleri vardır ama internet gerekebilir.
# Biz garanti olsun diye kendimiz üretelim.
np.random.seed(42)
df = pd.DataFrame({
    'Math': np.random.normal(60, 15, 100),
    'Physics': np.random.normal(55, 10, 100) + np.random.normal(0, 5, 100), # Math ile ilişkili
    'Literature': np.random.normal(75, 10, 100),
    'Gender': np.random.choice(['Male', 'Female'], 100)
})

# 1. Pairplot (İkili İlişkiler Matrisi)
# Veri setindeki tüm sayısal değişkenlerin birbirleriyle olan ilişkisini gösterir.
print("1. Pairplot oluşturuluyor...")
sns.pairplot(df, hue='Gender', palette='husl')
plt.savefig('advanced_seaborn_pairplot.png')
print("Kaydedildi: advanced_seaborn_pairplot.png")

# 2. Heatmap (Isı Haritası - Korelasyon Matrisi)
print("2. Heatmap oluşturuluyor...")
plt.figure(figsize=(8, 6))
# Sadece sayısal sütunların korelasyonu
corr = df.select_dtypes(include=[np.number]).corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title("Ders Notları Korelasyon Matrisi")
plt.savefig('advanced_seaborn_heatmap.png')
print("Kaydedildi: advanced_seaborn_heatmap.png")

# 3. Violin Plot vs Box Plot
# Box plot medyan ve çeyrekleri gösterirken, Violin plot dağılımı da gösterir.
print("3. Violin Plot oluşturuluyor...")
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
sns.boxplot(x='Gender', y='Math', data=df)
plt.title('Box Plot (Matematik)')

plt.subplot(1, 2, 2)
sns.violinplot(x='Gender', y='Math', data=df)
plt.title('Violin Plot (Matematik)')

plt.tight_layout()
plt.savefig('advanced_seaborn_violin.png')
print("Kaydedildi: advanced_seaborn_violin.png")

print("Tüm Seaborn grafikleri hazır.")
