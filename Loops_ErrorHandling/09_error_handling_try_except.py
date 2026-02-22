# --- Python Hata Yönetimi (try-except) ---

print("="*30)
print("BÖLÜM 1: HATA YÖNETİMİ OLMADAN (ÇÖKEN KOD)")
print("="*30)

# Aşağıdaki satırın başındaki '#' işaretini kaldırırsanız,
# program 'ZeroDivisionError' hatası verir ve burada çöker.
# Kalan kodlar (Bölüm 2, 3, 4) ASLA çalışmaz.

# sayi = 10 / 0 
# print("Bu satır asla görünmeyecek.")

print("Bölüm 1 (atlandı) - Program çökmedi çünkü hata kodu yorum satırında.")
print("\n")


print("="*30)
print("BÖLÜM 2: TEMEL try...except KULLANIMI (Genel Hata Yakalama)")
print("="*30)

print("Program başladı.")
try:
    # Hata çıkma potansiyeli olan kodu bu 'try' bloğuna yazarız.
    print("Bölme işlemi deneniyor...")
    sayi = 10 / 0  # Burası 'ZeroDivisionError' fırlatacak
    print(f"Sonuç: {sayi}") # Hata olduğu için burası çalışmaz
    
except:
    # 'try' bloğunda herhangi bir hata yakalanırsa, bu 'except' bloğu çalışır.
    # Bu çok genel bir yaklaşımdır.
    print("!!! HATA (Bölüm 2): Bir sorun oluştu! Program çökmedi, devam ediyor.")

# Program çökmediği için burası çalışır:
print("Program bitti. (Bölüm 2 sonu)")
print("\n")


print("="*30)
print("BÖLÜM 3: BELİRLİ HATA TÜRLERİNİ YAKALAMAK")
print("="*30)

print("--- Örnek 3a: ValueError (Kullanıcı Girdisi) ---")
try:
    # Kullanıcıdan yaşını girmesini isteyelim
    # Test için sayı yerine "otuz" gibi bir metin girmeyi deneyin.
    yas_str = input("Lütfen yaşınızı girin (örn: 25): ")
    
    # int() fonksiyonu "otuz" gibi bir metni sayıya çeviremez
    # ve 'ValueError' fırlatır.
    yas_int = int(yas_str) 
    
    print(f"Harika! {yas_int} yaşındasınız.")

except ValueError:
    # SADECE 'ValueError' türünde bir hata olursa burası çalışır.
    print("!!! HATA (Bölüm 3a): Lütfen sayısal bir değer girin (örn: 25).")

print("\n")


print("--- Örnek 3b: KeyError (Sözlük Hatası) ---")
# Sözlükleri tekrar etmiştik, oradan bir örnek:
kullanici = {
    "k_adi": "ahmet_y",
    "isim": "Ahmet Yılmaz"
}

try:
    # Olmayan bir anahtarı ('sehir') çağırmayı DENE
    print(f"Kullanıcının adı: {kullanici['isim']}") # Bu çalışır
    print("Kullanıcının şehri aranıyor...")
    print(f"Kullanıcının şehri: {kullanici['sehir']}") # Bu 'KeyError' verir

except KeyError:
    # 'KeyError' yakalanırsa burayı çalıştır
    print("!!! HATA (Bölüm 3b): 'sehir' bilgisi bu kullanıcıda bulunamadı.")
    
print("\n")


print("="*30)
print("BÖLÜM 4: TAM YAPI (try - except - else - finally)")
print("="*30)

# 'else' -> try bloğunda HİÇ hata oluşmazsa çalışır.
# 'finally' -> Hata olsa da olmasa da HER ZAMAN çalışır.

try:
    # Test etmek için 3 senaryoyu deneyin:
    # 1. Başarılı: "10" girin (else çalışacak)
    # 2. ValueError: "beş" girin (except ValueError çalışacak)
    # 3. ZeroDivisionError: "0" girin (except ZeroDivisionError çalışacak)
    
    sayi_str = input("Bölüm 4 için bir sayı girin (örn: 10, 0, veya 'beş'): ")
    sayi = int(sayi_str)
    sonuc = 100 / sayi # Burası hem ValueError hem ZeroDivisionError verebilir

except ValueError:
    # YAKALA (Eğer harf girerse)
    print("!!! HATA (Bölüm 4): Bu bir sayı değildi.")

except ZeroDivisionError:
    # YAKALA (Eğer 0 girerse)
    print("!!! HATA (Bölüm 4): Bir sayıyı 0'a bölemezsiniz.")

except Exception as e:
    # YAKALA (Beklenmedik diğer tüm hatalar için)
    # 'as e' -> Hatanın detayını 'e' değişkenine atar
    print(f"!!! Beklenmedik bir hata oluştu: {e}")

else:
    # HATA OLMAZSA (try bloğu başarıyla biterse)
    print(f"İşlem başarılı. Sonuç: {sonuc}")

finally:
    # HER ZAMAN (Hata olsa da olmasa da, 'else' çalışsa da çalışmasa da)
    print("--- Hata yönetimi bloğu (Bölüm 4) sona erdi ---")


print("\n>>> TÜM KOD BİTTİ. Program çökmeden sonuna kadar ulaştı! <<<")