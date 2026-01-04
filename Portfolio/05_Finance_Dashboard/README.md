# 💰 Kişisel Finans Kontrol Paneli (Full-Stack)

Bu proje, kişisel gelir ve giderlerinizi takip etmenizi sağlayan, Python (FastAPI) backend ve React frontend ile geliştirilmiş modern bir finansal yönetim uygulamasıdır.

![Ekran Görüntüsü](screenshot.png) *(Varsa ekran görüntüsü eklenebilir)*

## 🚀 Özellikler

*   **Gelir/Gider Takibi:** Harcamalarınızı ve gelirlerinizi tarih ve kategori bazlı ekleyin.
*   **Anlık İstatistikler:** Toplam Gelir, Toplam Gider, Net Bakiye ve En Çok Harcanan Kategori anlık olarak hesaplanır.
*   **Görsel Analiz:** Harcamalarınızın dağılımını gösteren dinamik pasta grafiği (Matplotlib entegrasyonu).
*   **Detaylı Liste & Filtreleme:** İşlemlerinizi listeleyin, "Gelir/Gider" sekmeleriyle filtreleyin veya Arama Çubuğu ile spesifik harcamaları bulun.
*   **Kart Görünümü:** Modern, karanlık tema (Dark Mode) uyumlu, responsive tasarım.

## 🛠️ Teknolojiler

### Backend
*   **Python 3.10+**
*   **FastAPI:** Hızlı ve modern API framework'ü.
*   **Pandas:** Veri analizi ve işlem özetleri için.
*   **Matplotlib:** Grafik oluşturma için.
*   **SQLite:** Hafif ve hızlı yerel veritabanı.

### Frontend
*   **React (Vite):** Hızlı geliştirme ortamı.
*   **CSS3 (Flexbox & Grid):** Modern ve duyarlı tasarım.
*   **Fetch API:** Backend ile haberleşme.

## ⚙️ Kurulum ve Çalıştırma

Proje iki ana klasörden oluşur: `backend` ve `frontend`.

### 1. Backend Kurulumu

```bash
cd backend
# Sanal ortam oluşturma (Opsiyonel ama önerilir)
python -m venv venv
# Windows için aktivasyon:
venv\Scripts\activate

# Kütüphaneleri yükleyin
pip install -r requirements.txt

# Sunucuyu başlatın
uvicorn main:app --reload
```
Backend `http://localhost:8000` adresinde çalışacaktır.

### 2. Frontend Kurulumu

Yeni bir terminal açın ve frontend klasörüne gidin:

```bash
cd frontend
# Bağımlılıkları yükleyin
npm install

# Uygulamayı başlatın
npm run dev
```
Frontend genellikle `http://localhost:5173` (veya `5174/5175`) adresinde çalışacaktır. Terminaldeki linke tıklayarak açabilirsiniz.

## 📂 Proje Yapısı

```
05_Finance_Dashboard/
├── backend/
│   ├── main.py          # API Endpoint'leri
│   ├── database.py      # Veritabanı işlemleri (SQLite)
│   ├── analytics.py     # Veri analizi kodları (Pandas)
│   ├── visuals.py       # Grafik oluşturma (Matplotlib)
│   └── schema.sql       # Veritabanı şeması
├── frontend/
│   ├── src/
│   │   ├── components/  # React bileşenleri (Form, List, Chart)
│   │   ├── App.jsx      # Ana düzen
│   │   └── main.jsx     # Giriş noktası
└── README.md
```

## 📝 Lisans
Bu proje açık kaynaklıdır ve eğitim amaçlı geliştirilmiştir.
