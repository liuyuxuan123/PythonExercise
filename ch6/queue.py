
queue = []

def pushit():
	queue.append(raw_input(' Enter New String !').strip())

def popit():
	if len(queue) == 0:
		print('Cannot Pop From an Empty Queue!')
	else:
		print('Removed [' + `queue.pop(0)` + ']')

def viewit():
	print(queue)

CMDs = {
	'u' : pushit,
	'o' : popit,
	'v' : viewit
}

def showmenu():
	pr = '''
P(U)sh
P(O)p
(V)iew
(Q)uit

Enter Choice : '''

	while True:
		while True: 
			try:
				choice = raw_input(pr).strip()[0].lower()
			except(EOFError,KeyboardInterrupt,IndexError):
				choice = 'q'

			if choice not in 'uovq':
				print('Invalid option Try again !')
			else:
				break
		if choice == 'q':
			break
		else:
			CMDs[choice]()

if __name__ == '__main__':
	showmenu()





