a=3
b=4

if a==3 and b==4:
    print("Evet")
else:
    print("Hayır")

if a==3 or b==5:
    print("Evet") #en az bir tanesi doğru ise ifin içine girer
else:
    print("Hayır")

if (not (3==4)): # not(false) =true yapar, yani ifin içine girer
    print("evet")