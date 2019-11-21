
# open files
input_file = open("input.txt", "r")

# get two nums from two lines
p = int(input_file.readline().strip('\n'))
g = int(input_file.readline().strip('\n'))
b = int(input_file.readline().strip('\n'))
A = int(input_file.readline().strip('\n'))
ciphertext = input_file.readline().strip('\n')
input = int(ciphertext, 2)

print(input)
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

Alice_pub_key = A
print("Alice public key = ", Alice_pub_key)

Bob_pub_key = cal(g, b, p)
print("Bob public key = ", Bob_pub_key)

Bob_pri_key = cal(A, b, p)
print("Bob private = ", Bob_pri_key)

# get multiplier(inverse of the shared key mod p)
# decrypt by converting it into decimal and multiplying multiplier
multiplier = cal(Bob_pri_key, p - 2, p)
result = input * multiplier
binary_result = bin(result).replace("0b","")
print("result message = ", binary_result)
