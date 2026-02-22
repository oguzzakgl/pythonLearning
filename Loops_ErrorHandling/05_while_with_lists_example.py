# Konu: While Döngüsü Örneği (Aralıktaki Çift Sayılar)
# Amaç: Kullanıcıdan alınan aralıktaki çift sayıları while döngüsü ile bulup yazdırmak.

# Kullanıcıdan aralığın başlangıç değerini al ve 'int' (tam sayı) tipine dönüştür.
start_number = int(input("Başlangıç sayısını girin: "))
# Kullanıcıdan aralığın bitiş değerini al ve 'int' (tam sayı) tipine dönüştür.
end_number = int(input("Bitiş sayısını girin: "))

# Bir 'while' döngüsü başlat. 
# Bu döngü, 'start_number' değişkeni 'end_number' değişkenine eşit veya ondan küçük olduğu sürece devam eder.
while (start_number <= end_number):
    
    # 'if' (eğer) bloğu: 'start_number'ın 2'ye bölümünden kalanın 0 olup olmadığını kontrol et.
    # Kalan 0 ise, bu sayının 'çift sayı' olduğu anlamına gelir.
    if start_number % 2 == 0:
        
        # Eğer sayı çift ise, sayıyı ekrana yazdır.
        # 'end=" "' parametresi, bir sonraki 'print' işleminin yeni bir satıra değil,
        # aynı satıra bir boşluk bırakarak devam etmesini sağlar.
        print(start_number, end=" ")
        
    # Bu satır 'if' bloğunun DIŞINDA, ama 'while' döngüsünün İÇİNDEDİR.
    # Sayı ister tek ister çift olsun, her döngü adımında 'start_number'ı 1 artırır.
    # Bu, döngünün sonsuza kadar sürmesini engeller ve aralıktaki bir sonraki sayıya geçmemizi sağlar.
    start_number += 1