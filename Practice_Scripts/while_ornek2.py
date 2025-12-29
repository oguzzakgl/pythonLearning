# While Döngüsü Örnekleri (Çalışma)
# numbers = [3, 5, 7, 9, 11]

# i = 0
# while i < len(numbers):
#     print(f"Sayı: {numbers[i]}")
#     i += 1
# print("Döngü tamamlandı.")

# baslangic = int(input("baslangıc değerini giriniz:"))
# bitis = int(input("bitis değerini giriniz:"))

# while baslangic < bitis :
#     if baslangic % 2 == 0:
#         print(baslangic, end=" ")
#     baslangic += 1


# x = 100

# while x > 0:
#     print(x, end=" ")
#     x -= 1


liste = []
while len(liste) < 5:
    sayi = int(input("Lütfen bir sayi giriniz: "))
    liste.append(sayi)

liste.sort()
print("Girilen sayılar:", liste)
