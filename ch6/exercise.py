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
	while aStr[:1] == ' ':
	    aStr = aStr[1:]
	while aStr[-1:] == ' ':
   		aStr = aStr[:-1]
	return aStr

aStrList = ['  asklas',' wqowio  ',' ajskajsk  ','','   ']
for i in range(len(aStrList)):
	s = nstrip(aStrList[i])
	print(s,len(s))
	#nstrip(aStrList[i])

# 6-8
def translate(num):
	#word = ['thousand','hundred']

	num1 = 'One Two Three Four Five Six Seven Eight Nine Ten' \
	'Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
	num2 = 'Twelve Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()

	def words(n):
		if n < 20:
			return num1[n - 1:n]
		elif n < 100:
			return [num2[n // 10 - 2]] + words(n % 10)
		elif n < 1000:
			return [num1[n // 100 - 1]] + ['Hundred'] + words(n % 100)
		else:
			for p, w in enumerate(('Thousand', 'Million', 'Billion'), 1):
				if n < 1000 ** (p + 1):
					return words(n // 1000 ** p) + [w] + words(n % 1000 ** p)

	print(words(num))
	return ' '.join(words(num)) or 'Zero'

print(translate(9999))















