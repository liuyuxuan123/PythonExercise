import string
s1 = 'This is a test string'
s2 = string.digits

l1 = s1.split()
l2 = [int(i) for i in s2]

# len 
print('Len : %d' % len(l1))

#max && min 
print('Max : %d' % max(l2))
print('Min : %d' % min(l2))

#sorted && reversed

print('Sorted : %s' % str(sorted(l1)))
print('Reversed : %s' % str(list(reversed(l2))))


#enumerate && zip
album = ['tale','robot','pyramid']
print('Enumerate :')
for i,name in enumerate(album):
	print(i,name)

fn = ['ian','stuart','david']
ln = ['bairnson','elloit','paton']
print('Zip:')
for i in zip(fn,ln):
	print('%s %s' % i)

#sum
print('Sum %d' % sum(l2))




