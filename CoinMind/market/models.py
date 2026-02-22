"""
market/models.py - Veri Modelleri (Kiler) 📦

Sanal Kripto Paralarımızı koyacağımız rafları burada tasarlıyoruz.
"""

from django.db import models

# Class (Sınıf) = Veritabanında bir "Tablo" demektir.
# MarketData adında bir tablomuz olacak.
class MarketData(models.Model):
    
    # 1. Sütun: Sembol (İsim)
    # CharField: "Karakter Alanı" demektir. Kısa yazılar için kullanılır.
    # max_length=20: En fazla 20 harf olabilir (Örn: "BTC/USDT" sığar).
    symbol = models.CharField(max_length=20, verbose_name="Kripto Sembolü")

    # 2. Sütun: Fiyat
    # FloatField: "Kesirli Sayı" demektir. Virgüllü sayılar için (Örn: 98000.50).
    price = models.FloatField(verbose_name="Güncel Fiyat")

    # 3. Sütun: Hacim
    # default=0: Eğer veri gelmezse, otomatik olarak 0 yaz.
    volume = models.FloatField(default=0, verbose_name="24 Saatlik Hacim")

    # 4. Sütun: Tarih
    # DateTimeField: Tarih ve Saat tutar.
    # auto_now_add=True: Veri ilk eklendiği anki saati otomatik basar. Senin yazmana gerek kalmaz.
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Kayıt Tarihi")

    # Bu fonksiyon, Admin panelinde satırın nasıl görüneceğini belirler.
    # Bunu yazmazsak "MarketData object (1)" gibi çirkin bir yazı çıkar.
    def __str__(self):
        return f"{self.symbol} - {self.price} $"

    # Tablonun genel ayarları
    class Meta:
        verbose_name = "Piyasa Verisi"        # Tekil İsim
        verbose_name_plural = "Piyasa Verileri" # Çoğul İsim
