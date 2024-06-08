def encyption(cin):
    listt = []
    for i in cin:
     listt.append(ord(i)+12)  

    encoder = ""

    for val in listt:
     encoder = encoder + chr(val)

    return str(encoder)


# a = input("Enter a string to encrypt: ")

# res = encyption(a)

# print(res)











