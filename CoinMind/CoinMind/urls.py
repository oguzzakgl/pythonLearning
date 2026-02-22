"""
CoinMind Projesi Adres Yönlendirmeleri (URL Configuration)

Burası sitenin "Adres Defteri" veya "Menüsü" gibidir.
Kullanıcı tarayıcıya bir adres yazdığında (örn: coinmind.com/giris),
Django buraya bakar ve hangi sayfayı (View) göstereceğine karar verir.

Örnekler:
1. Fonksiyonlu Görünüm:
    path('anasayfa/', views.home, name='home')
2. Class Tabanlı Görünüm:
    path('', Home.as_view(), name='home')
3. Başka bir URL dosyasını dahil etme (Include):
    path('market/', include('market.urls'))
"""
from django.contrib import admin
from django.urls import path

# Burası adreslerin listesidir:
urlpatterns = [
    # 'admin/' adresine gidilince Yönetim Panelini aç
    path('admin/', admin.site.urls),
]
