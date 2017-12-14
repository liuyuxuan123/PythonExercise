
stack = []

def pushit():
	stack.append( raw_input(' Enter New String: ').strip() )

def popit():
	if len(stack) == 0:
		print(' Cannot Pop From an Empty Stack!')
	else:
		print('Removed [' + `stack.pop()` + ']')

def viewit():
	print(stack)	

CMDs = {'v' : viewit,
		'u' : pushit,
		'o' : popit
}


def showmenu():
	pr = '''
P(U)sh
P(O)p
(V)iew
(Q)uit
	
Enter choice: '''
	
	while True:
		while True:
			try:
				choice = raw_input(pr).strip()[0].lower()
			except(EOFError,KeyboardInterrupt,IndexError):
				choice = 'q'

			print('\nYour Choice is [%s]' % choice)
			if choice not in 'uovq':
				print('Invalid option try again!')
			else:
				break
		if choice == 'q':
			break
		else:
			CMDs[choice]()

if __name__ == '__main__':
	showmenu()















