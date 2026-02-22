"""
core/apps.py - Uygulama Ayarları ⚙️

Burası 'core' uygulamasının kimlik kartıdır.
Adı nedir, varsayılan ayarları nelerdir burada yazar.
Genelde burayı pek değiştirmeyiz.
"""

from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    verbose_name = "Çekirdek (Genel) Modülü" # Admin panelinde görünen isim
