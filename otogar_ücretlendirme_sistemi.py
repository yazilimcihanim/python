
print("\t menü \t \n 1.otobüs \n 2.taksi \n  \n ")

araba=int(input("giriş yapıcağınız arabanın türünü giriniz:"))

while True:
    if araba==1:
        print("araba ile giriş yapıldı ")
        saat=int(input("kaç saat kalıcak arabanız:"))
        if 0<saat<=3:
            ucret = (saat * 1.5)
            print(f"{saat} için ücret:{ucret} TL'dir ")
            break
        elif 3<saat<=6:
            ucret=(saat*2)
            print(f"{saat} için ücret:{ucret} TL'dir ")
            break
        else:
            ucret=(saat*3)
            print(f"{saat} için ücret:{ucret} TL'dir ")
            break
    elif araba==2:
        print("Taksi ile giriş yapıldı")
        saat = int(input("kaç saat kalıcak arabanız:"))
        break
        if 0<saat<=4:
            print(f"{saat} için ücret:{saat} TL'dir ")
            break
        elif 4<saat<=8:
            ucret=(saat*2)
            print(f"{saat} için ücret:{ucret} TL'dir ")
            break
        else:
            ucret=(saat*4)
            print(f"{saat} için ücret:{ucret} TL'dir ")
            break