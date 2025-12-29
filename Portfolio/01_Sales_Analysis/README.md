# 📊 Mağaza Satış Analizi (Sales Analysis Project)

Bu proje, Python'un **NumPy** ve **Pandas** kütüphanelerini kullanarak sanal bir mağazanın satış verilerini üretir, analiz eder ve raporlar.

## 📂 Dosyalar

- **`data_generator.py`**: NumPy kullanarak rastgele ancak anlamlı 1000 satırlık satış verisi (`satislar.csv`) üretir.
- **`analysis_report.py`**: Pandas kullanarak bu veriyi işler ve aşağıdaki raporları sunar:
    - Toplam Ciro ve Ortalama Sepet Tutarı
    - Şehirlere Göre Performans
    - En Çok Satan Ürünler (Adet ve Ciro Bazlı)
    - Günlük Satış Trendleri

## 🚀 Kurulum ve Çalıştırma

1.  Gerekli kütüphaneleri kurun:
    ```bash
    pip install pandas numpy
    ```

2.  Önce veri üretici scripti çalıştırın:
    ```bash
    python data_generator.py
    ```

3.  Raporu görmek için analiz scriptini çalıştırın:
    ```bash
    python analysis_report.py
    ```

## 📈 Örnek Çıktı

```text
--- CİRO RAPORU ---
💰 Toplam Ciro: 26,688,150.00 TL
🏆 Şampiyon Şehir: Ankara
📦 En Çok Satan: Laptop (653 Adet)
```

