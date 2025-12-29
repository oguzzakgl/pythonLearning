# Konu: Dosya Okuma ve Hata Yönetimi
# Amaç: open() fonksiyonu modları (r, w, a), with bloğu kullanımı ve try-except ile hata yakalama.

"""
    open() fonksiyonu ile dosya açma ve kapama işlemleri
    open(dosya adi, dosya_erisim_modu)
    dosya_erisim_modu: 
        'r' : okuma modu (varsayılan)
        'w' : yazma modu (dosya yoksa oluşturur, varsa içeriğini siler)
        'a' : ekleme modu (dosya yoksa oluşturur, varsa sonuna ekler)
        'b' : ikili mod (binary)
        't' : metin modu (varsayılan)
        '+' : okuma ve yazma modu

"""

f = open("log.txt", encoding="utf-8")
print(f.read())
f.close()


with open("log.txt", encoding="utf-8") as f:
    print(f.read(10))
    print(f.tell())
    print(f.read())
    print(f.tell())
try:
    with open("log2.txt", "r", encoding="utf-8") as file:
        for i in file:
            print(i, end="")
except FileNotFoundError as e:
    print("Dosya bulunamadı." + str(e))


