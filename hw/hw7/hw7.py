# open files
input_file = open("input.txt", "r")

# get two nums from two lines
p = int(input_file.readline().strip('\n'))
g = int(input_file.readline().strip('\n'))
A = int(input_file.readline().strip('\n'))
a = int(input_file.readline().strip('\n'))

r = 4663
m = 'm'


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

c1 = cal(g, r, p)
c2 = bin2int(msg2bin(m)) * int(cal(A, r, p)) % p

f = open("output.txt", "w")
f.write(str(p) + '\n')
f.write(str(g) + '\n')
f.write(str(a) + '\n')
f.write(str(c1) + '\n')
f.write(str(c2))

# part 2: get message from Bob
message = cal(cal(c1, a, p), p - 2, p)  * c2 % p
print("message", message)

final_message = int2msg(message)
print("final message", final_message)

