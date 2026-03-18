i=0
while (i<10):
    if i==5:
        break #döngüyü sonlandırır
    print("i:",i)
    i +=1

k=0
while (k<10):
    if k==3 or k==5:
        k +=1   #k hep 3'te kalacağı için sonsuz döngüde kalır o yüzden bunu yazdık
        continue # döngünün başına git, alttaki işlem yapılmaz
    print("k:",k)
    k +=1