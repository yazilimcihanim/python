import math as m
#ax^2+bx+c=0 için:

a=float(input("2. dereceden ki katsayıyı giriniz: "))
b=float(input("1. derecedeki katsayıyı giriniz: "))
c=float(input("sabit sayıyı giriniz: "))

delta=m.pow(b,2)-4*a*c
if(delta>0):
    x1=(-b-m.sqrt(delta))/2*a
    x2=(-b+m.sqrt(delta))/2*a
    print("iki farklı kök vardır x1=",x1,"x2=",x2)
elif(delta==0):
    x=b/2*a
    print("iki kök birbirinie eşittir: x1=x2=",x,)
else:
    print("reel kök yoktur")