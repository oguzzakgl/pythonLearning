# Konu: Statistics Modülü
# Amaç: İstatistiksel hesaplamalar (ortalama, medyan, mod, standart sapma vb.).

import statistics

data = [10, 20, 30, 40, 50]
data1 = ["apple", "banana", "cherry", "date", "apple", "banana", "apple"]

print(statistics.mean(data))        # Aritmetik ortalama,
print(statistics.harmonic_mean(data))  # Harmonik ortalama
print(statistics.geometric_mean(data)) # Geometrik ortalama
print(statistics.median(data))      # Medyan
print(statistics.mode(data))        # Mod
print(statistics.mode(data1))        # Mod
print(statistics.multimode(data1))  # Çoklu mod
print(statistics.stdev(data))      # Standart sapma
print(statistics.variance(data))    # Varyans
print(statistics.pvariance(data))   # Popülasyon varyansı
print(statistics.quantiles(data, n=4))  # Çeyreklik değerler
print(statistics.median_low(data))  # Düşük medyan
print(statistics.median_high(data)) # Yüksek medyan
print(statistics.fmean(data))       # Float ortalama