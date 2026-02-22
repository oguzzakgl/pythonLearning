import os
import django

# Django ayarlarını yükle
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CoinMind.settings')
django.setup()

from django.contrib.auth.models import User

# Kullanıcıyı oluştur veya varsa getir
try:
    user, created = User.objects.get_or_create(username='admin', defaults={'email': 'admin@example.com'})
    
    # Şifreyi her durumda 'admin123' olarak ayarla
    user.set_password('admin123')
    user.is_superuser = True
    user.is_staff = True
    user.save()
    
    if created:
        print("✅ Süper kullanıcı (Admin) oluşturuldu!")
    else:
        print("✅ Admin şifresi 'admin123' olarak güncellendi!")
        
    print("Kullanıcı Adı: admin")
    print("Şifre: admin123")
    
except Exception as e:
    print(f"❌ Hata oluştu: {e}")
