# Konu: Faktöriyel Hesaplama
# Amaç: While döngüsü kullanarak bir sayının faktöriyelini hesaplamak.

result=1
i=1
number=int(input("Faktöriyelini hesaplamak istediğiniz sayıyı giriniz: "))
while i<=number:
    result*=i
    i+=1
print(f"{number}! = {result}")