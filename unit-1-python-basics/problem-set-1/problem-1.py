# s = 'azcbobobegghakl'
vowelCount = 0

for char in s:
    if char in ["a", "e", "i", "o", "u"]:
        vowelCount += 1

print("Number of vowels: " + str(vowelCount))
