def bolenler(sayi):
     liste=[]
     for tara in range(1,sayi):
         if (sayi%tara==0):
             liste.append(tara)
     return sum(liste)

sayi=int(input("sayi giriniz: "))
print("bölenlerin toplamı:",bolenler(sayi))