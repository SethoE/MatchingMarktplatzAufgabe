duden = ["lampe", "palme", "anna", "otto", "regallager", "lagerregal", "ampel", ""]
palindrom = []
anagramm = []


def checkforPalindrom(word):
    return word[::-1] == word


def checkforAnagramm(word):
    sorted_word = sorted(word)
    for anagramm_word in duden:
        if anagramm_word == word:
            continue
        if(sorted_word == sorted(anagramm_word)):
            return True
    return False


for word in duden:
    if("-" in word):
        continue
    if(checkforPalindrom(word)):
        palindrom.append(word)
    if(checkforAnagramm(word)):
        anagramm.append(word)


print(anagramm)
print(palindrom)
