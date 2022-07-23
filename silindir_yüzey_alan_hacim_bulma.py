import math as m # math kütüphanesini artık m takma ismiyle çağırabilirim

print("silindir yüze alan ve hacim bulan programa hoşgeldiniz")
yükseklik=float(input("yükseklik: "))
yarıçap=float(input("yarıçap: "))

#yüzey alanı = S
S=(yarıçap*yarıçap*m.pi*2)+(2*m.pi*yarıçap*yükseklik)
#hacim=V
V=m.pi*m.pow(yarıçap,2)*yükseklik # pow=üs alan fonksiyondur

print("yüzey alan: ",S,"hacim: ",V)