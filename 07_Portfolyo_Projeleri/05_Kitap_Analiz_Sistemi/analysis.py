import pandas as pd
import os

"""
🧹 Veri Temizleme ve Analiz Modülü
---------------------------------
Scraper'dan gelen ham (raw) verileri ML modeline uygun hale getiren,
eksik/hatalı verileri düzelten modüldür.
"""

def clean_and_analyze():
    # Scriptin olduğu dizini baz alıyoruz
    current_dir = os.path.dirname(os.path.abspath(__file__))
    raw_path = os.path.join(current_dir, "data", "raw_books_data.csv")
    
    if not os.path.exists(raw_path):
        print(f"❌ Hata: '{raw_path}' dosyası bulunamadı!")
        return

    # Veriyi yükle
    df = pd.read_csv(raw_path)
    print(f"📊 {len(df)} adet ham veri yüklendi.")

    # 1. Fiyat Temizleme (£51.77 -> 51.77 float)
    df['Price'] = df['Price'].str.replace('£', '').astype(float)
    
    # 2. Rating Sayısallaştırma (One -> 1, Two -> 2 vb.)
    rating_map = {
        'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5
    }
    df['Rating_Num'] = df['Rating'].map(rating_map)

    # 3. İsim Uzunluğu (Özellik Mühendisliği - Feature Engineering)
    # Kitap isminin uzunluğu rating tahmini için bir özellik olabilir
    df['Title_Length'] = df['Title'].apply(len)

    # 4. Stok Durumu (In stock -> 1, Out of stock -> 0)
    df['In_Stock_Bool'] = df['Stock'].apply(lambda x: 1 if "In stock" in x else 0)

    # Temizlenmiş veriyi kaydet
    clean_path = os.path.join(current_dir, "data", "cleaned_books_data.csv")
    df.to_csv(clean_path, index=False, encoding="utf-8-sig")
    
    print("\n✅ Veriler temizlendi ve 'data/cleaned_books_data.csv' olarak kaydedildi.")
    print("\n📈 Temel İstatistikler:")
    print(df[['Price', 'Rating_Num', 'Title_Length']].describe())
    
    return df

if __name__ == "__main__":
    clean_and_analyze()
