from functions import operations, eccproperties
import random
from tinyec import registry
a = 5829
b = 2079
p = 6277101735386680763835789423207666416083908700390324961279
private_key_A = 7487
private_key_B = 6737
G = [2436, 4951]
radom_integer = random.randint(
    0, 6277101735386680763835789423207666416083908700390324961279)
txt = input("Enter some text : ")


# Encryption
asciiCoded = operations.txt2ascii(txt)
pairLength = len(operations.toDigits(p, 65536))-1
groupList = operations.grouping(asciiCoded, pairLength)
bigInt = operations.bigInteger(groupList)
cipherPair = operations.grouping(bigInt, 2)
cx1 = eccproperties.double_and_add(radom_integer, G, p, a)  # first half of ciphertxt
pkey = eccproperties.double_and_add(private_key_B, G, p, a)
lamxp = eccproperties.double_and_add(radom_integer, pkey, p, a)
cx2 = []  # second half of cipher text
for i in cipherPair:
    cx2.append(eccproperties.ecc_add(i[0], i[1], lamxp[0], lamxp[1], p, a))
print("\nEncrypted msg : " + str([cx1, cx2]))
print("\n")


# Decryption
l2 = eccproperties.double_and_add(private_key_B, cx1, p, a)
Cipher = []  # pm
for i in cx2:
    Cipher.append(eccproperties.ecc_add(i[0], i[1], l2[0], -l2[1], p, a))
sml_Int = []
for i in Cipher:
    for j in i:
        sml_Int.append(operations.toDigits(j, 65536))
Dicipher = ""
for i in sml_Int:
    for j in i:
        Dicipher = Dicipher + chr(j)
print("decrypted msg : " + str(Dicipher))
