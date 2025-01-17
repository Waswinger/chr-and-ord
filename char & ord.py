"""" chr = şifreli hale döndürür
     ord = değeri alır
""" 
def sifrele(metin): # we created a function(encryption)
    a = "" # We created a variable of type string named a
    for a in metin: # we sent a into the metin
        a = a+chr(ord(a)+3) # encrypted
    print(f"Şifrelenmiş hali {a}") # We printed the encrypted version of the text entered by the user
    return a # we returned a

def sifrecoz(metin): # we created a function(decryption)
    b = "" # We created a variable of type string named b
    for b in metin: # we sent b into the metin
        b = b+chr(ord(b)-3) # decrypted
    print(f"Çözülmüş hali {b}") # We printed the decoded version of the text entered by the user
    return b # we returned b

metin = input("Şifre giriniz: ") # We received the text that the user wants to encrypt

sifrelenmis= sifrele(metin) # we encrypt the variable named text received from the user and synchronize it with the variable named sifrele
sifrecoz(sifrelenmis) # decrypting the text we encrypt


    