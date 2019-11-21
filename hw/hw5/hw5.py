
# open files
input_file = open("input.txt", "r")

# get two nums from two lines
p = int(input_file.readline().strip('\n'))
g = int(input_file.readline().strip('\n'))

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


print("g = ", g, " ,p = ", p)
print("Final result = ", cal(g, p - 2, p))