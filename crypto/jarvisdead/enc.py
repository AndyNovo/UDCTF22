#!/usr/bin/env sage

try:
    with open("flag.txt", 'rb') as file:
        FLAG = file.read()
        FLAG = int.from_bytes(FLAG, 'big')
except Exception as e:
    print(e)
    exit()

constants = [0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b]

n = 303
rounds = 4
K = GF(2^n, "a")
K.inject_variables()

def encrypt(p, k, r):
    p = (p + k) ^ 3
    for i in range(0, r):
        p = (p + k + constants[i]) ^ 3
    p = p + k
    return p

key = K.random_element()
# print("key=", key.integer_representation())
plaintext = K.random_element()
print("plaintext=", plaintext.integer_representation())
ciphertext = encrypt(plaintext, key, rounds)
print("ciphertext=", ciphertext.integer_representation())
cipherflag = encrypt(K.fetch_int(FLAG), key, rounds)
print("encrypted_flag=", cipherflag.integer_representation())
#plaintext= 9602140981710252221694284230904298893361278924232497822433432074996923308941917819732065189
#ciphertext= 8546470156243784005122895379912338712106607998851570193903315952129674486027849847614186710
#encrypted_flag= 882197250993409532403476557109065048801215346217931399142598807562498231306543530723470090
