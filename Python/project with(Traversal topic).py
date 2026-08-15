ask = input('Type anything you want to work upon: ')
gh =  input('Enter which character you want to count from your enterd text: ') #inputs are taken in the first place

#____ex.1 Print one char is line____
print('one character each line:')
index = 0
while index < len(ask):
	print(ask[index])
	index += 1
print()

#____ex.2 Count a specific letter____
index = 0
ii = 0
while index < len(ask):
	if ask[index] == gh:
		ii += 1
	index += 1
print('Total count of  ' + gh + ' is:' , ii , '\n')

#____ex.3 Print char with index____
index = 0
print('Each character on a new line with its index number:')
while index < len(ask):
	print(f"Index {index}: {ask[index]}")
	index += 1
print()

#____ex.4 Count Vowels____
index = 0
vow = 0
print('Total vowels are:')
while index < len(ask):
	if ask[index] == 'a':
		vow += 1
	elif ask[index] == 'i':
		vow += 1
	elif ask[index] == 'o':
		vow += 1
	elif ask[index] == 'u':
		vow += 1
	elif ask[index] == 'e':
		vow += 1
	index += 1
print(vow, '\n')

#____ex.5 Reverse Print____
print('One character per line in reverse order:')
index = 0
index1 = len(ask)
while index1 > index:
	index1 -= 1
	print(ask[index1])
print()

#____ex.challenge  Alternating char (even indexing)____
	#print(ask[::2]) # ------- it gives less control than the while loop.
index = 0
while index < len(ask):
	print(ask[index])
	index += 2
	
print()







