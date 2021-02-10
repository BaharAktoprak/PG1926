i=0
len=int(input("Kaç eleman girmek istersiniz:"))
sayilar=[]
ysayilar=[]
z=0
while i<len:
    i+=1
    sayi=int(input())
    if sayi==0:
        sayilar.insert(z,sayi)
        z+=1
    else:
        sayilar.append(sayi)
print(sayilar)
