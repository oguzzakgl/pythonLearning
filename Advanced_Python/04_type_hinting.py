# Konu: Type Hinting (Tip İpuçları)
# Amaç: Kodun okunabilirliğini artırmak ve hataları önceden görmek.
# NOT: Python bu tipleri ZORLAMAZ. Sadece geliştiriciye ve IDE'ye (VS Code) ipucu verir.

# 1. DEĞİŞKENLERDE TİP BELİRTME
# ---------------------------------------------------------
isim: str = "Ali"
yas: int = 25
boy: float = 1.78
ogrenci_mi: bool = True

# Yanlış tip verirsen Python hata vermez ama altını çizer (sarı uyarı).
# yas = "yirmi beş"  # VS Code bunu sevmez ama çalıştırır.


# 2. FONKSİYONLARDA TİP BELİRTME (EN ÖNEMLİSİ)
# ---------------------------------------------------------
# Parametrelerin ne olduğunu ve fonksiyonun ne döndüreceğini (->) belirtiriz.

def topla(a: int, b: int) -> int:
    return a + b

def selamla(isim: str) -> str:
    return f"Merhaba {isim}"

print(f"Toplama: {topla(10, 20)}")
print(f"Selamlama: {selamla('Oğuz')}")


# 3. KARMAŞIK TİPLER (LIST, DICT, TUPLE)
# ---------------------------------------------------------
# Python 3.9+ sürümünde direkt list, dict kullanabilirsin.
# Eskiden "from typing import List" gerekirdi.

# Sadece sayı içeren bir liste
notlar: list[int] = [10, 20, 30, 40]

# Anahtarı string, değeri int olan bir sözlük (Örn: İsim -> Numara)
telefon_rehberi: dict[str, int] = {
    "Ali": 5551234,
    "Ayşe": 5559876
}

# Karışık veri içeren bir tuple (İsim, Yaş, Aktiflik)
kullanici: tuple[str, int, bool] = ("Mehmet", 30, True)


# 4. ÖZEL DURUMLAR (OPTIONAL, UNION)
# ---------------------------------------------------------
from typing import Union, Optional

# Union: "Ya şu olsun, ya bu olsun" demek.
# Örnek: ID numarası sayı da olabilir, yazı da.
user_id: Union[int, str] = "A123"
user_id = 101 # Bu da geçerli

# Optional: "Değer olabilir de olmayabilir de (None)" demek.
# Örnek: Kullanıcının orta adı olmayabilir.
def tam_isim(ad: str, soyad: str, orta_ad: Optional[str] = None) -> str:
    if orta_ad:
        return f"{ad} {orta_ad} {soyad}"
    return f"{ad} {soyad}"

print(f"Tam İsim 1: {tam_isim('Ahmet', 'Yılmaz')}")
print(f"Tam İsim 2: {tam_isim('Ahmet', 'Yılmaz', 'Can')}")
