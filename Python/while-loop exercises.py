
#1 --- Number guessing game
secret = 15
guess = None
while guess != secret:
	guess = input("( 1 )Guess the secret number: ")
	if guess == '-':
		print()
		break
	elif guess != '-':
		guess= int(guess)
	elif guess <secret:
		print("Too low!")
	elif guess > secret:
		print("Too high!")
	else:
		print("Congretulations! You gussed it!\n")

#1 --- User input Until "done"
total = 0
count = 0
while True:
	inp = input("( 2 )Enter a number (or 'done' to finish): ")
	if inp == '-':
		print()
		break
	elif inp != 'done':
		num = float(inp)
		total += num
		count +=1
	elif inp == 'done':
		if total > 0:
			print("Sum:", total)
			print("Average:", total / count)
			print()
			break
		else:
			print("Sum = No number entered!")
			print("Avreage = No number entered!")
			print()
			break
	else:
		print("No  numbers were entered.")

#3 --- Valid user input
while True:
	password = input("( 3 )Enter a password (at  least 6 characters): ")
	if password == '-':
		print()
		break
	elif len(password) >= 6:
		print("Password accepted!\n")
		break
	else:
		print("Password too short, try again.")


#while True:
	#n = input("( 4 )Enter a positive integer(1 - 10): ")
	#if n == '-':
		#print()
		#break
	#elif int(n) <= 10 and int(n) > 0:
		#n=int(n)
		#n-=1
		#print(n)
	#else:
		#print('Please enter a number form 1 to 10:')
#print("Blastoff!")
#2	

#n = input("( 4 )Enter a positive integer(1 - 10): ")
#if n != '-':
	
	
	
#4 --- Countdown Timer	
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

#5 --- Menu-driven calculator
iop='( 5 )Menu driven calculator(type "ok" to continue and "-" to skip). '
ik = input(iop)
if ik == "ok":
	while True:
		print("------- Menu -------\n")
		print("1. Add")
		print("2. Multiply")
		print("3. Quit")
		choice = input("Choose an option: ")
		if choice == '3':
			print("Goodbye!")
			break
		elif choice in ('1', '2'):
			a = float(input("Enter first number: "))
			b = float(input("Enter second number: "))
			if choice == '1':
				print("Result: ", a + b)
			else:
				print("Result: ", a + b)
		else:
			print("Invalid option.")
else:
	print()



