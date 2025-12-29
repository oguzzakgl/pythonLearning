# 🛒 E-Ticaret Veritabanı ve SQL Analizi

Bu proje, **SQLite** ve **Python** kullanarak ilişkisel bir e-ticaret veritabanı tasarlar, örnek verilerle doldurur ve SQL sorguları ile kritik iş raporları oluşturur.

## 📂 Proje Yapısı

- **`schema.sql`**: Veritabanı şemasını (tablolar, ilişkiler, veri tipleri) tanımlayan SQL dosyası.
- **`setup_db.py`**: Veritabanını (`ecommerce.db`) sıfırdan kurar ve `seed.sql` dosyasındaki örnek verileri yükler.
- **`queries.py`**: Python (Pandas) içinde SQL sorguları çalıştırarak stok ve satış analizleri yapar.
- **`seed.sql`**: Test için gerekli örnek verileri (Kullanıcılar, Ürünler, Siparişler) içerir.

## 🚀 Kurulum

1.  Gerekli kütüphaneleri yükleyin:
    ```bash
    pip install pandas numpy
    ```

2.  Veritabanını kurun:
    ```bash
    python setup_db.py
    ```
    *Bu işlem `ecommerce.db` dosyasını oluşturacaktır.*

3.  Analiz raporlarını çalıştırın:
    ```bash
    python queries.py
    ```

## 📊 Örnek Raporlar

Proje şu analizleri otomatik olarak sunar:
- **Kritik Stok Raporu**: Stoğu 20 adedin altına düşen ürünleri listeler.
- **En Çok Ciro Yapan Ürünler**: Satış adedi ve birim fiyat üzerinden toplam geliri hesaplar.
- **Sipariş Detayları**: Hangi kullanıcının ne zaman, ne kadar alışveriş yaptığını gösterir.
