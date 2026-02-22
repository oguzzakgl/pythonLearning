# Konu: Dosyaya Ekleme (Append)
# Amaç: 'a' modu ile mevcut dosyanın sonuna veri ekleme işlemi.

# a yazma modu
# dosyayı konumda oluşturur
# eğer konumda aynı dosya varsa içeriğini silmeden sonuna ekleme

with open("dosya.txt", "a", encoding="utf-8") as file:
    file.write("birinci satir\n")