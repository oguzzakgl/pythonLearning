
INSERT INTO Kullanicilar (ad_soyad, email) VALUES ('Ahmet Yılmaz', 'ahmet.yilmaz@example.com');
INSERT INTO Kullanicilar (ad_soyad, email) VALUES ('Ayşe Kaya', 'ayse.kaya@example.com');
INSERT INTO Kullanicilar (ad_soyad, email) VALUES ('Mehmet Veli', 'mehmet.veli@example.com');
INSERT INTO Kullanicilar (ad_soyad, email) VALUES ('Fatima Ali', 'fatima.ali@example.com');
INSERT INTO Kullanicilar (ad_soyad, email) VALUES ('Ahmet Yılmaz', 'ahmet.kaya@example.com');


INSERT INTO Urunler (urun_adi, kategori, fiyat, stok_adedi) VALUES ('Laptop', 'Elektronik', 1500.00, 10);
INSERT INTO Urunler (urun_adi, kategori, fiyat, stok_adedi) VALUES ('Mouse', 'Elektronik', 50.00, 20);
INSERT INTO Urunler (urun_adi, kategori, fiyat, stok_adedi) VALUES ('Kahve', 'Mutfak', 10.00, 50);
INSERT INTO Urunler (urun_adi, kategori, fiyat, stok_adedi) VALUES ('Kahve', 'Mutfak', 10.00, 50);
INSERT INTO Urunler (urun_adi, kategori, fiyat, stok_adedi) VALUES ('Kahve', 'Mutfak', 10.00, 50);


INSERT INTO Siparisler (kullanici_id, siparis_tarihi, toplam_tutar) VALUES (1, '2023-01-01 10:00:00', 1500.00);
INSERT INTO Siparisler (kullanici_id, siparis_tarihi, toplam_tutar) VALUES (2, '2023-01-02 11:00:00', 50.00);
INSERT INTO Siparisler (kullanici_id, siparis_tarihi, toplam_tutar) VALUES (3, '2023-01-03 12:00:00', 10.00);
INSERT INTO Siparisler (kullanici_id, siparis_tarihi, toplam_tutar) VALUES (4, '2023-01-04 13:00:00', 10.00);
INSERT INTO Siparisler (kullanici_id, siparis_tarihi, toplam_tutar) VALUES (5, '2023-01-05 14:00:00', 10.00);


INSERT INTO SiparisDetay (siparis_id, urun_id, adet, birim_fiyat) VALUES (1, 1, 1, 1500.00);
INSERT INTO SiparisDetay (siparis_id, urun_id, adet, birim_fiyat) VALUES (2, 2, 1, 50.00);
INSERT INTO SiparisDetay (siparis_id, urun_id, adet, birim_fiyat) VALUES (3, 3, 1, 10.00);
INSERT INTO SiparisDetay (siparis_id, urun_id, adet, birim_fiyat) VALUES (4, 4, 1, 10.00);
INSERT INTO SiparisDetay (siparis_id, urun_id, adet, birim_fiyat) VALUES (5, 5, 1, 10.00);