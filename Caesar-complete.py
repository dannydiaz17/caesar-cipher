import string

alphabet = list(string.ascii_lowercase)
decoded = list()
encrypted = list()

print("Caesar Cipher Decrypter-----------------------------------\n\n")

def init():
    global boolin
    boolin = str(input("Would you like to (e)ncrpyt a message?\nOr, (d)ecrypt one?\n\n"))
    print('\n')

init()
#print(boolin)

#Make Shifted List

def alphacs(shift):
    diff = int(26 - shift)
    #diff=difference
    global sl
    sl = alphabet [diff:26]

    for x in range(diff):
        sl.append(alphabet [x])
        #sl = Shifted list

def encrypt(message,shift):
    for i in range(len(message)):
        char = message[i]
        if char in alphabet:
            pos = alphabet.index(char)
            enchar = sl[pos]
            #enchar = Encrypted Character
            encrypted.append(enchar)
        else:
            otr = char
            #otr= Other
            encrypted.append(otr)

def decrypt(code,shift):
    for i in range(len(code)):
        char = code[i]
        if char in alphabet:
            pos = sl.index(char)
            dechar = alphabet[pos]
            #dechar = Decoded Character
            decoded.append(dechar)
        else:
            otr = char
            #otr= Other
            decoded.append(otr)

#Encrypt
if boolin in ("e", "encrypt"):
    message = str(input("Message to Encrypt\n\n"))
    shift = int(input("Shift?\n\n"))
    alphacs(shift)
    encrypt(message,shift)
    fencrypted = "".join(encrypted)
    print("Encrypted Message:" + fencrypted)

#Decrypt
elif boolin in ("d", "decrypt"):
    code = str(input("Encrypted Message\n\n"))
    shift = int(input("Shift?\n\n"))
    alphacs(shift)
    decrypt(code,shift)
    fdecoded = "".join(decoded)
    print("Decrypted Code:" + fdecoded)

else:
    print("invalid selection\n")
    init()
