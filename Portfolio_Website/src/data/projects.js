import { BarChart3, Building, TrendingUp, Users } from 'lucide-react';

export const projects = [
    {
        id: 'stock-analysis',
        title: 'Borsa Analiz Platformu',
        category: 'Makine Öğrenmesi & Veri Bilimi',
        description: 'Yahoo Finance API\'den canlı hisse senedi verisi çeken, teknik analiz yapan ve Random Forest ile yarınki fiyatı tahmin eden uçtan uca borsa platformu.\n\nÖne Çıkan Özellikler:\n• requests ile Yahoo Finance JSON API\'den 8 hisse (ABD, Türkiye, Kripto) verisi çekme.\n• pandas ile hareketli ortalama (MA20/MA50), günlük getiri ve volatilite hesaplama.\n• Plotly ile interaktif candlestick, subplot ve korelasyon ısı haritası grafikleri.\n• Random Forest modeli ile yarınki kapanış fiyatı tahmini (MAE ≈ 5.97 $).\n• Streamlit dark-theme dashboard: KPI kartları, AI tahmin kutusu, hisse karşılaştırma.',
        tags: ['Streamlit', 'Plotly', 'Scikit-learn', 'Pandas', 'REST API'],
        icon: TrendingUp,
        image: 'https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?auto=format&fit=crop&w=1000&q=80',
        githubLink: 'https://github.com/oguzzakgl/stockAnalysisPlatform',
        demoLink: '#',
        stats: []
    },
    {
        id: 'real-estate',
        title: 'Emlak Danışmanı AI',
        category: 'Makine Öğrenmesi',
        description: 'Emlak piyasası verilerini analiz ederek konut fiyatlarını tahmin eden kapsamlı bir veri bilimi projesi.\n\nÖne Çıkan Özellikler:\n• Faker ve Numpy kullanılarak gerçekçi piyasa senaryoları simülasyonu ve sentetik veri üretimi.\n• Streamlit ile geliştirilmiş, anlık keşifsel veri analizi (EDA) sunan interaktif web arayüzü.\n• Konum, büyüklük ve özelliklere göre değerleme yapan makine öğrenmesi modelleri (Random Forest).\n• Fiyat dağılımlarını ve korelasyonları ortaya çıkaran Matplotlib ve Seaborn görselleştirmeleri.',
        tags: ['Streamlit', 'Scikit-learn', 'Pandas', 'Numpy', 'Faker'],
        icon: Building,
        image: 'https://images.unsplash.com/photo-1560518883-ce09059eeffa?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80',
        githubLink: 'https://github.com/oguzzakgl/EmlakVeriAnalizi',
        demoLink: '#',
        stats: []
    },
    {
        id: 'crypto-analysis',
        title: 'Kripto Para Analiz Paneli',
        category: 'Backend & Görselleştirme',
        description: 'Kripto para piyasalarını takip eden ve görselleştiren güçlü bir finansal analiz aracı.\n\nTeknik Detaylar:\n• Veri işleme ve servis etme için yüksek performanslı FastAPI backend.\n• CoinGecko API ile canlı piyasa fiyatlarını ve geçmiş trendleri çeken gerçek zamanlı entegrasyon.\n• Matplotlib kullanılarak sunucu tarafında oluşturulan dinamik grafikler.\n• Volatilite göstergelerini ve finansal metrikleri sunan Jinja2 tabanlı web arayüzü.',
        tags: ['FastAPI', 'Matplotlib', 'Python', 'CoinGecko API', 'Jinja2'],
        icon: BarChart3,
        image: 'https://images.unsplash.com/photo-1621761191319-c6fb62004040?auto=format&fit=crop&w=1000&q=80',
        githubLink: 'https://github.com/oguzzakgl/CryptoAnalysis',
        demoLink: '#',
        stats: []
    },
    {
        id: 'hr-analytics',
        title: 'İK Analitiği & Çalışan Performans',
        category: 'Veri Analizi',
        description: 'Çalışan sadakatini artırmak ve performans takibi yapmak için geliştirilen İnsan Kaynakları analiz çözümü.\n\nProje Kapsamı:\n• Ham İK verilerini temizlemek ve yapılandırmak için Pandas ile uçtan uca veri işleme.\n• Çalışan performans puanları, memnuniyet seviyeleri ve ayrılma (churn) oranlarının derinlemesine analizi.\n• Personel sirkülasyonundaki desenleri belirlemek için Seaborn ile görsel raporlama.\n• İşe alım ve elde tutma stratejilerini optimize etmek için veri odaklı içgörüler.',
        tags: ['Pandas', 'Seaborn', 'Matplotlib', 'Python', 'Veri Analizi'],
        icon: Users,
        image: 'https://images.unsplash.com/photo-1551836022-d5d88e9218df?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80',
        githubLink: 'https://github.com/oguzzakgl/HRAnalytics',
        demoLink: '#',
        stats: []
    }
];
