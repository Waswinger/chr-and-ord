"""" chr = şifreli hale döndürür
     ord = değeri alır
""" 
def sifrele(metin):
    a = ""
    for a in metin:
        a = a+chr(ord(a)+3) 
    print(f"Şifrelenmiş hali {a}")
    return a

def sifrecoz(metin):
    b = ""
    for b in metin:
        b = b+chr(ord(b)-3) 
    print(f"Çözülmüş hali {b}")
    return b

metin = input("Şifre giriniz: ")

sifrelenmis= sifrele(metin) 
sifrecoz(sifrelenmis) 


    