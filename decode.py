
def decryption(cin):
    listt = []

    for i in cin:
        listt.append(ord(i)-12)
    
    decoder = ""

    for val in listt:
        decoder = decoder + chr(val)

    return str(decoder)



# a = str(input("Enter the encypted text: "))

# res = decryption(a)

# print(res)




