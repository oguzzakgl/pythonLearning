import sqlite3
import pandas as pd
import numpy as np
import os

def raporla():
    # Veritabanı bağlantısı
    db_path = os.path.join(os.path.dirname(__file__), "ecommerce.db")
    con = sqlite3.connect(db_path)
    
    print("--- E-Ticaret Veri Analiz Raporu ---\n")

    # 1. Kritik Stok Analizi
    df_urunler = pd.read_sql("SELECT * FROM Urunler", con)
    
    # Stok < 20 ise KRİTİK, değilse Normal
    df_urunler["stok_durumu"] = np.where(df_urunler["stok_adedi"] < 20, "KRİTİK", "Normal")
    
    print("1. KRİTİK STOK RAPORU:")
    # Sadece KRİTİK olanları filtrele
    kritik_urunler = df_urunler[df_urunler["stok_durumu"] == "KRİTİK"]
    
    # Sadece istediğimiz sütunları seçip ekrana yazdırıyoruz.
    print(kritik_urunler[["urun_adi", "stok_adedi", "stok_durumu"]])
    print("-" * 30 + "\n")

    # 2. En Çok Ciro Yapan Ürünler
    # Ürünler ve SiparisDetay tablolarını birleştir
    query_satis = """
    SELECT Urunler.urun_adi, SiparisDetay.adet, SiparisDetay.birim_fiyat 
    FROM SiparisDetay
    JOIN Urunler ON SiparisDetay.urun_id = Urunler.id
    """
    df_satis = pd.read_sql(query_satis, con)
    
    # Toplam tutar hesapla
    df_satis["toplam_tutar"] = df_satis["adet"] * df_satis["birim_fiyat"]
    
    # Ürün bazında toplam ciro sıralaması
    en_cok_satanlar = df_satis.groupby("urun_adi")["toplam_tutar"].sum().sort_values(ascending=False)
    
    print("2. EN ÇOK CİRO YAPAN ÜRÜNLER:")
    print(en_cok_satanlar)
    print("-" * 30 + "\n")

    con.close()

if __name__ == "__main__":
    raporla()
