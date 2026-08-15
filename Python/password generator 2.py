            charactors = '*#/$@^%&_-.<>~:;abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while True:
    try:
        inp = int(input(f"How many charactors do you need in your password?\nType from (6 to 18): "))
        if inp >= 6 and inp <= 18:
            break
        else:
            print('Please type vlaue between 6 to 18!')
    except:
        print('Please try again. Enter a valid number as suggested before!')

import random as ra

char_pass = [
ra.choice('*#/$@^%&_-.<>~:;'), 
ra.choice('abcdefghijklmnopqrstuvwxyz'), 
ra.choice('0123456789'), 
ra.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
]

#ra.shuffle(charactors)
#chr = charactors
#di = ra.choices(chr, k=inp)
#ki = ("".join(di))

char_pass += ra.choices(charactors, k=inp-len(char_pass))
ra.shuffle(char_pass)
print(f"Password generated: ", "".join(char_pass))
