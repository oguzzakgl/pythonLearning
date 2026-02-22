# Konu: Lambda Fonksiyonları
# Amaç: İsimsiz (lambda) fonksiyonların tanımlanması ve map(), filter() ile kullanımı.

# Lambda Fonksiyonu (İsimsiz ve Tek İfadeli Fonksiyon)
# ------------------------------------------------------------------------------------------------------
# square adında bir normal fonksiyon tanımlanır (Yorum satırında bırakıldı, Lambda ile eşdeğerdir).
# def square(number): return number ** 2 

# Lambda ile square fonksiyonunun tek satırlık ve isimsiz hali tanımlanır.
square = lambda num: num ** 2

numbers = [1,3,5,9,10,4] # Üzerinde işlem yapılacak liste.


# 1. map() ile normal fonksiyon kullanımı: 'square' fonksiyonu listenin her elemanına uygulanır.
result_map_func = list(map(square, numbers))
print(f"1. Map (Normal Fonksiyon) Sonucu: {result_map_func}")

# 2. map() ile Lambda kullanımı: İsimsiz Lambda fonksiyonu listenin her elemanına uygulanır.
result_map_lambda = list(map(lambda num: num ** 2, numbers))
print(f"2. Map (Lambda) Sonucu: {result_map_lambda}")

# 3. Direkt Lambda çağrısı: 3'ün karesi hesaplanır.
result_square_call = square(3)
print(f"3. Lambda Direkt Çağrı Sonucu: {result_square_call}")

# 4. map() sonucunu döngü ile yazdırma: map objesi tek tek gezilir.
print("4. Map Objesi Üzerinde Döngü Sonucu:")
for item in map(square, numbers):
    print(item)


# Filter Fonksiyonu
# ------------------------------------------------------------------------------------------------------
# check_even adında Lambda fonksiyonu: Bir sayının çift olup olmadığını (True/False) kontrol eder.
check_even = lambda num: num%2==0

# 5. filter() ile normal fonksiyon kullanımı: check_even (lambda) fonksiyonu listenin çift sayılarını filtreler.
result_filter_func = list(filter(check_even, numbers))
print(f"5. Filter Sonucu (Lambda ile): {result_filter_func}")

# 6. filter() ile isimsiz Lambda kullanımı: Aynı filtreleme işlemi.
result_filter_lambda = list(filter(lambda num: num%2==0, numbers))
print(f"6. Filter Sonucu (İsimsiz Lambda ile): {result_filter_lambda}")

# 7. Lambda fonksiyonunun doğrudan bir liste elemanına uygulanması.
# numbers[2] = 5. 5 % 2 == 0 koşulu kontrol edilir.
result = check_even(numbers[2]) 

# Sonuç: 5 çift olmadığı için False döner.
print(f"7. check_even(numbers[2]) Sonucu: {result}")