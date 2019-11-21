
# open files
input_file = open("input.txt", "r")

# get two nums from two lines
p = int(input_file.readline().strip('\n'))
g = int(input_file.readline().strip('\n'))
b = int(input_file.readline().strip('\n'))
A = int(input_file.readline().strip('\n'))
ciphertextStr = input_file.readline().strip('\n')
ciphertext = int(ciphertextStr)

# fast-power  O(logN) time
def cal(g, p, MOD):
    # base num is a
    # result is b
    a = g
    b = 1
    while(p > 0):
        # fast power
        # do mod every time

        # if p is odd, we should multiple a single base num a to result
        if p % 2 == 1:
            b = b * a % MOD
        # do a^2 to reduce time to compute b by multipling b every time
        a = a ** 2 % MOD
        p = int(p / 2)
    return b % MOD


# for binaryTxt, get 8 binary digits and transfer them to char every round
def binary_to_alpha(binary_str):
    # every time, substring eight digits binary and transfer it to num
    # then transfer num to ascii char
    origin_str = binary_str
    result = ""
    while origin_str != "":
        i = chr(int(origin_str[0:8], 2))
        result = result + i
        origin_str = origin_str[8:]
    return result


def bin2msg(binary):
    return ''.join(chr(int(binary[(i*8):(i*8 + 8)],2)) for i in range(len(binary)//8))

print("g = ", g, " ,p = ", p)

Alice_pub_key = A
print("Alice public key = ", Alice_pub_key)

Bob_pub_key = cal(g, b, p)
print("Bob public key = ", Bob_pub_key)

Bob_pri_key = cal(A, b, p)
print("Bob private = ", Bob_pri_key)

Bob_pri_key_binaryStr = '{0:08b}'.format(Bob_pri_key)
print ("Bob_pri_key_binaryStr", Bob_pri_key_binaryStr)
print ("ciphertext            ", ciphertext)
i = len(Bob_pri_key_binaryStr) - 1
res = ""
while i >= 0:
    ciphertext_digit = ciphertext % 10
    ciphertext = ciphertext / 10

    if (Bob_pri_key_binaryStr[i] == '1' and ciphertext_digit == 1)\
            or (Bob_pri_key_binaryStr[i] == '0' and ciphertext_digit == 0):
        res = '0' + res

    else:
        res = '1' + res
    i = i - 1


def bin2msg(binary):
    return ''.join(chr(int(binary[(i*8):(i*8 + 8)],2)) for i in range(len(binary)//8))

binary = bin(int(res, 2))