# --- Yöntem 1: Standart 'for' Döngüsü (En Yaygın Yöntem) ---
# Bir tuple (veya liste) üzerinde döngü kurmanın en basit ve Python'a en uygun yoludur.
fruits = ("grape", "apple", "banana", "cherry")

# 'for' döngüsü, 'fruits' tuple'ındaki her bir elemanı sırayla 'item' değişkenine atar.
for item in fruits:
    print(item)  # Her döngüde o anki elemanı yazdırır.

# --- Yöntem 2: 'range(len())' ile 'for' Döngüsü (İndeks Gerektiğinde) ---
# Bu yöntem, elemanın kendisine ek olarak onun SIRA NUMARASINA (indeksine)
# ihtiyaç duyduğunuzda kullanılır.
numbers = (10, 20, 30, 40, 50)

# len(numbers) -> 5
# range(5) -> 0, 1, 2, 3, 4 sayılarını üretir
# 'num' değişkeni sırayla 0, 1, 2, 3, 4 değerlerini alır.
for num in range(len(numbers)):
    # numbers[num] -> numbers[0], numbers[1], vb. ile elemana erişiriz.
    print(f"Index {num} değer: {numbers[num]}")

# --- Yöntem 3: 'while' Döngüsü (Manuel Kontrol) ---
# 'while' döngüsü kullanmak için bir sayaç (indeks) değişkenini kendimiz yönetmeliyiz.
names = ("Ali", "Veli", "Ayşe", "Fatma")

# 1. Başlangıç indeksi (sayaç) tanımlanır.
i = 0
# 2. Koşul: Sayaç, tuple'ın uzunluğundan (len(names) -> 4) küçük olduğu sürece döner.
while i < len(names):
    # 'i' indeksindeki elemanı yazdırır (names[0], names[1], ...)
    print(names[i])
    # 3. ÖNEMLİ: Sayacı 1 artırırız.
    # Bu satır unutulursa, 'i' hep 0 kalır ve program SONSUZ DÖNGÜYE girer.
    i += 1