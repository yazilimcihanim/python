while True:

      sayi_gir = input("Lütfen basamak sayısını merak ettiğiniz sayıyı giriniz:")

      if int(sayi_gir)==0:
             print("program sonlandı, iyi günler....")
             break
      if int(sayi_gir) > 0:
            print("Girilen sayının basamak sayısı:", len(sayi_gir))
      elif int(sayi_gir) == 0:
            print("Girilen sayının basamak sayısı:", 1)
      else:
            print("Girilen sayının basamak sayısı:", len(sayi_gir)-1)
            # negatif sayılar için
