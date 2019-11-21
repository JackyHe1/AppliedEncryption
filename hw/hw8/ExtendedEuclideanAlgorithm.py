import math

# open files
input_file = open("input.txt", "r")
# get two nums from two lines
a = int(input_file.readline().strip('\n'))
b = int(input_file.readline().strip('\n'))

# according to extended euclidean algorithm, we try to find a solution for aX + bY = gcd(a, b)
# assume we have a solution X1, Y1, then we have aX1 + bY1 = gcd(a, b)
# assume we have another bX2 + (a % b)Y2 = gcd(b, (a % b))
#  according to gcd, we know that gcd(a, b) = gcd(b, (a % b))
# then we will have aX1 + bY1 = bX2 + (a % b)Y2 => aX1 + bY1 = bX2 + (a - [a / b] * b)Y2
# then we get: aX1 + bY1 = aY2 + b(X2 - [a/b]Y2)
# so we know X1 = Y2, Y1 = X2 - [a/b]Y2
# then we can use recursive func to solve this


def extend_gcd(a, b):
    if b == 0:
        return 1,0,a
    x2, y2, remain = extend_gcd(b, a % b)

    x1 = y2
    y1 = x2 - a // b * y2

    return x1, y1, remain


print(extend_gcd(a, b))