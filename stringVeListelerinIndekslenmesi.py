a="Python"
b=[1,2,3,4,5,6,7]
print(a[0])
print(a[2])
print(len(a))
print(len(b)) #kaç tane eleman olduğunu söyler
print(a[len(a) - 1])
print(a[0:2]) #0. indeksten başla 2. indekse kadar git, 2.indeks dahil değil
print(a[2:]) #2. indeksten başla ve sonuna kadar git
print(a[:4]) #baştan başla ve 4.indekse kadar git
print(b[0:6:2]) #0dan başla 6.indekse kadar git ama 2şer atlayarak git
print(b[::2]) #baştan sona kadar git ama 2 atlarak git

sozluk={"Elma":3,"Armut":4,"Kiraz":5}
print(sozluk["Kiraz"]) #kiraza karşılık gelen değeri döndürür