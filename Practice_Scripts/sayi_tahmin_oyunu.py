# Sayı Tahmin Oyunu (Basit)
import random

random_sayi = random.randint(1,100)
tahmin_hakki = 5

print("Sayı tahmin oyununa hoş geldiniz.")

while (tahmin_hakki>0):
    tahmin = int(input("Lutfen 1 ile 100 arasında bir sayı giriniz: "))
    tahmin_hakki -=1
    if tahmin < 1 or tahmin > 100:
        print("Lutfen 1 ile 100 arasında bir sayı giriniz")
        continue
    if tahmin == random_sayi:
        print (f"Tebrikler {tahmin_hakki} denemede doğru bildiniz.")
        break
    elif tahmin < random_sayi:
        print ("Daha büyük bir sayı giriniz")
    elif tahmin > random_sayi:
        print ("Daha kücük bir sayi giriniz")
else:
    print ("Tahmin hakkınız bitti.")
        