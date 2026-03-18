class Account:
    def __init__(self,isim,numara,bakiye):  #self ->objem , init fonksiyon-> özelliklere değer vermemizi sağlar
        self.isim=isim
        self.numara=numara
        self.bakiye=bakiye
    
    
    def hesapBilgileri(self):
        print("isim:",self.isim)
        print("numara:",self.numara)
        print("bakiye:",self.bakiye)
    
    def paraCek(self,miktar):
        if (self.bakiye- miktar<0):
            print("bakiye yetersiz")
        else:
            self.bakiye -= miktar
            print("güncel bakiye:", self.bakiye)

    def paraYatir(self,miktar):
        self.bakiye += miktar
        print("güncel bakiye:",self.bakiye)

account= Account("Dilara Erdoğan",123456,1000)
account.hesapBilgileri()
account.paraCek(800)
account.paraYatir(500)

