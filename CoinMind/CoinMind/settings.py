"""
CoinMind Projesi için Django Ayarları.

Bu dosya, projenin kalbidir. Veritabanı, dil, saat ve yüklü uygulamalar buradan yönetilir.
"""

from pathlib import Path
import os

# Proje ana klasörünü buluyoruz
BASE_DIR = Path(__file__).resolve().parent.parent

# GÜVENLİK ANAHTARI (Gizli tutulmalı!)
SECRET_KEY = 'django-insecure-k=^!change_me_in_production!^=k'

# Geliştirme modu (Hataları görmek için True)
DEBUG = True

ALLOWED_HOSTS = []

# --- YÜKLÜ UYGULAMALAR (APPS) ---
INSTALLED_APPS = [
    'django.contrib.admin',       # Yönetim Paneli
    'django.contrib.auth',        # Kullanıcı Sistemi
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Bizim Oluşturduğumuz Uygulamalar:
    'core',   # Ana sayfa ve temel işlemler
    'market', # Kripto verileri ve borsa işlemleri
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'CoinMind.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [], 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'CoinMind.wsgi.application'

# --- VERİTABANI AYARLARI (PostgreSQL) ---
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'coinmind',      # Veritabanı Adı
        'USER': 'postgres',      # Kullanıcı Adı
        'PASSWORD': '',          # Şifre (Yerel kurulumda boş bırakılabilir)
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Şifre Kuralları
AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

# --- DİL ve SAAT AYARLARI ---
LANGUAGE_CODE = 'tr-tr'             # Türkçe
TIME_ZONE = 'Europe/Istanbul'       # İstanbul Saati
USE_I18N = True
USE_TZ = True

# Statik Dosyalar (CSS, Logo vb.)
STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
