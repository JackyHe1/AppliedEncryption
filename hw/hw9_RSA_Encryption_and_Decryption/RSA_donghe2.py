import math

# open files
input_file = open("input.txt", "r")
# get nums from file
p = int(input_file.readline().strip('\n'))
q = int(input_file.readline().strip('\n'))
e = int(input_file.readline().strip('\n'))
N = p * q

# m is almost 2 times of size of pq
m = 'We are slowly getting a better handle on the next roller coaster ride heading to Texas. A strong cold front will ' \
    'move through the state on Thursday, arriving in Central Texas by Thursday night.I think we are dry by Friday, but ' \
    'temperatures will be about thirty degrees cooler with highs near 50 under the '

#m = 'hi'
chunks = len(m)
chunk_size = len(str(N))


def msg2bin(message):
    return ''.join(['{0:08b}'.format(ord(x)) for x in message])


def bin2int(binary):
    return int(binary,2)


def int2bin(integer):
    binString=''
    while integer > 0:
        mod = integer % 2
        binString = str(mod)+binString
        integer //= 2
    while len(binString)%8 !=0:
        binString = '0' + binString
    return binString


def int2msg(integer):
    return bin2msg(int2bin(integer))


def bin2msg(binary):
    return ''.join(chr(int(binary[(i * 8):(i * 8 + 8)], 2)) for i in range(len(binary) // 8))


def msg2int(message):
    return bin2int(msg2bin(message))


def int2msg(integer):
    return bin2msg(int2bin(integer))


def fast_power(base, power):
    result = 1
    while power > 0:
        # If power is odd
        if power % 2 == 1:
            result = result * base

        # Divide the power by 2
        power = power // 2
        # Multiply base to itself
        base = base * base

    return result

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a


def extend_gcd(a, b):
    if b == 0:
        return 1,0,a
    x2, y2, remain = extend_gcd(b, a % b)

    x1 = y2
    y1 = x2 - a // b * y2

    return x1, y1, remain


def findD(a, b, c):
    i = 1
    while True:
        if (i * b + c) % a == 0:
            break
        i = i + 1
    return (i * b + 1) / a


def wrap(m, w):
    return [m[i:i + w] for i in range(0, len(m), w)]


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



def get_c_list(m_arr, e, N):
    #c_list = [cal(msg2int(m), e, N) for m in m_arr]
    c_list = []
    for m in m_arr:
        print('m=', m)
        m_int = msg2int(m)
        c = cal(m_int, e, N)
        c_list.append(c)
    print('c_list = ', c_list)
    return c_list


def get_decrypted_message(c_arr, p, q, N, e):
    seta = (p - 1) * (q - 1)
    # d = findD(e, seta, 1)
    d = extend_gcd(e, seta)[0]
    return [int2msg(cal(c, d, N)) for c in c_arr]


# # to delete
#m = 'We are slowly getting a better'
# p = 1223
# q = 1987
# e = 948047
# N = 2430101

def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi / e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi

seta = (p - 1) * (q - 1)
#d2 = extend_gcd(e, seta)[0]
d = multiplicative_inverse(e, seta)
#d3 = findD(e, seta, 1)
print('d =',d,  'd3=')
publicKey, privateKey = ((e, N), (d, N))


def fastPower(g,A,N):
    a=g
    b=1
    while A > 0:
        if A%2 == 1:
            b= (b*a)%N
        a = (a*a) % N
        #print (a)
        A = A//2
    return b

def encrypt(pk, plaintext):
    print('encrypt', plaintext)
    print('pk', pk)
    key, n = pk
    print('key =', key)
    cipher = [(fastPower(ord(char), key, n)) for char in plaintext]
    return cipher


def decrypt(pk, ciphertext):
    print('decrypt', ciphertext)
    print('pk', pk)
    key, n = pk
    plain = [chr(fastPower(char, key, n)) for char in ciphertext]
    return ''.join(plain)


c = encrypt(privateKey, m)
print('encryptedMsg', c)

decryptedMsg = decrypt(publicKey, c)
print('decryptedMsg', decryptedMsg)

# # ------------------------------- start RSA encryption ---------------------------
# # check if gcd(c, seta) == 1
# if gcd(e, (p - 1) * (q - 1)) != 1:
#     print('not valid, gcd(c, seta) != 1')
#
# # RSA encryption
# m_arr = wrap(m, len(str(p * q)))
# print('c_arr=', m_arr)
# c_arr = get_c_list(m_arr, e, N)
#
# print('cList:')
# print(c_arr)
#
# # ------------------------------- start RSA Decryption ---------------------------
# messageArr = get_decrypted_message(c_arr, p, q, N, e)
# print('Decrypted Message = ', messageArr)
