-- E-Ticaret Veritabanı Şeması (schema.sql)
-- Tabloları temizle
DROP TABLE IF EXISTS SiparisDetay;
DROP TABLE IF EXISTS Siparisler;
DROP TABLE IF EXISTS Urunler;
DROP TABLE IF EXISTS Kullanicilar;

-- Kullanicilar tablosu
CREATE TABLE IF NOT EXISTS Kullanicilar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ad_soyad TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    kayit_tarihi DATETIME DEFAULT CURRENT_TIMESTAMP
);
-- Urunler tablosu
CREATE TABLE IF NOT EXISTS Urunler (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    urun_adi TEXT,
    kategori TEXT,
    fiyat REAL,
    stok_adedi INTEGER
);
-- Siparisler tablosu
CREATE TABLE IF NOT EXISTS Siparisler (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kullanici_id INTEGER,
    siparis_tarihi DATETIME,
    toplam_tutar REAL,
    FOREIGN KEY (kullanici_id) REFERENCES Kullanicilar(id)
);
-- SiparisDetay tablosu
CREATE TABLE IF NOT EXISTS SiparisDetay (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    siparis_id INTEGER,
    urun_id INTEGER,
    adet INTEGER,
    birim_fiyat REAL,
    FOREIGN KEY (siparis_id) REFERENCES Siparisler(id),
    FOREIGN KEY (urun_id) REFERENCES Urunler(id)
);  