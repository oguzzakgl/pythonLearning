
# Konu: Dosyaya Yazma (Write)
# Amaç: 'w' modu ile dosya oluşturma ve üzerine yazma (overwrite) işlemi.

# w yazma modu
# dosyayı konumda oluşturur
# eğer konumda aynı dosya varsa içeriğini siler ve yeni oluşturur

# file = open("dosya.txt", "w", encoding="utf-8")

# file.write("Python programlama dili\n")
# file.close()

with open("dosya.txt", "w", encoding="utf-8") as file:
    file.write("Python programlama dili\n")
    file.write("Python 3 programlama dili\n")

with open("dosya.txt", "r", encoding="utf-8") as file:
    for i in file:
        print(i, end="")