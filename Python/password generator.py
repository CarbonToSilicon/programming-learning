    
charactors = ['*', '#', '/', '$', '@', '^', '%', '&', '_', '-', '.', '<', '>', '~', ':', ';',]
letters = ['a' 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
cap_letters = ['A' 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

while True:
    try:
        inp = int(input(f"How much long password do you need?\nPlease enter how much charactors should it contain (from 6 to 16 charactors)"))
        if inp >= 6 and inp <= 16:
            break
        else:
            print('Please enter value between 6-16')
    except ValueError:
        print('Please enter value in whole number between(6-16)')

import random

def random_pass(bb, aa):
    inp_1 = random.choice(letters)
    inp_2 = random.choice(charactors)
    inp_3 = random.choice(numbers)
    inp_4 = random.choice(cap_letters)
    ti0 = [inp_1, inp_2, inp_3, inp_4]
    ti = random.choices(ti0, weights=bb, k=aa)
    print('Your password is: ', "".join(ti))

if inp == 6:
    asi = [2, 2, 1, 1]
    dd = inp
    random_pass(asi, dd)
elif inp == 7:
    asi = [2, 2, 1, 1]
    dd = inp
    random_pass(asi, dd)
elif inp == 8:
    asi = [2, 2, 1, 1]
    dd = inp
    random_pass(asi, dd)
elif inp == 9:
    asi = [2, 2, 1, 1]
    dd = inp
    random_pass(asi, dd)
elif inp == 10:
    asi = [2, 2, 1, 1]
    dd = inp
    random_pass(asi, dd)
elif inp == 11:
    asi = [2, 2, 1, 1]
    dd = inp
    random_pass(asi, dd)
elif inp == 12:
    asi = [2, 2, 1, 1]
    dd = inp
    random_pass(asi, dd)
elif inp == 13:
    asi = [2, 2, 1, 1]
    dd = inp
    random_pass(asi, dd)
elif inp == 14:
    asi = [2, 2, 1, 1]
    dd = inp
    random_pass(asi, dd)
elif inp == 15:
    asi = [2, 2, 1, 1]
    dd = inp
    random_pass(asi, dd)
elif inp == 16:
    asi = [2, 2, 1, 1]
    dd = inp
    random_pass(asi, dd)
else:
    print("get out!")
    
    #inp1 = random.choice(charactors)
    #inp2 = random.choice(letters)
    #inp2 = random.choice(numbers)
    #inp3 = random.choice(cap_letters)
    #inp4 = random.choice(numbers)
    #inp5 = random.choice(letters)
    #inp6 = random.choice(numbers)
    #ti = [inp1, inp2, inp3, inp4, inp5, inp6]
    #random.shuffle(ti)



