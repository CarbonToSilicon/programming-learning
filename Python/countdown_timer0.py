while True:
	try:
		n = input("( 4 )Enter a positive integer(1 - 10), or '-' to skip: ")
		if n == '-':
			break
		elif int(n) >= 1 and int(n) <= 10:
			n=int(n)
			while n > 0:
				print(n)
				n-=1
			print("Blastoff!")
		else:
			print("Please enter a valid input, try again!")
			continue
		break
	except:
			print("Please enter a valid input, try again!")

