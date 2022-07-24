
#yazilimci.hanim
def unlu_sayisi_bul(metin="",sayi=0):
    unlu_harfler="euıüaiöo"
    for tara in metin:
        if tara in unlu_harfler:
            sayi+=1
    return sayi

while True:
    metin=input("sesli harfleri bulmak istediğiniz metini girinizi:")
    if metin=="dur":
        print("program sonlandı")
        break
    print(unlu_sayisi_bul(metin))

