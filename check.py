from encode import encyption
from decode import decryption

a = str(input("Enter any text: "))

ey = encyption(a)
print(f"after encrption : {ey}")

dy = decryption(ey)

print(f"after decryption : {dy}")

