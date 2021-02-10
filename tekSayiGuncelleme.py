len=int(input("Kaç eleman girmek istersiniz"))
i=0
z=0
liste=[]
while i<len:
    sayi=int(input())
    i+=1
    liste.append(sayi)
maxNumber=liste[0]
while z<len:
    if(maxNumber<liste[z])and (liste[z]%2==1):
        maxNumber=liste[z]
        z+=1
    else:
        z+=1
print(f"Listenin en büyük tek sayısı {maxNumber}")


