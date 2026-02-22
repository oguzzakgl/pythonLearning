import sqlite3
import os

def veritabani_kur():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "ecommerce.db")
    schema_path = os.path.join(base_dir, "schema.sql")
    seed_path = os.path.join(base_dir, "seed.sql")

    print(f"Veritabanı oluşturuluyor: {db_path}")
    
    con = sqlite3.connect(db_path)
    cursor = con.cursor()
    
    try:

        print(f"Schema yükleniyor: {schema_path}")
        if os.path.exists(schema_path):
            with open(schema_path, "r", encoding="utf-8") as f:
                schema_sql = f.read()
            cursor.executescript(schema_sql)
            con.commit()
            print("Tablolar oluşturuldu.")
        else:
            print(f"HATA: schema.sql bulunamadı! Yol: {schema_path}")
            return
        

        print("Veriler yükleniyor (seed.sql)...")
        if os.path.exists(seed_path):
            with open(seed_path, "r", encoding="utf-8") as f:
                seed_sql = f.read()
            cursor.executescript(seed_sql)
            con.commit()
            print("Veriler eklendi.")
        else:
            print(f"seed.sql bulunamadı! Yol: {seed_path}")
            
    except Exception as e:
        print(f"HATA OLUŞTU: {e}")
        
    finally:
        con.close()
        print("Bağlantı kapatıldı.")

if __name__ == "__main__":
    veritabani_kur()
