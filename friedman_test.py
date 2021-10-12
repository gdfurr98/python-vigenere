alphaDict = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
nMinusOneDict = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
nTimesMinusOneDict = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
toBeCracked = input("Type in the encoded text here: ")
lowerCrack = ''
n = 0
nTimesMinusOne = 0

for x in toBeCracked:
    if ord(x.lower()) > 122:
        continue
    if ord(x.lower()) < 97:
        continue
    lowerCrack += x.lower()
print('lowercrack:', lowerCrack)
for x in lowerCrack:
    alphaDict[x] += 1

for x in alphaDict:
    nMinusOneDict[x] += alphaDict[x] - 1

for x in nTimesMinusOneDict:
    nTimesMinusOneDict[x] += nMinusOneDict[x] * alphaDict[x]

for x in alphaDict:
    n += alphaDict[x]
    nTimesMinusOne += nTimesMinusOneDict[x]

print('alphaDict:', alphaDict)
print('n equals:', n)
print('n times minus one:', nTimesMinusOne)
print('nMinusOneDict:', nMinusOneDict)
print('nTimesMinusOneDict:', nTimesMinusOneDict)

finalN = float(n)
finalNTimesMinusOne = float(nTimesMinusOne)
friedmanSeriesValue = (finalNTimesMinusOne) / ((finalN) * (finalN - 1.0))

print('series value', friedmanSeriesValue)
###for some fucking reason the goddamn floating point math is fucking up and resolving to a higher value than should be expected.
##Idk if this is my own failure or the programming language's or both. who knows im too fucked up with sleep deprivation to work it out further.
numerator = 0.027 * finalN
denominatorP1 = (finalN - 1) * friedmanSeriesValue
denominatorP2 = finalN * 0.038
denominatorP3 = 0.065
finalDenom = denominatorP1 - denominatorP2 + denominatorP3
fullEQ = numerator / finalDenom
print('numerator: ', numerator)
print('denominatorp1: ', denominatorP1)
print('denominatorp2: ', denominatorP2)
print('full denominator', finalDenom)
print("final value of the friedman test", fullEQ)
