# while dongusu
# kosul false olana kadar calisir
# Dikkat Edilmesi Gereken: En önemli nokta, koşulun bir 
# noktada False olmasını sağlamaktır. Aksi takdirde 
# sonsuz döngüye girersiniz ve program kilitlenir. 
# Bu genellikle bir "sayaç" değişkeni ile yapılır.
sayac = 0

while sayac < 5:
    print(f"suan sayac {sayac}")
    sayac += 1 

print("dongu bitti")

# listelerle while kullanımı

meyveler = ["elma", "armut", "kiraz"]
i = 0

while i < len(meyveler): # i değeri listenin uzunluğundan kücük oldugu surece calisir
    print(meyveler[i])
    i += 1

print("-----------------------------------------------------") 

# for dongusu

# for döngüsü, bir koleksiyondaki (liste, tuple, string, set, dict veya range()) 
# her bir eleman için kod bloğunu çalıştırır.
# while gibi bir kosula bakmaz bunun yerine koleksiyondaki elemanlar bitene kadar devam eder
# Listeler, sözlükler gibi veri yapılarının üzerinde gezinmek (iterate) için en çok tercih edilen döngü tipidir.

meyveler = ["elma", "armut", "kiraz"]

# 'meyve' değişkeni her döngüde sırayla "elma", "armut" ve "kiraz" olur
for meyve in meyveler:
    print(meyve.capitalize()) # capitalize() ilk harfi büyük yapar

# Çıktı:
# Elma
# Armut
# Kiraz

# range ile for kullanımı

# range(5) -> [0, 1, 2, 3, 4] sayılarını üretir
for i in range(5):
    print(i) # 0'dan 4'e kadar yazdırır

# range(1, 6) -> 1'den başla, 6'ya kadar (6 hariç) [1, 2, 3, 4, 5]
for sayi in range(1, 6):
    print(sayi)

print("-----------------------------------------------------") 

# try except ile hata yönetimi

# try-except bloğu, kodumuzun bu beklenmedik hatalar 
# yüzünden çökmesini (crash) engeller ve hatayı "yakalamamızı" sağlar.

#try: Hata çıkarabilecek riskli kodu bu bloğun içine yazarız.

# except: Eğer try bloğunda bir hata olursa, program çökmek yerine except 
# bloğuna atlar ve oradaki kod çalışır.

try:
    # 1. Riskli kodu deniyoruz
    yas_str = input("Lütfen yaşınızı girin: ")
    yas_int = int(yas_str) # Hata burada çıkabilir! (Kullanıcı "abc" girerse)
    
    print(f"Siz {yas_int} yaşındasınız.")
    print(f"10 yıl sonra {yas_int + 10} yaşında olacaksınız.")

except ValueError:
    # 2. Eğer 'int()' dönüşümünde 'ValueError' hatası çıkarsa burası çalışır
    print("Hata: Lütfen harf değil, sadece sayı giriniz.")
except ZeroDivisionError:
    # 3. Başka bir hata türünü de yakalayabilirsiniz
    print("Hata: Sayıyı sıfıra bölemezsiniz.")
except:
    # 4. (Genel) Beklemediğiniz diğer tüm hatalar için
    print("Beklenmedik bir hata oluştu.")

print("Program kapanmadı, çalışmaya devam ediyor...")