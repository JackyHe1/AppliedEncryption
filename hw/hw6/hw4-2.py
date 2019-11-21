# open files
input_file = open("input.txt", "r")

# get data from two files
input_txt = input_file.readline().strip('\n')

isBinay = True
for ch in input_txt:
    if ch not in ['1', '0', ' ']:
        isBinay = False
        break

# for alphaTxt, get every char and transfer it to binary
def alpha_to_binary(alpha_str):
    # for every char in alpha_str, convert it to binary according to format '08b', binary with 8 digits
    # join result from different chars
    result = ' '.join(format(ord(x), '08b') for x in alpha_str)
    print("Convert \"", alpha_str, "\" to \"", result, "\"")


# for binaryTxt, get 8 binary digits and transfer them to char every round
def binary_to_alpha(binary_str):
    # every time, substring eight digits binary and transfer it to num
    # then transfer num to ascii char
    origin_str = binary_str
    result = ""
    while origin_str != "":
        i = chr(int(origin_str[0:8], 2))
        result = result + i
        origin_str = origin_str[9:]
    print("Convert \"", binary_str, "\" to \"", result, "\"")


# call functions to get generated txt
if isBinay :
    binary_to_alpha(input_txt)
else :
    alpha_to_binary(input_txt)



