# judge whether string(word in sArr) is English, accoroding to the ratio of English word in dictionary
# if ratio is more than 0.3, we think this sentence(sArr) is English
def isEnglish(sArr, dict):
    count = 0
    for word in sArr:
        if word.upper() in dict:
            count = count + 1
    return count * 1.0 / len(sArr) > 0.3

# get new Char according to current char(ch) and key value(i)
# flag 1 is to used encrypt message, flag -1 is used to decrypt message
def getNewChar(ch, i, flag):
    if ch in lowers:
        index = lowers.index(ch)
        newIndex = (index + flag * i) % len(alphabet)
        return lowers[newIndex]
    elif ch in caps:
        index = caps.index(ch)
        newIndex = (index + flag * i) % len(alphabet)
        return caps[newIndex]

# get input
file_name = str(input("What input file do you want to use? "))
input_file = open(file_name, "r")

# first line if key values
key = input_file.readline().strip().split(" ")

# second line is message
str_message = input_file.readline()
message = str_message.strip('\n').split(" ")
print("Key: ", key)
print("str: ", str_message)
print("Original message: ", message)

# get dict info from dictionary.txt file
# add dict info to set to reduce search time
dictionary = set()
dict_file = open("dictionary.txt", "r")
for line in dict_file.readlines():
    dictionary.add(str(line.strip('\n')))

# basic alphabets for shift
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# get lower case alphabets and upper case alphabets
caps = list(alphabet)
lowers = list(alphabet.lower())

# encrypte message according to key if message is English
newMessage = ''
i = 0
flag = 1

# set flag to -1 if it is not English, because we need to decrypt, we need to do left shifting
if isEnglish(message, dictionary) == False:
    flag = -1

# decrypt or encrypt all the word in message
for word in message:
    newWord = ''
    # get shifted char according to key and add it to newWord, then add newWord to final result(new Message)
    for ch in word:
        if ch.isalpha() == False:
            newWord = newWord + ch
            continue
        newCh = getNewChar(ch, int(key[i]), flag)
        newWord = newWord + newCh
        i = i + 1
    newMessage = newMessage + " " + newWord;

# save new message to different file
if(flag == 1):
    f = open("encryption.txt", "w")
    f.write(newMessage)
else:
    f = open("decryption.txt", "w")
    f.write(newMessage)

print("new message = ", newMessage)