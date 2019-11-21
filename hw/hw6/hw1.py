def getNewChar(ch, i):
    if ch in lowers:
        index = lowers.index(ch)
        newIndex = (index + i) % len(alphabet)
        return lowers[newIndex]
    elif ch in caps:
        index = caps.index(ch)
        newIndex = (index + i) % len(alphabet)
        return caps[newIndex]


# get input
input_file = open("CaesarInput.txt", "r")
message = ''
for line in input_file.readlines():
    message = message + line
print ("Original message: ", message)
message = message.strip('\n').split(" ")

# get dict info
dictionary = set()
dict_file = open("dictionary.txt", "r")

# basic chars for shift
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
caps = list(alphabet)
lowers = list(alphabet.lower())

for line in dict_file.readlines():
    dictionary.add(str(line.strip('\n')))

# try to find a shift offset which can transfer most of the words in message, and print decrypted message
maxCount = 0
finalMessage = ''
for i in range(1, 27):
    newMessage = ''
    count = 0

    for word in message:
        newWord = ''
        for ch in word:
            if ch.isalpha() == False:
                newWord = newWord + ch
                continue
            newCh = getNewChar(ch, i)
            newWord = newWord + newCh
        if newWord in dictionary:
            count = count + 1
        newMessage = newMessage + " " + newWord;

    if count > maxCount:
        maxCount = count
        finalMessage = newMessage

print ("Decrypted message: ", finalMessage)


