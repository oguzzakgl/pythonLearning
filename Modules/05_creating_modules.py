# Konu: Modül Oluşturma ve Çağırma
# Amaç: Kendi modülümüzü (my_module) oluşturup başka bir dosyada kullanmak.

import my_module as m
# from my_module import greeting
# greeting ile dogrudan fonksiyona erişebiliriz
print(m.number)

print(m.greeting("Oğuz"))

print(f"name: {m.person['name']}")