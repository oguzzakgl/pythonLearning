# --- Örnek 2: Parola Sorma Ekranı ---

# Doğru parolayı belirliyoruz
dogru_parola = "12345"

# 1. Koşul: 'while True' bilerek sonsuz bir döngü başlatır.
# Bu döngüden çıkmanın tek yolu 'break' komutudur.
while True:
    
    girilen_parola = input("Lütfen parolanızı giriniz: ")
    
    # 2. Çıkış Kontrolü:
    if girilen_parola == dogru_parola:
        # Eğer girilen parola doğruysa...
        print("Giriş başarılı! Hoş geldiniz.")
        
        # 3. Döngüyü Kırma: 'break' komutu döngüyü anında sonlandırır.
        break
    else:
        # Eğer parola yanlışsa...
        print("Parola hatalı! Lütfen tekrar deneyin.")
        # Döngü 'break' komutuna ulaşmadığı için en başa döner.

print("Program sona erdi.")