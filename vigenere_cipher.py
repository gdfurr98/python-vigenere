cipherList = [['a', 0], ['b', 1], ['c', 2],['d', 3], ['e', 4], ['f', 5], ['g', 6], ['h', 7], ['i', 8],['j', 9], ['k', 10], ['l', 11],
['m', 12], ['n', 13], ['o', 14],['p', 15], ['q', 16], ['r', 17], ['s', 18], ['t', 19], ['u', 20],['v', 21], ['w', 22], ['x', 23], ['y', 24], ['z', 25]]

keyList = []

testList = []

appendList = []

rotList = []

encryptedList = []

counter = 0

initInput = input("Do you want to encrypt or decrypt? ")
if initInput == "encrypt":
    unEncryptedText = input("What do you want encrypted? ")

    keyText = input("What is the key? ")

    ###Numerical/Assignment Logic

    for x in range(len(keyText)):
        keyList.append(keyText[x].lower())
    for x in range(len(unEncryptedText)):
        appendList.append(unEncryptedText[x].lower())
        appendList.append(keyList[counter])
        testList.append(appendList)
        counter = counter + 1
        appendList = []
        if counter == len(keyText):
            counter = 0
    for x in testList:
        for y in cipherList:
            if y[0] == x[1]:
                rotList.append(y[1])
    counter = 0

    ###Encryption Loop

    for z in testList:
        if ord(z[0]) < 97 or ord(z[0]) >= 123:
            encryptedList.append(z[0])
            continue
        if (ord(z[0]) + int(rotList[counter])) < 123:
            rotted = int(rotList[counter]) + ord(z[0])
            encryptedList.append(chr(rotted))
            counter = counter + 1
            continue
        if ord(z[0]) + int(rotList[counter]) >= 123:
            rotted = 97 + ((ord(z[0])+int(rotList[counter])) - 123)
            encryptedList.append(chr(rotted))
            counter = counter + 1
            continue
        counter = counter + 1
        encryptedList.append(chr(rotted))
    finalString = ''.join(encryptedList).upper()
    print(finalString)
else:
    unDecryptedText = input("What do you want decrypted? ")

    keyText = input("What is the key? ")

    ###Numerical/Assignment Logic

    for x in range(len(keyText)):
        keyList.append(keyText[x].lower())
    for x in range(len(unDecryptedText)):
        appendList.append(unDecryptedText[x].lower())
        appendList.append(keyList[counter])
        testList.append(appendList)
        counter = counter + 1
        appendList = []
        if counter == len(keyText):
            counter = 0
    for x in testList:
        for y in cipherList:
            if y[0] == x[1]:
                rotList.append(y[1])
    counter = 0

    ##Decryption Loop

    for z in testList:
        if ord(z[0]) < 97 or ord(z[0]) >= 123:
            encryptedList.append(z[0])
            continue
        if (ord(z[0]) - int(rotList[counter])) >= 97:
            rotted = ord(z[0]) - int(rotList[counter])
            encryptedList.append(chr(rotted))
            counter = counter + 1
            continue
        if ord(z[0]) - int(rotList[counter]) < 97:
            rotted = 123 - (97 - (ord(z[0])-int(rotList[counter])))
            encryptedList.append(chr(rotted))
            counter = counter + 1
            continue
        counter = counter + 1
        encryptedList.append(chr(rotted))
    finalString = ''.join(encryptedList).upper()
    print(finalString)
