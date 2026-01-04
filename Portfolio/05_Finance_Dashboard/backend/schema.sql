

-- Kullanıcılar Tablosu
-- CREATE TABLE users ...
CREATE TABLE IF NOT EXISTS users (
    kullanici_id INTEGER NOT NULL,
    ad_soyad TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    kayit_tarihi DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (kullanici_id)
);
-- Harcamalar/Gelirler Tablosu
-- CREATE TABLE transactions ...
CREATE TABLE IF NOT EXISTS transactions (
    kullanici_id INTEGER NOT NULL,
    baslik TEXT NOT NULL,
    miktar REAL NOT NULL,
    tip TEXT NOT NULL,
    tarih DATE NOT NULL,
    FOREIGN KEY (kullanici_id) REFERENCES users(kullanici_id)
);