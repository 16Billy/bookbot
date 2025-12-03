def count(content):
    arrayOfWords = content.split()
    return len(arrayOfWords)

def count_char(content):
    dictOfChars = {}
    for i in content.lower():
        if i in dictOfChars:
            dictOfChars[i] += 1
        else:
            dictOfChars[i] = 1
    return dictOfChars

def sort_on(items):
    return items["count"]

def report(dictOfChars):
    listOfDicts = []
    for i in dictOfChars.keys():
        if i.isalpha():
            listOfDicts.append({"char":i,"count":dictOfChars[i]})
    listOfDicts.sort(reverse=True,key=sort_on)
    return listOfDicts