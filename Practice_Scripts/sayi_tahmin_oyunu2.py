# Sayı Tahmin Oyunu (Puanlı)
import random

sayi = random.randint(1, 100)
puan = 100
hak = 10

print ("Sayı tahmin oyununa hoş geldiniz!")
print ("1 ile 100 arasında bir sayı tuttum. Bu sayıyı bilmek için 10 hakkınız var.")

while hak > 0:
    tahmin = int(input("Tahmininizi giriniz: "))
    hak -= 1
    if tahmin < 1 or tahmin > 100:
        print("Lütfen 1 ile 100 arasında bir sayı giriniz.")
        continue
    if tahmin == sayi:
        print(f"Tebrikler! {10 - hak} denemede doğru bildiniz. Puanınız: {puan}")
        break
    elif tahmin < sayi:
        print("Daha büyük bir sayı giriniz.")
        puan -= 10
    else:
        print("Daha küçük bir sayı giriniz.")
        puan -= 10
else:
    print(f"Tahmin hakkınız bitti. Doğru sayı {sayi} idi.")
