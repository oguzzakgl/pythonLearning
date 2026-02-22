import matplotlib.pyplot as plt
import numpy as np

# Veri Hazırlığı
gunler = ["Pzt", "Sal", "Çar", "Per", "Cum", "Cmt", "Paz"]
sicaklik = [20, 22, 25, 24, 19, 23, 26]
yagis = [10, 0, 0, 5, 40, 0, 0]

# 1. Çizgi Grafiği (Line Plot)
plt.figure(figsize=(8, 4)) # Boyut: 8x4
plt.plot(gunler, sicaklik, marker='o', color='red', linestyle='--')
plt.title("Haftalık Sıcaklık Değişimi (Matplotlib)")
plt.xlabel("Günler")
plt.ylabel("Sıcaklık (°C)")
plt.grid(True)
plt.show() # Grafiği Ekrana Bas

# 2. Sütun Grafiği (Bar Plot)
plt.figure(figsize=(8, 4))
plt.bar(gunler, yagis, color='blue')
plt.title("Haftalık Yağış Miktarı (Bar Chart)")
plt.ylabel("Yağış (mm)")
plt.show()

# 3. İki Grafiği Aynı Anda Gösterme (Subplot)
# (1 satır, 2 sütunlu bir alan aç)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

ax1.plot(gunler, sicaklik, 'r')
ax1.set_title("Sıcaklık")

ax2.bar(gunler, yagis, color='b')
ax2.set_title("Yağış")

plt.show()
