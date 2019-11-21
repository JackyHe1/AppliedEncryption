import random

# open files
input_file = open("input.txt", "r")

# get two nums from two lines
bit_len = int(input_file.readline().strip('\n'))


# get greatest common divisor from two nums
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


def miller_rabin(num, k):
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

    # if a0 is 1 or -1, return true
    if ai == 1 or ai == -1:
        return True

    # iterate k time to check ai
    for i in range(0, k):
        print('ai = ', ai)
        # if -1 % num is ai, true
        if ai == -1 % num:
            return True
        # get next ai number to check
        ai = fast_power(ai, 2, num)
    return ai == -1


# generate random num to check
rand_num = random.getrandbits(bit_len)

# keep generating new number util miller_rabin return true
test_count = 5
k_val = 5
while True:
    allTrue = True
    # iterate test_count times test
    for i in range(0, test_count):
        # once failed, rand_num should not be result
        if not miller_rabin(rand_num, k_val):
            allTrue = False
            break
    # if all true, rand_num could be result
    if allTrue:
        break
    else:  # not all true, generate a new number to test
        rand_num = random.getrandbits(bit_len)

# print result
print (rand_num)



