# Konu: Dictionary (Sözlük) Örneği
# Amaç: Öğrenci notlarını sözlük yapısında saklama ve veri ekleme yöntemleri.

ogrenci_listesi = {
    101: {"ad": "Ali", "soyad": "Yılmaz", "not": 85},
    102: {"ad": "Ayşe", "soyad": "Kara", "not": 92},
    103: {"ad": "Mehmet", "soyad": "Demir", "not": 90}
}
print(f"Orijinal Sözlük: {ogrenci_listesi}")
# ogrenci_listesi.append(104, {"ad": "Fatma", "soyad": "Çelik", "not": 88}) # HATA verir
# print(ogrenci_listesi)
ogrenci_listesi[104] = {"ad": "Fatma", "soyad": "Çelik", "not": 88} # Doğru ekleme yöntemi
print(f"Ekleme sonrası sözlük: {ogrenci_listesi}") 