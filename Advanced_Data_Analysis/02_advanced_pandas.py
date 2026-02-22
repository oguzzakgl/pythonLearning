import pandas as pd
import numpy as np

# ==========================================
# İLERİ SEVİYE PANDAS (ADVANCED PANDAS)
# ==========================================
print("--- İLERİ SEVİYE PANDAS DERSLERİ ---\n")

# Veri Seti Oluşturma
data = {
    'Department': ['HR', 'IT', 'IT', 'HR', 'Finance', 'Finance', 'IT'],
    'Employee': ['Ali', 'Ayşe', 'Mehmet', 'Fatma', 'Ahmet', 'Zeynep', 'Can'],
    'Salary': [5000, 7000, 7200, 5200, 8000, 8500, 6800],
    'Years': [2, 5, 6, 3, 7, 8, 4]
}
df = pd.DataFrame(data)
print("Çalışan Veri Seti:")
print(df)
print("-" * 30)

# 1. Advanced GroupBy ve Aggregation
print("1. GroupBy ve Çoklu Aggregation:")
# Her departman için min, max ve ortalama maaşı hesapla
agg_df = df.groupby('Department').agg({
    'Salary': ['min', 'max', 'mean'],
    'Years': 'mean'
})
print(agg_df)
print("-" * 30)

# 2. Pivot Table (Özet Tablo)
print("2. Pivot Table:")
# Excel'deki pivot tablo mantığı
pivot = df.pivot_table(values='Salary', index='Department', columns='Years', aggfunc='mean')
print("Maaşların Departman ve Yıla göre pivot tablosu:")
print(pivot)
print("-" * 30)

# 3. Merge ve Join İşlemleri
print("3. Merge (Birleştirme):")
df_city = pd.DataFrame({
    'Department': ['HR', 'IT', 'Finance', 'Marketing'],
    'City': ['Istanbul', 'Ankara', 'Izmir', 'Bursa']
})

# Sol birleştirme (Left Join) - Ana tabloyu korur, eşleşeni getirir
merged_df = pd.merge(df, df_city, on='Department', how='left')
print("Departman Lokasyonları ile Birleştirme:")
print(merged_df)
print("-" * 30)

# 4. Apply ve Lambda Fonksiyonları
print("4. Apply ve Custom Fonksiyonlar:")

def salary_category(salary):
    if salary > 7500:
        return 'High'
    elif salary > 6000:
        return 'Medium'
    else:
        return 'Low'

df['Category'] = df['Salary'].apply(salary_category)
print("Maaş Kategorisi Eklenmiş Tablo:")
print(df)
print("-" * 30)

# 5. Window Functions (Pencere Fonksiyonları)
print("5. Rolling Window (Hareketli Ortalama):")
# Basit bir zaman serisi verisi
dates = pd.date_range('20230101', periods=6)
ts = pd.DataFrame(np.random.randn(6), index=dates, columns=['Value'])
# 2 günlük hareketli ortalama
ts['Rolling_Mean'] = ts['Value'].rolling(window=2).mean()
print(ts)
