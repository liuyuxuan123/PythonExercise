import string


aList = list(range(0,10))
bList = list(range(11,20,2))

print('Before Append: ',aList)
aList.append(100)
print('After Append: ',aList)

print('Count:',aList.count(2))

print('Before Extend: ',aList)
aList.extend(bList)
print('After Extend: ',aList)

print('Index: ',aList.index(2,1))

print('Before Insert: ',aList)
aList.insert(1,99)
print('After Inser: ',aList)

print('Before Pop: ',aList)
aList.pop()
print('After Pop: ',aList)

print('Before Reverse: ',aList)
aList.reverse()
print('After Reverse: ',aList)

print('Before Sort: ',aList)
aList.sort()
print('After Sort: ',aList)



