"""
market/apps.py - Uygulama Ayarları ⚙️

Burası 'market' uygulamasının kimliğidir.
"""

from django.apps import AppConfig


class MarketConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'market'
    verbose_name = "Kripto Piyasa Modülü" # Admin panelinde görünen isim
