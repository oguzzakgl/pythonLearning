# 🗺️ CoinMind - Büyük Yol Haritası (Sıfırdan Zirveye)

Bu rehber, boş bir klasörden başlayıp "Wow" dedirtecek bir Kripto Analiz Sitesi yapana kadar atacağımız tüm adımları içerir.

---

## 🏗️ 1. Bölüm: Temel ve İskelet (BİTTİ ✅)
Evi inşa etmeden önce temelini attık.
*   [x] Django Kurulumu (`startproject`)
*   [x] Uygulamaların Açılması: `core` (Genel) ve `market` (Kripto).
*   [x] Ayarların Yapılması: [`settings.py`](file:///C:/Users/Oğuz/Desktop/python-library/CoinMind/CoinMind/settings.py) dosyasına Türkçe ayarlar ve Veritabanı (PostgreSQL) eklendi.

---

## 🧠 2. Bölüm: Veri Yapısı (ŞU AN BURADASIN 📍)
Sitenin hafızasını oluşturuyoruz.
*   [ ] **Veri Modelini Yaz:** [`market/models.py`](file:///C:/Users/Oğuz/Desktop/python-library/CoinMind/market/models.py) dosyasını açıp `MarketData` tablosunu kodla.
    *   *İpucu:* `class MarketData(models.Model):` ile başla. `symbol`, `price` alanlarını ekle.
*   [ ] **Veritabanına İşle:** Yazdığın kodu veritabanına göndermek için terminale şunları yazacaksın:
    1.  `python manage.py makemigrations` (Planı hazırla)
    2.  `python manage.py migrate` (İnşaatı yap)
*   [ ] **Admin'de Göster:** [`market/admin.py`](file:///C:/Users/Oğuz/Desktop/python-library/CoinMind/market/admin.py) dosyasına girip modelini panele kaydet.
    *   *İpucu:* `admin.site.register(MarketData)` kodunu kullan.

---

## 🤖 3. Bölüm: Veri Toplama Botu (Backend)
Sürekli çalışıp veri çeken robotumuzu yazacağız.
*   [ ] **Komut Dosyası Oluştur:** Django'nun içine özel bir komut dosyası açacağız.
    *   *Yer:* `market/management/commands/veri_cek.py` (Yeni oluşturacağız).
*   [ ] **Botu Kodla:** Binance'den fiyat çeken (`ccxt` kullanarak) ve bunu az önce yaptığın `MarketData` tablosuna kaydeden kodu yazacağız.
*   [ ] **Test Et:** Terminalden `python manage.py veri_cek` diyerek çalışıyor mu bakacağız.

---

## 🎨 4. Bölüm: Ön Yüz ve Tasarım (Frontend)
Kullanıcının gördüğü o şık ekranları yapacağız.
*   [ ] **Adresleri Belirle:** [`CoinMind/urls.py`](file:///C:/Users/Oğuz/Desktop/python-library/CoinMind/CoinMind/urls.py) dosyasına gidip `/piyasa` gibi adresleri tanımlayacağız.
*   [ ] **Sayfa Mantığını Kur:** [`market/views.py`](file:///C:/Users/Oğuz/Desktop/python-library/CoinMind/market/views.py) içinde veriyi veritabanından çekip sayfaya gönderen fonksiyonu yazacağız.
*   [ ] **HTML Şablonu:** `templates/dashboard.html` dosyasını oluşturup iskeleti kuracağız.
*   [ ] **Stil (CSS):** `static/css/style.css` ile o "Glassmorphism" (Cam Efekti) tasarımını kodlayacağız.

---

## 📊 5. Bölüm: Grafikler ve Final
Pastanın üzerindeki çilek.
*   [ ] **Grafik Kütüphanesi:** Sayfaya **Chart.js** ekleyip, çektiğimiz fiyatları çizgi grafik olarak göstereceğiz.
*   [ ] **Son Kontroller:** Sitede dolaşıp hata var mı bakacağız.

---
👉 **Tavsiye:** Sırayla git. Şu an **2. Bölümdesin**. Önce `models.py` dosyasını hallet, sonra diğerlerine geçeceğiz!
