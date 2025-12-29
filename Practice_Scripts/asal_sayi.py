# Sayı girişi
input_number = int(input("Bir sayı girin: "))

# Bulunan asal sayıları saklamak için boş bir liste oluştur
prime_numbers = []

# Girilen sayının negatif olup olmadığını kontrol et
if(input_number < 0):
    # Negatif sayılar için asal sayı kontrolü yapmıyoruz
    print("Negatif sayıların asal olup olmadığını kontrol edemem.")
else:
    # Sayı 0 veya daha büyükse işleme başla
    
    # 2'yi elle ekle
    prime_numbers.append(2)

    # Tek sayıları kontrol et
    for i in range(3, input_number + 1, 2):
        
        # Bölen kontrolü (kareköküne kadar)
        for j in range(3, int(i**0.5) + 1, 2):
            
            # Eğer 'i' sayısı, 'j' sayısına tam bölünüyorsa (kalan 0 ise)
            if i % j == 0:
                break
        
        else:
            # Sayı asaldır, listeye ekle
            prime_numbers.append(i)
            
    # Tüm döngüler bittikten sonra, toplanan asal sayıları ekrana yazdır
    print(f"{input_number} sayısına kadar olan asal sayılar: {prime_numbers}")