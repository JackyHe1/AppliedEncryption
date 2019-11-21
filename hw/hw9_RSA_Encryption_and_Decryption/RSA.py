import math

# open files
input_file = open("input.txt", "r")
# get nums from file
p = int(input_file.readline().strip('\n'))
q = int(input_file.readline().strip('\n'))
e = int(input_file.readline().strip('\n'))
N = p * q
chunk_size = len(str(N))

# m is almost 5 times of size of pq
m = 'We are slowly getting a better handle on the next roller coaster ride heading to Texas. A strong cold front will ' \
    'move through the state on Thursday, arriving in Central Texas by Thursday night.I think we are dry by Friday, but ' \
    'temperatures will be about thirty degrees cooler with highs near 50 under the ' \
    'clouds on Friday. Overnight lows could approach a light freeze in some spots by Friday night.' \
    'Overall rainfall projections are staying modest with a quarter to half inch of rain possible as the front' \
    'moves through. Those numbers will need some tweaking, and hopefully we can bump them up some to help with the ' \
    'still severe drought across the area.'


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


def gcd(a, b):
    while b:
        a, b = b, a%b
    return a


def findD(a, b, c):
    i = 1
    while True:
        if (i * b + c) % a == 0:
            break
        i = i + 1
    return (i * b + 1) / a


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


# to delete
m = 'hi'
p = 1223
q = 1987
e = 948047
N = 2430101

# ------------------------------- start encryption ---------------------------
# check if gcd(c, seta) == 1
if gcd(e, (p - 1) * (q - 1)) != 1:
    print('not valid, gcd(c, seta) != 1')

# RSA encryption
m_int = msg2int(m)

# get c
c = cal(m_int, e, N)
print('c = ', c)


# RSA Decryption
seta = (p - 1) * (q - 1)
d = findD(e, seta, 1)
print('seta=', seta, '  e=',e)
print('d=', d)
print('d2 = ', cal(e, seta - 2, seta))

# decrypt message
print('c=', c)
message = int2msg(cal(c, d, N))
print('Decrypted Message = ', message)
