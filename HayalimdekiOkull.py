class okul:
    def __init__(self,calisanSayisi,sinifSayisi,toplamOgrenciSayisi,okulTuru,ogretmenSayisi):
     self.calisanSayisi = calisanSayisi
     self.sinifSayisi = sinifSayisi
     self.toplamOgrenciSayisi = toplamOgrenciSayisi
     self.okulTuru= okulTuru
     self.ogretmenSayisi=ogretmenSayisi
     
    def bilgileriGoster(self):    
        print("Bu okulda calisanlarin sayisi: "+self.calisanSayisi)
        print("Bu okuldaki sinif Sayisi: "+self.sinifSayisi)
        print("Bu okuldaki toplam öğrenci sayısı: "+self.toplamOgrenciSayisi)
        print("Bu okulun türü: "+self.okulTuru)
        print("Bu okuldaki öğretmenlerin sayısı: "+self.ogretmenSayisi)


okull=okul("12","21","150","ilkokul","3")
okull.bilgileriGoster()

class ikinciOkul(okul):
    pass
y = ikinciOkul("2","3","200","ortaokul","4")
y.bilgileriGoster()  
       
class ucuncuOkul(okul):
    pass
z = ucuncuOkul("4","5","100","lise","5")
z.bilgileriGoster()  
       
    