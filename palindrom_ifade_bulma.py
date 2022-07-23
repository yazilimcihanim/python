#palindrom=1221 kek yay  232

while True:
    metin=input("metin giriniz:")
    ters=metin[::-1]
    if metin=="dur":
        print("program sonlandı")
        break
    if metin==ters:
        print("palindromdur")
    else:
        print("palindrom değildir")