import random

# open files
input_file = open("input.txt", "r")

# get two nums from two lines
bit_len = int(input_file.readline().strip('\n'))


def gcd_fun(a, b):
    if b == 0:
        return a
    else:
        return gcd_fun(b, a % b)


# fast-power  O(logN) time
def fast_power(g, p, MOD):
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


def miller_rabin(num, k = 2):
    if num % 2 == 0:
        return False
    # generate a random a
    a = random.randint(1, num)

    # if gcd is not 1, return false
    if gcd_fun(a, num) != 1:
        return False

    # calculate q
    q = (num - 1) / int(pow(2, k))

    # get a0
    ai = fast_power(a, q, num)

    if ai == 1 or ai == -1:
        return True

    for i in range(0, k):
        print('ai = ', ai)
        if ai == -1 % num:
            return True
        ai = fast_power(ai, 2, num)
    return ai == -1

import datetime
# get maximum possible value when given a bit length


# use current time to generate random number
def getRandomWithRange(min_val, max_val):
    a = datetime.datetime.now()
    h = a.hour
    m = a.minute
    s = a.second
    ms = a.microsecond
    # we can multiple hour, min, second, microsecond to then do mod and add base number
    return min_val + ((h + 1) * (m + 1) * (s + 1) * (ms + 1) % (max_val - min_val))


# generate random num to check
max_res = 2 ** bit_len - 1
min_res = 2 ** (bit_len - 1) + 1
rand_num = getRandomWithRange(min_res, max_res)


# keep generating new number util miller_rabin return true
while not miller_rabin(rand_num):
    print('rand_num=', rand_num)
    rand_num = getRandomWithRange(min_res, max_res)

# print result
print (rand_num)



