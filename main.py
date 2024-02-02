from english_words import get_english_words_set
web2lowerset = get_english_words_set(['web2'], lower=True)

listofsolves = []

def getLetters():
    letters = []
    for x in range(0, 5):
        letternum = x + 1
        letters.append(input("Letter number " + str(letternum) + ": "))
    return letters


def yellowLetters():
    yellows = []
    for x in range(0,5):
        userinput = input("Yellow Letter (type nothing to end): ")
        if userinput != '':
            yellows.append(userinput)
        else:
            break
    return yellows


def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


def getWrong():
    wrongletters = []
    for i in range(0,26):
        userinput = input("Input wrong letters 1 at a time (if no more, enter nothing):  ")
        if not userinput:
            break
        wrongletters.append(userinput)
    return wrongletters


def cleanUpList():
    global listofsolves
    listofsolves = list(dict.fromkeys(listofsolves))
    length1 = 0
    while length1 < len(listofsolves):
        item1 = listofsolves[length1]
        if len(item1) != 5 or item1 not in web2lowerset:
            listofsolves.remove(item1)
            length1 = length1 - 1
        length1 = length1 + 1


def solver(letters, yellows, wrongs):
    testsolve = letters[:]
    yellowschecked = True
    for a in range(97,123):
        i = 0
        if not letters[i] and chr(a) not in wrongs:
            testsolve[i] = chr(a)
        for b in range(97,123):
            i = 1
            if not letters[i] and chr(b) not in wrongs:
                testsolve[i] = chr(b)
            for c in range(97,123):
                i = 2
                if not letters[i] and chr(c) not in wrongs:
                    testsolve[i] = chr(c)
                for d in range(97,123):
                    i = 3
                    if not letters[i] and chr(d) not in wrongs:
                        testsolve[i] = chr(d)
                    for e in range(97,123):
                        i = 4
                        if not letters[i] and chr(e) not in wrongs:
                            testsolve[i] = chr(e)
                        for m in yellows[:]:
                            if m not in testsolve:
                                yellowschecked = False
                        if yellowschecked is True:
                            listofsolves.append(listToString(testsolve))
                        yellowschecked = True


solver(getLetters(),yellowLetters(),getWrong())
cleanUpList()
print(listofsolves)