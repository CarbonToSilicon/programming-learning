Names = ['crunchy fog', 'ram  bladder', 'lark vomit']
Nums = [10, 35, 90, 2]
Mix = [Names, Nums, 5.6]
empty = []

print(Mix)
ss = Names[0]
print(ss)
dd = ss[0]
print(dd)

Nums[1] = 15 #change in nums[1]

Num_2 = []
for i in range(len(Nums)):
    ak = Nums[i] * 2
    Num_2.append(ak)
print(Num_2)

print(15 in Nums)
print(35 in Nums)

for i in Mix:
    print(i)

for x in empty:
    print("This never happens!")

print(Nums + [33, 30])
print(Nums[0:2] * 2)
print("\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n")

days = []
with open("mbox-short.txt", "r") as file:
    for i in file:
        if i.startswith('From '):
           #print(i)
            s = i.split(" ")
            #print(s[2])
            days.append(s[2])

print(days)
days1 = " ".join(days)

sun, mon, tue, wed, thu, fri, sat = 0, 0, 0, 0, 0, 0, 0
for i in days:
    if i == "Sun":
        sun += 1
    elif i == "Mon":
        mon += 1
    elif i == "Tue":
        tue += 1
    elif i == "Wed":
        wed += 1
    elif i == "Thu":
        thu += 1
    elif i == "Fri":
        fri += 1
    elif i == "Sat":
        sat += 1
# print(f"Sunday: {"Sun".count(days1)}")
# print(f"Monday: {"Mon".count(days1)}")
# print(f"Tuesday: {"Tue".count(days1)}")
# print(f"Wednesday: {"Wed".count(days1)}")
# print(f"Thursday: {"Thu".count(days1)}")
# print(f"Friday: {"Fri".count(days1)}")
# print(f"Saturday: {"Sat".count(days1)}")
print(f"Sunday: {sun}")
print(f"Monday: {mon}")
print(f"Tuesday: {tue}")
print(f"Wednesday: {wed}")
print(f"Thursday: {thu}")
print(f"Friday: {fri}")
print(f"Saturday: {sat}")
print("\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n")

unique_words = []
with open("romeo.txt") as romeo:
    for line in romeo:
        words = line.split()
        wlen = 0
        for word in words:
            if words[wlen] not in unique_words:
                unique_words.append(words[wlen])
            wlen += 1
unique_words.sort()
print(unique_words)
print("\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n")

file_name = input("Enter a file name: ")
senders = []
try:
    with open(file_name) as m_file:
        for line in m_file:
            if line.startswith("From "):
                words = line.split()
    
                senders.append(words[1])    
    count = 0
    #print(senders)
    while count < len(senders):
        print(senders[count])
        count += 1
    print(f"There were {len(senders)} lines in the file with From as the first word")
except FileNotFoundError:
    print("File not found!\n")
print("\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n")

nums = []
while (True):
    num = input("Enter a number: ")
    if num.lower() == "done":
        break
    nums.append(num)
maX = max(nums)
miN = min(nums)
print(f"Maximum: {float(maX)}")
print(f"Minimum: {float(miN)}")
print("\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n")

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    if line.startswith('From:'):
        print(line.strip())

