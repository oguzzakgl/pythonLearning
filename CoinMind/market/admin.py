"""
market/admin.py - Yönetim Paneli 🛠️

Kripto verilerini (MarketData) admin panelinden görüp yönetmek için
burada kaydediyoruz.
"""

from django.contrib import admin
from .models import MarketData

# Modelimizi Admin Paneline Kayıt Ediyoruz
@admin.register(MarketData)
class MarketDataAdmin(admin.ModelAdmin):
    # Listede hangi sütunlar görünsün?
    list_display = ('symbol', 'price', 'timestamp')
    
    # Hangi sütunlarda arama yapılabilsin?
    search_fields = ('symbol',)
    
    # Hangi sütunlara göre filtreleme yapılabilsin?
    list_filter = ('timestamp',)
