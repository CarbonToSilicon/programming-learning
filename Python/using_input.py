t2 = input('What is your name? ')
t3s = input('How old are you? ')
t3 = int(t3s)
t4s = input('what is your height in cm? ')
t4 = float(t4s)

# f-string method
print(f'Welcome {t2}. You are {t3} years old. You are {t4} cm tall.')

# String Concatenation with +
print("Welcome " + t2 + "!  You are " + str(t3) + ' years old.' + " You are " + str(t4) + " cm tall.")

# str.format() method
print('Welcome {}. You are {} years old. You are {} cm tall.'.format(t2, t3, t4))

#Comma-Separated print()
print('Welcome', t2 + '.', 'You are', t3, 'years old. You are', t4, 'cm tall.')