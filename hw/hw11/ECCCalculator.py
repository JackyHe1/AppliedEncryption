import math


# fast-power  O(logN) time
def fast_power(g, p, MOD):
    # base num is a
    # result is b
    a = g
    b = 1
    while p > 0:
        # fast power
        # do mod every time

        # if p is odd, we should multiple a single base num a to result
        if p % 2 == 1:
            b = b * a % MOD

        # do a^2 to reduce time to compute b by multipling b every time
        a = a ** 2 % MOD
        p = int(p / 2)
    return b % MOD


def getECCResult(Xp, Yp, Xq, p, lambdaK):
    # get b by using b = yp - lamba * xp
    b = Yp - lambdaK * Xp

    # get Xr by using Xr = lamba^2 - Xp - Xq
    Xr = (lambdaK * lambdaK - Xp - Xq) % p

    # get Yr by using Yr = lambda * Xr + b
    Yr = lambdaK * Xr + b

    # get Yr' by using Yr' = -Yr (mod p)
    Yr1 = (-Yr) % p

    # return result
    return Xr, Yr1


def point_double(A, B, p, Xp, Yp):
    # derivation is (3 * X^2 + A) / (2 * Y)
    numerator = (3 * Xp * Xp + A) % p
    denominator = (2 * Yp) % p

    # lambdaK = numerator / denominator, run as numerator * (1 / denominator)
    # call fast_power to reduce running time
    lambdaK = (numerator * fast_power(denominator, p - 2, p)) % p
    return getECCResult(Xp, Yp, Xp, p, lambdaK)


def point_add(A, B, p, Xp, Yp, Xq, Yq):
    # get lambaK by using point P and point Q
    numerator = (Yq - Yp) % p
    denominator = (Xq - Xp) % p

    # lambdaK = numerator / denominator,  run as numerator * (1 / denominator)
    # call fast_power to reduce running time
    lambdaK = (numerator * fast_power(denominator, p - 2, p)) % p

    # get ECC result = P + Q
    result = getECCResult(Xp, Yp, Xq, p, lambdaK)

    # return result
    return result


def ECCMultiple(A, B, p, Xp, Yp, a):
    # if a is 1, just return point P
    if a == 1:
        return Xp, Yp

    # copy a for iteration
    n = a

    # initial value for double-add algorithm
    # consider odd or even to make logic right
    if n % 2 == 1:
        R = (Xp, Yp)
        Q = (Xp, Yp)
        n = a - 1
    else:
        R = point_double(A, B, p, Xp, Yp)
        Q = R
        n = a - 2

    # double and add to reduce running time
    while n > 0:
        if n % 2 == 1:
            # call point_add function to calculate R = R + Q
            R = point_add(A, B, p, R[0], R[1], Q[0], Q[1])

        # calculate Q = 2 * Q
        Q = point_double(A, B, p, Q[0], Q[1])
        n = n // 2

    # return result
    return R


# open files
input_file = open("input.txt", "r")

# get nums and points from file
A = int(input_file.readline().strip('\n'))
B = int(input_file.readline().strip('\n'))
p = int(input_file.readline().strip('\n'))
Point_P = input_file.readline().strip('\n')

# get coordinates of point p
Xp = int(Point_P.split(',')[0])
Yp = int(Point_P.split(',')[1])

# check if fifth element is point or integer
fifth_input = input_file.readline().strip('\n')

# if it is point Q
if ',' in fifth_input:
    # get point Q
    Xq = int(fifth_input.split(',')[0])
    Yq = int(fifth_input.split(',')[1])

    # call point_add function to calculate R = P + Q
    print('P = (', Xp, ',', Yp, ')')
    print('Q = (', Xq, ',', Yq, ')')
    print('P + Q = ', point_add(A, B, p, Xp, Yp, Xq, Yq))

else:
    # get a
    a = int(fifth_input)
    # call point_add function to calculate R = a * P
    print('a = ', a)
    print('P = (', Xp, ',', Yp, ')')
    print('R = a * P = ', ECCMultiple(A, B, p, Xp, Yp, a))

input_file.close()

