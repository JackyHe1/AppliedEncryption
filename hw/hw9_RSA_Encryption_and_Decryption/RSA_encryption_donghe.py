import math

# open files
input_file = open("input.txt", "r")
# get nums from file
p = int(input_file.readline().strip('\n'))
q = int(input_file.readline().strip('\n'))
e = int(input_file.readline().strip('\n'))
N = p * q


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


def wrap(m, w):
    # split message m into different parts based on length w
    return [m[i:i + w] for i in range(0, len(m), w)]


# fast-power  O(logN) time
def fastPower(g, p, MOD):
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


# according to extended euclidean algorithm, we try to find a solution for aX + bY = gcd(a, b)
# assume we have a solution X1, Y1, then we have aX1 + bY1 = gcd(a, b)
# assume we have another bX2 + (a % b)Y2 = gcd(b, (a % b))
#  according to gcd, we know that gcd(a, b) = gcd(b, (a % b))
# then we will have aX1 + bY1 = bX2 + (a % b)Y2 => aX1 + bY1 = bX2 + (a - [a / b] * b)Y2
# then we get: aX1 + bY1 = aY2 + b(X2 - [a/b]Y2)
# so we know X1 = Y2, Y1 = X2 - [a/b]Y2, then we can use iteration to solve this
# cite http://anh.cs.luc.edu/331/notes/xgcd.pdf
def extend_gcd(e, seta):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1

    temp_seta = seta

    while e > 0:
        temp1 = temp_seta / e
        temp2 = temp_seta - temp1 * e
        temp_seta = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_seta == 1:
        return d + seta


def encrypt(public_key, message):
    key, n = public_key
    # split based on pq, get 506 bits, and then /8, get length
    m_arr = wrap(message, int(math.log(n, 2)) // 8)
    m_int_list = [msg2int(m) for m in m_arr]
    ciphers = [fastPower(m_int, key, n) for m_int in m_int_list]
    return ciphers


def decrypt(decrypt_key, ciphertextArr):
    key, n = decrypt_key
    return [int2msg(fastPower(ciphertext, key, n)) for ciphertext in ciphertextArr]


# get public key
public_key = (e, N)


# ------------------------------------- Bob ----------------------------
# m is a long message, we will split this message and generate many Cs
m = 'We are slowly getting a better handle on the next roller coaster ride heading to Texas. A strong cold front will ' \
    'move through the state on Thursday, arriving in Central Texas by Thursday night.I think we are dry by Friday, but ' \
    'temperatures will be about thirty degrees cooler with highs near 50 under the ' \
    'clouds on Friday. Overnight lows could approach a light freeze in some spots by Friday night.' \
    'Overall rainfall projections are staying modest with a quarter to half inch of rain possible as the front' \
    'moves through. Those numbers will need some tweaking, and hopefully we can bump them up some to help with the ' \
    'still severe drought across the area.'

print("Original Message = ", m)

# get ciphers and print it--------send cipher text to Alice
ciphers = encrypt(public_key, m)
print("Ciphers = ", ciphers)

# --------------------------------------Alice----------------------------
# calculate seta = (p - 1) * (q - 1)
seta = (p - 1) * (q - 1)

# calculate d
d = extend_gcd(e, seta)
print('d =', d)

decrypt_key = (d, N)

# get decrypted message
decryptedMsg = decrypt(decrypt_key, ciphers)
print('Decrypted Message = ', decryptedMsg)
print('Joined Message = ', ''.join(decryptedMsg))
