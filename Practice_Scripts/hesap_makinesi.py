# Gelişmiş Hesap Makinesi (Loglama Özellikli)
import math

islem_gecmisi = []

def Toplama(*args):
    sonuc = sum(args)
    islem_gecmisi.append(f"Toplama: {args} = {sonuc}")
    return sonuc

def Cikarma(a, b):
    sonuc = a - b
    islem_gecmisi.append(f"Cikarma: {a} - {b} = {a - b}")
    return sonuc

def Carpma(*args):
    sonuc =  math.prod(args)
    islem_gecmisi.append(f"Carpma: {args} = {math.prod(args)}")
    return sonuc

def Bolme(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError
        sonuc = a / b
        islem_gecmisi.append(f"Bölme: {a} / {b} = {sonuc}")
        return sonuc
    except ZeroDivisionError:
        hata_mesaji = "Hata: Bir sayı sıfıra bölünemez."
        islem_gecmisi.append(f"Bölme: {a} / {b} = {hata_mesaji}")
        return hata_mesaji
    

def Faktoriyel(n):
    try:
        n_int = int(n) 
        
        if n_int != n:
             raise ValueError 
        
        if n_int < 0:
            raise ValueError("Negatif sayı.")

        sonuc = math.factorial(n_int)
        islem_gecmisi.append(f"Faktöriyel: {n_int}! = {sonuc}")
        return sonuc
        
    except ValueError:
        hata_mesaji = "Hata: Faktöriyel için negatif olmayan tam sayı beklenir."
        islem_gecmisi.append(f"Faktöriyel: {n}! = {hata_mesaji}")
        return hata_mesaji  

def GecmisGoster():
    if not islem_gecmisi:
        return "İşlem geçmişi boş."
    return "\n".join(islem_gecmisi)



while True:
    print("\nHesap Makinesi")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("5. Faktöriyel")
    print("6. İşlem Geçmişi")
    print("7. Çıkış")

    secim = input("Bir işlem seçin (1-7): ")

    if secim == '7':
        print("Hesap makinesi kapatılıyor. Güle güle!")
        break
    
    elif secim == '6':
        print("\n--- İŞLEM GEÇMİŞİ ---")
        print(GecmisGoster())
    
    elif secim in ['1', '2', '3', '4', '5']:
        
        try:
            sonuc = None
            
            if secim in ['1', '3']:
                sayi_str = input("Sayıları virgülle ayırarak girin (Örn: 5,10,2): ")
                sayilar = [float(s.strip()) for s in sayi_str.split(',')]
                
                if secim == '1':
                    sonuc = Toplama(*sayilar)
                else:
                    sonuc = Carpma(*sayilar)
            
            elif secim in ['2', '4']:
                a = float(input("İlk sayıyı (a) girin: "))
                b = float(input("İkinci sayıyı (b) girin: "))
                
                if secim == '2':
                    sonuc = Cikarma(a, b)
                else:
                    sonuc = Bolme(a, b)

            elif secim == '5':
                n = float(input("Faktöriyelini almak istediğiniz sayıyı girin: "))
                sonuc = Faktoriyel(n)
            
            if sonuc is not None and not (isinstance(sonuc, str) and "Hata" in sonuc):
                 print(f"\nİşlem Başarılı. SONUÇ: {sonuc}")
            elif isinstance(sonuc, str) and "Hata" in sonuc:
                 print(f"\n{sonuc}")

        except ValueError:
            print("\nHata: Geçersiz sayı formatı. Lütfen sayısal değerler girin.")
        except Exception as e:
            print(f"\nBeklenmedik bir hata oluştu: {e}")
            
    else:
        print("Geçersiz seçim. Lütfen 1 ile 7 arasında bir sayı girin.")