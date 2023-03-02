myDictionary={}

myDictionary.update({input("name1"):input("age1")})
myDictionary.update({input("name2"):input("age2")})
myDictionary.update({input("name3"):input("age3")})

print(myDictionary)

dictKeys=list(myDictionary.keys())
dictValues=list(myDictionary.values())

print(dictKeys)
print(dictValues)

if dictValues[0]>dictValues[1] and dictValues[0]>dictValues[2]:
    print(dictKeys[0])
elif dictValues[1]>dictValues[0] and dictValues[1]>dictValues[2]:
    print(dictKeys[1])
elif dictValues[2]>dictValues[1] and dictValues[2]>dictValues[0]:
    print(dictKeys[2])
else:
    print("no_difference")