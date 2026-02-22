# Konu: String Formatlama Örneği
# Amaç: Vize ve final notlarını alıp ortalamayı hesaplayarak formatlı yazdırmak.

vize_not = input("Lütfen vize notunuzu giriniz: ")
final_not = input("Lütfen final notunuzu giriniz: ")
ortalama = (float(vize_not) * 0.4) + (float(final_not) * 0.6)
result=f"vize notunuz: {vize_not}\nfinal notunuz: {final_not}\nortalamanız: {ortalama:.2f}"
print(result)