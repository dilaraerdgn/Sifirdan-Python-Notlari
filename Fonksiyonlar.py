def selamla(isim = "isimsiz"): #isim gönderilmezse isimsiz olarak çıkacak
    print("merhaba", isim)
    
def toplama(a,b,c):
    print("toplam", a+b+c)


def toplama2(a,b,c):
    return a+b+c

selamla("dilara")
selamla()
toplama(3,4,5)
toplam=toplama2(9,8,7)
print(toplam)  #print ile toplama fonk. değer ekrana yazdıramazdık çünkü return değil