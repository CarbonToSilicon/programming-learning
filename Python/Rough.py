print("<<Welcome to number system conversion>>")

while True:
    user_input_data=input("Enter your number for conversion: ")
    try:
        if '.' in inp:
            i = float(inp)
            break
        elif '.' not in inp:
            i = int(inp)
            break
    except:
        print("Please enter only numbers!")
        
print(f"Input type - {type(i)}\n ")

print(f"Number type-\n1. Binary\n2. Octal\n3. Decimal\n4. Hexadecimal")
while True:
    ooi=input(f"Select the type you want to convert from: ")
    try:
        ooi = int(ooi) 
        if ooi < 6 and ooi > 0:
            ooi = ooi
            break
        else:
            print("Wrong input!")
    except:
        print("Please only type the relative number of the option!")
while True:
    ooi2=input(f"Select the type you want to convert to: ")
    try:
        ooi2 = int(ooi2)
        if ooi2 == 1 or ooi2 == 2 or ooi2 == 3 or ooi2 == 4:
            ooi2 = ooi2
            break
        else:
            print("Wrong input!")
    except:
        print("Please only type the number corresponding to the option!")
ooi0i = str(user_input_data)
# Binary to Octal
if ooi == 1 and ooi2 == 2:
    fuk = ooi0i.split('.')
    ooi0 = fuk[0]

    len_o=len(ooi0)
    iooup = ooi0.zfill(len_o+(3-(len_o%3)))
    df = 0
    gjj=[]
    hhh=0
    ghj = 0
    for i in iooup:
        hhh += 1
        if hhh%3 == 0:
            gjj = gjj + [iooup[df:hhh]]
            df+=3
    sdk = 0
    ssf = []
        #if '2' not in ooi0 and '3' not in ooi0 and '4' not in ooi0 and '5' not in ooi0 and '6' not in ooi0 '7' not in ooi0 and '8' not in ooi0 and '9' not in ooi0:
    if set(ooi0) <= {'0', '1'}:
        for j in gjj:
            if gjj[sdk] == '001':
                ssf = ssf + [1]
            elif gjj[sdk] == '010':
                ssf = ssf + [2]
            elif gjj[sdk] == '011':
                ssf = ssf + [3]
            elif gjj[sdk] == '100':
                ssf = ssf + [4]
            elif gjj[sdk] == '101':
                ssf = ssf + [5]
            elif gjj[sdk] == '110':
                ssf = ssf + [6]
            elif gjj[sdk] == '111':
                ssf = ssf + [7]
            elif gjj[sdk] == '000':
                ssf = ssf
            else:
                break
            sdk += 1
    else:
        print("Number is not a binary!")
    #print(iooup)
    #print(gjj)
        #print(''.join(ssf))
    pri = ''
    shi= ''.join(map(str, ssf))
    if fuk[0] != ooi0i:
        uoio0 = fuk[1]
        ulen = len(uoio0)
        zneed = 3-(ulen%3)+ulen
        uioi0 = uoio0.ljust(zneed, '0')
    #print(uioi0)
    #print(zneed)
#print(inp[uu:])
        df1 = 0
        gjj1=[]
        hhh1=0
        sdk1 = 0
        ssf1 = []
        for io in uioi0:
            hhh1 += 1
            if hhh1%3 == 0:
                gjj1 = gjj1 + [uioi0[df1:hhh1]]
                df1+=3
        #pri = ''
        if set(uoio0) <= {'0', '1'}:
            for ji in gjj1:
                if gjj1[sdk1] == '001':
                    ssf1 = ssf1 + [1]
                elif gjj1[sdk1] == '010':
                    ssf1 = ssf1 + [2]
                elif gjj1[sdk1] == '011':
                    ssf1 = ssf1 + [3]
                elif gjj1[sdk1] == '100':
                    ssf1 = ssf1 + [4]
                elif gjj1[sdk1] == '101':
                    ssf1 = ssf1 + [5]
                elif gjj1[sdk1] == '110':
                    ssf1 = ssf1 + [6]
                elif gjj1[sdk1] == '111':
                    ssf1 = ssf1 + [7]
                elif gjj1[sdk1] == '000':
                    ssf1 = ssf1
                else:
                    break
                sdk1 += 1
            ghj += 1
    #print(ssf1)
        pri=''.join(map(str, ssf1))
    if ghj > 0:
        print(shi+'.'+pri+'₈')
    else:
        print(shi+'₈')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    