import pandas as pd
from database import get_db_connection

# ---------------------------------------------------------
# ADIM 1: Veriyi Çekme Fonksiyonu (get_data_as_dataframe)
# ---------------------------------------------------------
# Bu fonksiyonun yapması gerekenler:
# 1. get_db_connection() fonksiyonunu kullanarak veritabanı bağlantısını al.
# 2. "SELECT * FROM transactions" SQL sorgusu ile tüm verileri pd.read_sql kullanarak çek.
# 3. Bağlantıyı kapat.
# 4. 'tarih' sütununu pd.to_datetime ile tarih formatına çevir (işlemleri kolaylaştırır).
# 5. Oluşturduğun DataFrame'i (df) return et.

def get_data_as_dataframe():
    con, _ = get_db_connection()
    df = pd.read_sql("SELECT * FROM transactions", con)
    con.close()

    if 'tarih' in df.columns:
        df['tarih'] = pd.to_datetime(df['tarih'])

    return df
# ---------------------------------------------------------
# ADIM 2: Analiz Fonksiyonu (analyze_spending_by_category)
# ---------------------------------------------------------
# Bu fonksiyonun yapması gerekenler:
# 1. Parametre olarak bir DataFrame (df) almalı.
# 2. İpucu: Eğer 'tip' sütunu varsa sadece 'gider' olanları filtrele.
# 3. df.groupby() kullanarak harcamaları 'baslik' (veya kategori) sütununa göre grupla.
# 4. .sum() ile bu grupların toplam miktarını hesapla.
# 5. Sonuçları 'miktar'a göre sırala (sort_values) ki en çok harcanan en üstte görünsün.
# 6. Özetlenmiş DataFrame'i return et.

def analyze_spending_by_category(df):
    """
    Verilen DataFrame içindeki Gider kalemlerini filtreler,
    kategorilere (baslik) göre gruplar ve toplam tutarları hesaplar.
    """
    df = df[df['tip'] == 'Gider'] 
    summary_df = df.groupby('baslik')['miktar'].sum().reset_index()
    summary_df = summary_df.sort_values('miktar', ascending=False)
    return summary_df

def calculate_summary_stats(df):
    """
    Tüm veriler üzerinden Toplam Gelir, Gider, Bakiye ve 
    en yüksek harcama yapılan kategoriyi hesaplar.
    """
    if df.empty:
        return {
            "toplam_gelir": 0,
            "toplam_gider": 0,
            "bakiye": 0,
            "en_cok_harcanan": "Veri Yok"
        }

    # Gelir ve Gider Toplamları
    toplam_gelir = df[df['tip'] == 'Gelir']['miktar'].sum()
    toplam_gider = df[df['tip'] == 'Gider']['miktar'].sum()
    bakiye = toplam_gelir - toplam_gider

    # En Çok Harcama Yapılan Kategori Analizi
    giderler_df = df[df['tip'] == 'Gider']
    
    if not giderler_df.empty:
        en_cok_harcanan = giderler_df.groupby('baslik')['miktar'].sum().idxmax()
        en_cok_miktar = giderler_df.groupby('baslik')['miktar'].sum().max()
        en_cok_bilgi = f"{en_cok_harcanan} ({en_cok_miktar} TL)"
    else:
        en_cok_bilgi = "-"

    return {
        "toplam_gelir": float(toplam_gelir),
        "toplam_gider": float(toplam_gider),
        "bakiye": float(bakiye),
        "en_cok_harcanan": en_cok_bilgi
    }


# 3. İstatistikleri hesapla:
#    - Toplam Gelir (Tip == 'Gelir' olanların 'miktar' toplamı)
#    - Toplam Gider (Tip == 'Gider' olanların 'miktar' toplamı)
#    - Bakiye (Gelir - Gider)
#    - En çok harcanan kategori (Giderleri baslik'a göre grupla, topla, en büyüğünü bul)
#
# 4. Şöyle bir sözlük (dictionary) döndür:
#    return {
#       "toplam_gelir": ...,
#       "toplam_gider": ...,
#       "bakiye": ...,
#       "en_cok_harcanan": ...
#    }
#
# def calculate_summary_stats(df):
#     ...