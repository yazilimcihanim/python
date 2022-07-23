def olumsuz_karakter(string):
    if len(string)>0 and  "değil" in string:
        return "bencede "+string
    return string + " değil"

kelime=input("karakter analizinizi girinizi:")
print(olumsuz_karakter(kelime))