# Konu: String Parçalama (Slicing)
# Amaç: String ifadelerin belirli bölümlerini indeks kullanarak almak.

text = "python is weird"

print(text[1:5]) # ytho
print(text[:6])  # python
print(text[7:])  # is weird
print(text[-5:]) # weird
print(text[:-8]) # python
print(text[:])   # python is weird
print(text[-11:-6]) # on is
