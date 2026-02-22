import matplotlib.pyplot as plt
import numpy as np

# ==========================================
# İLERİ SEVİYE MATPLOTLIB
# ==========================================
print("--- İLERİ SEVİYE MATPLOTLIB DERSLERİ ---\n")
print("Grafikler oluşturuluyor... (Pencere açılabilir)")

# Veri Hazırlığı
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.exp(x / 3)

# 1. Subplots (Çoklu Grafikler)
fig, ax = plt.subplots(2, 1, figsize=(8, 6)) # 2 satır, 1 sütun

# 1. Grafik
ax[0].plot(x, y1, 'r-', label='Sinüs')
ax[0].set_title('Sinüs Dalgası')
ax[0].grid(True)
ax[0].legend()

# 2. Grafik
ax[1].plot(x, y2, 'b--', label='Üstel')
ax[1].set_title('Üstel Büyüme')
ax[1].grid(True)
ax[1].legend()

plt.tight_layout() # Grafikler birbirine girmesin diye
plt.savefig('advanced_matplotlib_subplots.png') # Kaydetme
print("1. Subplots grafiği kaydedildi: advanced_matplotlib_subplots.png")
# plt.show() # Not: Kod akışını durdurmaması için yorum satırı yaptım.

# 2. Dual Axis (İkincil Eksen)
fig, ax1 = plt.subplots(figsize=(8, 4))

color = 'tab:red'
ax1.set_xlabel('X ekseni')
ax1.set_ylabel('Sinüs', color=color)
ax1.plot(x, y1, color=color)
ax1.tick_params(axis='y', labelcolor=color)

# İkinci ekseni oluştur (x eksenini paylaşırlar)
ax2 = ax1.twinx()  
color = 'tab:blue'
ax2.set_ylabel('Üstel', color=color)  
ax2.plot(x, y2, color=color)
ax2.tick_params(axis='y', labelcolor=color)

plt.title("Aynı Grafikte İki Farklı Ölçek (Dual Axis)")
plt.savefig('advanced_matplotlib_dual_axis.png')
print("2. Dual Axis grafiği kaydedildi: advanced_matplotlib_dual_axis.png")

# 3. 3D Plotting (3 Boyutlu Çizim)
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Veri
z_line = np.linspace(0, 15, 1000)
x_line = np.sin(z_line)
y_line = np.cos(z_line)

ax.plot3D(x_line, y_line, z_line, 'gray')
ax.scatter3D(x_line, y_line, z_line, c=z_line, cmap='Greens')

ax.set_title("3D Spiral")
plt.savefig('advanced_matplotlib_3d.png')
print("3. 3D grafiği kaydedildi: advanced_matplotlib_3d.png")

print("Tüm grafikler başarıyla oluşturuldu.")
