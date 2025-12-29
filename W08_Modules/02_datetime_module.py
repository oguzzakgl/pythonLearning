# Konu: Datetime Modülü
# Amaç: Tarih ve saat işlemleri, zaman farkı hesaplama ve formatlama.

# import datetime
from datetime import datetime, timedelta, time, date

# result=dir(datetime)
# print(result)

result=datetime(2009,5,17,15,30,24)  # yıl, ay, gün
print(result)

my_date=datetime.now()   #şu anki tarih ve saat
print(my_date.day)  #gün
print(my_date.month)  #ay
print(my_date.year)   #yıl
print(my_date.hour)   #saat
print(my_date.minute)  #dakika
print(my_date.second)  #saniye

print(datetime.weekday(my_date))  #haftanın günü (0=pazartesi, 6=pazar)
print(datetime.ctime(my_date))  #tarih ve saati okunabilir formatta gösterir

date1=datetime(2020,1,1)
date2=datetime(2021,6,30)
difference=date2 - date1   #iki tarih arasındaki fark
print(difference.days)   #farkın gün cinsinden değeri
print(difference.seconds)  #farkın saniye cinsinden değeri


today=datetime.now()
future_date=today + timedelta(days=100)  #bugünden 100 gün sonrası
print(future_date)
past_date=today - timedelta(weeks=5)  #bugünden 5 hafta öncesi
print(past_date)


# donglerle tarih işlemleri

start_date=datetime(2025,1,1)
for item in range(14):
    print(start_date + timedelta(days=item))  #14 günün tarihleri


print(datetime.isocalendar(today))  #yıl, hafta numarası, haftanın günü

my_time=time(14,30,15)  #saat, dakika, saniye
my_date1=date(2023,12,25)  #yıl, ay, gün
combined=datetime.combine(my_date1, my_time)  #tarih ve saati birleştirir
print(my_time)
print(my_time.hour)   #saat
print(my_time.minute)  #dakika
print(my_time.second)  #saniye
print(combined)


updated_date=my_date1.replace(year=2024)  #tarihin yılını değiştirme
print(updated_date)
