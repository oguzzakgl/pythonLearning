# =========================================================
# 🚀 SIRA SENDE! (Pekiştirme Örnekleri)
# =========================================================

# SORU 1: Kelime Uzunlukları
# Görev: Aşağıdaki cümledeki her kelimenin uzunluğunu (harf sayısını) bir listeye at.
cumle = "Python öğrenmek çok zevkli bir iş"
kelimeler = cumle.split() # ['Python', 'öğrenmek', ...] yapar.
# Uzunlukları hesapla
list1 = [len(kelime) for kelime in kelimeler]
print(list1)


# SORU 2: Zam Yapma (If-Else)
# Görev: Maaş listesindeki;
# - 50000 TL altındakilere %20 zam yap (maas * 1.2)
# - 50000 TL ve üstündekilere %10 zam yap (maas * 1.1)
maaslar = [30000, 45000, 60000, 80000, 25000]
# yeni_maaslar = [ ... BURAYI SEN DOLDUR ... ]
# print(f"Yeni Maaşlar: {yeni_maaslar}")

list2 = [maas *  1.2 if maas < 50000 else maas * 1.1 for maas in maaslar]
print(list2)


# SORU 3: Pozitif Sayılar
# Görev: Karışık sayı listesinden sadece pozitif olanları (0'dan büyük) yeni bir listeye al.
sayilar = [10, -5, 20, -3, 0, 15, -8]
# pozitifler = [ ... BURAYI SEN DOLDUR ... ]
# print(f"Pozitifler: {pozitifler}")

positive_comp = [number for number in sayilar  if number > 0]
print(positive_comp)



# SORU 4: İsim Filtreleme ve Dönüştürme
# Görev: İsim listesinde "A" ile başlayanları bul ve hepsini BÜYÜK HARF'e çevir (upper()).
isimler = ["Ali", "Veli", "Ayşe", "Fatma", "Ahmet", "Mehmet"]
# a_ile_baslayanlar = [ ... BURAYI SEN DOLDUR ... ]
# print(f"A ile Başlayanlar: {a_ile_baslayanlar}")

a_ile_baslayanlar = [isim.upper() for isim in isimler if isim.startswith("A")]
print(a_ile_baslayanlar)



# SORU 5: Kareler Listesi (Tuple Olarak)
# Görev: 1'den 5'e kadar olan sayıların kendisini ve karesini tuple olarak tut.
# Beklenen Çıktı: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
# Sayı ve karesi tuple'ı
# kareler = [ ... BURAYI SEN DOLDUR ... ]
# print(f"Sayı ve Karesi: {kareler}")

tuple_list = [(number, number**2) for number in range(1, 6)]
print(tuple_list)