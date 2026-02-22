# Konu: Kaçış Karakterleri (Escape Sequences)
# Amaç: \n, \t, \\ gibi özel karakterlerin kullanımını anlamak.

# -----------------------------------------------------
# Kaçış karakterleri string içinde özel etkiler oluşturur.
# En yaygınları: \n (yeni satır), \t (sekme), \\ (ters eğik),
# \' ve \" (tırnak yazdırma), \r (satır başına dön), \b (geri sil),
# \f (form feed), \v (dikey sekme), \a (ziller/bip – her terminal desteklemez).

# 1) Yeni satır ve sekme
print("Satır1\nSatır2")             # \n: Yeni satır
print("Ad:\tKaan")                  # \t: Yatay sekme (tab)

# 2) Ters eğik çizgi ve tırnakları kaçırma
print("C:\\Users\\Kaan")            # \\: Tek bir \ üretir
print('O\'Reilly')                  # \': Tek tırnak yazdır
print("Dedi ki: \"Merhaba\"")       # \": Çift tırnak yazdır

# 3) \r (carriage return) – satır başına dön (üzeri yazabilir; terminale göre değişir)
print("Merhaba Dünya\rABC")         # Çıktıda baş tarafa "ABC" yazar (görünüm ortamdan etkilenir)

# 4) \b (backspace) – bir karakter geri (görsel sonuç terminale göre değişir)
print("abc\bX")                     # 'abX' gibi görünebilir

# 5) \f (form feed) ve \v (dikey sekme) – çoğu terminalde yeni satır benzeri davranır
print("Sayfa1\fSayfa2")
print("Üst\vAlt")

# 6) \a (bell) – bazı ortamlarda bip sesi (çoğu modern terminalde sessiz kalır)
print("Uyarı\aBip?")

# 7) Ham (raw) string – kaçışlar işlenmez; regex ve Windows path'leri için idealdir
print(r"C:\Users\Kaan")             # r"...": \ karakterleri aynen yazılır
print(r"\n\t\b")                    # Ekrana \n \t \b olarak görünür, etkileri uygulanmaz

# 8) Üç tırnak (çok satırlı metin) – kaçışlar yine çalışır
s = """Satır1
Satır2\t(Sekme burada gerçek sekme)
Satır3\\TersEğik"""
print(s)

# 9) repr() ile ham temsili görmek – kaçışları görselleştirir
x = "Merhaba\nPython\t\\"
print(x)                            # Kaçışlar uygulanmış hali
print(repr(x))                      # 'Merhaba\nPython\t\\' ham gösterim

# 10) Özet karışık örnek
y = "Klasör: C:\\Proje\\veri\nDosya: \"rapor.txt\"\tDurum: OK\b!"
print(y)

# ---------------------------------
# 🧠 NOTLAR
# - Kaçışlar sadece string literal içinde yorumlanır; r"..." ile devre dışı bırak.
# - \r ve \b'nin görsel etkisi terminal/OS'a göre değişir.
# - Tırnak karakterlerinin içinde aynı tip tırnak kullanacaksan \ kaçır.
# - Çok satırlı metin için üç tırnak kullan; yine de kaçışlar geçerlidir.
# - repr(obj) ham kaçışları gösterir, debug için faydalıdır.
# ---------------------------------
