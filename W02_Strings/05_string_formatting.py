# Konu: String Formatlama
# Amaç: format() metodu ve f-string kullanımı ile metinleri biçimlendirmek.

# string formatlama
name = "Oğuz"
age = 25
price = 99.9945454
text = "Benim adım {} ve yaşım {}.".format(name, age)
print(text)

# f-string formatlama
text_f = f"Benim adım {name} ve yaşım {age}."
print(text_f)

text_price = f"Ürünün fiyatı: {price:.2f} TL" # Virgülden sonra 2 basamak
print(text_price)   
text_price2 = f"Ürünün fiyatı: {price:,.2f} TL" # Binlik ayraç ekleme