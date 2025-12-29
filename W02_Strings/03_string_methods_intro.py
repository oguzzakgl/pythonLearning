# Konu: String Metotları
# Amaç: upper, lower, strip, replace, split gibi temel string metotlarını öğrenmek.

text=" Python is doing well "
print(text.upper())  # PYTHON IS DOING WELL
print(text.lower())  # python is doing well
print(text.strip())  # Python is doing well (baştaki ve sondaki boşluklaraı kaldırır)
print(text.replace("Python", "Java"))  #  Java is doing well
print(text.split())  # ['Python', 'is', 'doing', 'well']