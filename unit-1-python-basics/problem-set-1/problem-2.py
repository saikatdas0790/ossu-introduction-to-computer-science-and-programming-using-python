# s = "azcbobobegghakl"
stringToFind = "bob"
occurrencesCount = 0
indexToStartAt = 0

while True:
    result = s.find(stringToFind, indexToStartAt)
    if result == -1:
        break

    occurrencesCount += 1
    indexToStartAt = result + 1


print("Number of times bob occurs is: " + str(occurrencesCount))
