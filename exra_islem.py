"""sayi=int(input("Faktöriyelini hesaplanacak sayi giriniz:"))
deger=1
for i in range(sayi):
    deger=deger*(i+1)
print("Faktoriyel:",deger)
"""
print("Yapmak istediğiniz işlemi seçiniz.('1' Toplam- '2'-Çıkarma- '3'-Çarpma- '4' Bölme)")

def Carp(x,y):
    carpma_sonucu=x*y
    return carpma_sonucu
def Bol(x,y):
    return x/y
def Topla(x,y):
    return x+y
def cikar(x,y):
    return x-y

secim=int(input("Seçim:"))



if secim==1:
    sayi1=int(input("1.sayi giriniz:"))
    sayi2=int(input("2.sayi giriniz:"))
    print("\n",sayi1,"+",sayi2,"=",Topla(sayi1,sayi2)) 
elif secim==2:
    sayi1=int(input("1.sayi giriniz:"))
    sayi2=int(input("2.sayi giriniz:"))
    print("\n",sayi1,"-",sayi2,"=",cikar(sayi1,sayi2))
elif secim==3:
    sayi1=int(input("1.sayi giriniz:"))
    sayi2=int(input("2.sayi giriniz:"))
    print("\n",sayi1,"*",sayi2,"=",Carp(sayi1,sayi2))
elif secim==4:
    sayi1=int(input("1.sayi giriniz:"))
    sayi2=int(input("2.sayi giriniz:"))
    print("\n",sayi1,"/",sayi2,"=",Bol(sayi1,sayi2))
else:
    print("1-2-3-4 birini secin:")

