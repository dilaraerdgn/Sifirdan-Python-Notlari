liste=[1,2,3,4,5,6]
a="araba"
# len() biliyoruz zaten
print(a.startswith("a")) #a stringi a harfi ile mi başlıyor bunu true veya false döndürerek görebiliyoruz
print(a.endswith("b"))  #bitiyor mu

a = a.replace("a","o") # a stringinde bulunan a karakterlerini o ile değiştirir
print(a)

liste.append("python")  # listenin en sonuna python ekler
print(liste)

liste.pop() #içine bişey vermezsek direkt listenin son elemanını çıkarır
print(liste)

liste.pop(0) #içine 0. indeksi verdik, 0.indeksi atar
print(liste)