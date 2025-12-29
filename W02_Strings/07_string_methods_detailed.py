# Konu: İleri String Metotları
# Amaç: casefold, title, capitalize, swapcase, islower/isupper gibi metotları öğrenmek.

text = "evime hosgeldiniz"


print(text.casefold())     # lower'dan daha agresif
print(text.title())        # Her kelimenin ilk harfi büyük
print(text.capitalize())   # Sadece ilk harf büyük ama rakamdana sonraki harfler de büyük olur
result = text.swapcase()
print(result)              # Büyük-küçük harf değişimi büyükler küçük, küçükler büyük olur
result=text.islower()
print(result)              # Tüm karakterler küçük mü? True/False
result=text.isupper()
print(result)              # Tüm karakterler büyük mü? True/False
result=text.center(21,"*")     # Metni ortalar
print(result)