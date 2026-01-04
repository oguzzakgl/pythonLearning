# 🗺️ Finance Dashboard - Kodlama Yol Haritası

Bu proje, Python ve React yeteneklerini birleştireceğin büyük bir adımdır. Senin için "kopya çekebileceğin" örnek dosyaları da ekledim. 😉

---

## 🏗️ Faz 1: Kayıt Defterini Hazırlama (Backend / SQL)

Önce verilerin nerede ve nasıl saklanacağını belirlemeliyiz.

### 1. Adım: Veritabanı Tasarımı (`backend/schema.sql`)
*   **Amaç:** Banka defterinin sayfalarını çizmek.
*   **Yapılacak:** `transactions` (harcamalar) ve `budget_goals` tablolarını oluştur.
*   **👀 Örnek Dosya:** `Portfolio/02_Ecommerce_DB/schema.sql` (Oradaki tablo oluşturma mantığına bak).

### 2. Adım: Python ile Bağlantı (`backend/database.py`)
*   **Amaç:** Python'un SQL ile konuşmasını sağlamak.
*   **Yapılacak:** `get_db_connection` ve `add_transaction` fonksiyonlarını yaz.
*   **👀 Örnek Dosya:** `W14_Mini_Proje_Stok_Analiz/database.py` (Oradaki bağlantı fonksiyonunu alabilirsin).

---

## 🔌 Faz 2: Sunucuyu Kurma (Backend / FastAPI)

Veritabanını dış dünyaya (Web sitesine) açan kapıdır.

### 3. Adım: API Uçlarını Yazma (`backend/main.py`)
*   **Amaç:** Web sitesinin isteklerini karşılamak.
*   **Yapılacak:** `/transactions` adresine GET ve POST isteklerini hazırla.
*   **👀 Örnek Dosya:** `Portfolio/04_Crypto_Analysis/main.py` (FastAPI kurulumuna bak).

---

## 📊 Faz 3: Analiz ve Görsellik (Data Science)

Veriyi sadece listelemek yetmez, anlamlandırmak gerekir.

### 4. Adım: Veri Analizi (`backend/analytics.py`)
*   **Amaç:** Harcamaları kategorilere göre toplamak.
*   **Yapılacak:** Pandas kullanarak SQL'den veriyi çek ve `groupby` yap.
*   **👀 Örnek Dosya:** `Portfolio/04_Crypto_Analysis/services.py` (Pandas DataFrame oluşturma kısmı).

### 5. Adım: Grafik Çizimi (`backend/visuals.py`)
*   **Amaç:** Harcama pastası çizmek.
*   **Yapılacak:** Matplotlib ile grafiği çizip `static/chart.png` olarak kaydet.
*   **👀 Örnek Dosya:** `W15_Veri_Gorsellestirme/01_matplotlib.py` veya `Portfolio/04_Crypto_Analysis/services.py` (Matplotlib güncellememiz).

---

## ⚛️ Faz 4: Makyaj ve Sunum (Frontend / React)

Kullanıcının göreceği ekranı tasarlamak.

### 6. Adım: React Kurulumu
*   **Yapılacak:** `client` klasörü içinde Vite ile React projesi oluştur.

### 7. Adım: Arayüz ve Veri Bağlantısı
*   **Yapılacak:** Form ve Tablo oluştur, `fetch()` ile verileri çek.
*   **👀 Örnek Dosya:** `Portfolio/04_Crypto_Analysis/templates/index.html` (Oradaki `fetch` ve `document.getElementById` mantığı React'te `useEffect` ve `useState` olacak ama mantık aynı).

---

## 🚀 Başlangıç
`backend/schema.sql` dosyasını aç ve **`Portfolio/02_Ecommerce_DB/schema.sql`** dosyasındaki örneklere bakarak tablolarını oluşturmaya başla!
