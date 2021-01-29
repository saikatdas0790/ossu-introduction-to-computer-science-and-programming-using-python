# s = 'azcbobobegghakl'
indexToStartAt = 0
tempString = ""
lengthDictionary = {}

for char in s:
    if tempString == "":
        tempString = s[indexToStartAt]

    if indexToStartAt != len(s) - 1 and s[indexToStartAt] <= s[indexToStartAt + 1]:
        tempString = tempString + s[indexToStartAt + 1]
    else:
        if lengthDictionary.get(len(tempString)) == None:
            lengthDictionary[len(tempString)] = tempString
        tempString = ""

    indexToStartAt += 1

lengthDictionaryKeyList = list(lengthDictionary)
lengthDictionaryKeyList.sort()
print("Longest substring in alphabetical order is: " +
      lengthDictionary[lengthDictionaryKeyList[-1]])
