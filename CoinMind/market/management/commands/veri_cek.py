"""
Bu dosya bir "Django Komutu"dur.
Terminalden 'python manage.py veri_cek' yazdığında burası çalışır.

Görevi:
1. Binance borsasına bağlan.
2. Bitcoin (BTC) ve Ethereum (ETH) fiyatlarını çek.
3. Veritabanındaki 'MarketData' tablosuna kaydet.
"""

from django.core.management.base import BaseCommand
from market.models import MarketData
import ccxt
from datetime import datetime

class Command(BaseCommand):
    help = 'Binance borsasından güncel kripto verilerini (BTC, ETH) çeker ve kaydeder.'

    def handle(self, *args, **options):
        self.stdout.write("🌍 Binance borsasına bağlanılıyor...")
        
        # 1. Binance Bağlantısı (Bilgi çekmek için şifreye gerek yok)
        exchange = ccxt.binance()
        
        # Çekmek istediğimiz coinler
        symbols = ['BTC/USDT', 'ETH/USDT', 'SOL/USDT', 'AVAX/USDT']

        for symbol in symbols:
            try:
                # 2. Fiyatı Çek
                ticker = exchange.fetch_ticker(symbol)
                price = ticker['last']           # Son Fiyat
                volume = ticker['quoteVolume']   # 24s Hacim (USDT cinsinden)
                change = ticker['percentage']    # Günlük değişim yüzdesi

                # 3. Veritabanına Kaydet
                MarketData.objects.create(
                    symbol=symbol,
                    price=price,
                    volume=volume,
                    change_24h=change
                )
                
                self.stdout.write(self.style.SUCCESS(f"✅ {symbol} kaydedildi: {price} $"))

            except Exception as e:
                self.stdout.write(self.style.ERROR(f"❌ Hata ({symbol}): {e}"))
        
        self.stdout.write(self.style.SUCCESS("🎉 İşlem tamamlandı! Admin panelini kontrol et."))
