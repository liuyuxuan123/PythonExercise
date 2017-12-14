# 6-1

a = '12345678'
b = '234'
print( a and b)

# 6-3
import random 
import string

def grade(num):
	if num < 60:
		return 'F'
	elif num <= 69:
		return 'D'
	elif num <= 79:
		return 'C'
	elif num <= 89:
		return 'B' 
	elif num <= 100:
		return 'A'
	else:
		raise OverflowError

def averageScore(aList):
	s = sum(aList)
	n = len(aList)
	return s / n


scoreList = [random.randint(0,100) for i in range(100)]
gradeList = [grade(i) for i in scoreList]
print(scoreList)
print(gradeList)

print(averageScore(scoreList))

# 6-6

def nstrip(aStr):
	# for i in range(len(aStr)):
	# 	print(aStr[i])
	# 	if not aStr[i].isspace():
	# 		a = i
	# 		break
	# for j in range(len(aStr) - 1,1,-1):
	# 	print(aStr[j])
	# 	if not aStr[j].isspace():
	# 		b = j
	# 		break

	while aStr[:1]==' ':
	    aStr=aStr[1:]
	while aStr[-1:]==' ':
   		aStr=aStr[:-1]

	return aStr

aStrList = ['  asklas',' wqowio  ',' ajskajsk  ','','   ']

print(len(''[:1]),'Test')
for i in range(len(aStrList)):
	s = nstrip(aStrList[i])
	print(s,len(s))
	#nstrip(aStrList[i])
















