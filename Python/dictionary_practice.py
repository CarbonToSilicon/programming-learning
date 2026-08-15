dictionary = {"Car":"Ferarri", "Model": "Fi", "MFD": 2026, "Owner": "Jeff"} 
print(f"1:- {dictionary}") #1
print(f"2:- {dictionary.items()}") #2
dictionary["Owner"] = "Tushar"
print(f"3:- {dictionary}") #3
print(f"4:- {dictionary["Car"]}") #4
print(f"5:- {dictionary["Model"]}") #5
print(f"6:- {dictionary.get("MFD")}") #6
print(f"7:- {"Car" in dictionary}") #7
print(f"8:- {"Ferarri" in dictionary}") #8
print(f"9:- {dictionary.values()}") #9
print(f"10:- {"Ferarri" in dictionary.values()}") #10 
#print(dictionary["TTTTTTTTTTT"]) #ERROR
word = "brontosaurus" ########### 9.1 dictionary as a set of counters 
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] += 1
print(f"11:- {d}") #11
counts = {"chuck": 1, "annie": 42, "jan": 100}
print(f"12:- {dictionary.get("TTTTTTTTTTT")}") #12
print(f"13:- {counts.get("chuck", 0)}") #13
print(f"14:- {counts.get("TTTTTTTTTTT")}") #14
print(f"15:- {counts.get("TTTTTTTTTTT", 0)}") #15
word = "brontosaurus"
j = {}
for c in word:
    j[c] = j.get(c, 0) + 1
print(f"16:- {j}") #16
fhand = "romeo.txt" ###################### 9.2 dictionaries and files
with open(fhand, "r") as file:
    #rfile = file.read()
    counts = dict()
    for line in file:
        words = line.split()
        for word in words:
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1
    print(f"17:- {counts}") #17
counts = {"chuck": 1, "annie": 42, "jan": 100}  ########## 9.3 looping and dictionaries
print(f"18:- ") 
for key in counts:
    print(key, counts[key]) #18
print(f"19:- ")
for key in counts:
    if counts[key] > 10:
        print(key, counts[key]) #19
lst = list(counts.keys())
print(f"20:-  {lst}")
lst.sort()
print(f"21:-  {lst}")
print("22:-  ")
for key in lst:
    print(key, counts[key])
import string ########################### 9.4 advanced text parsing
print(f"23:-  {string.punctuation}")
with open("romeo-full.txt", "r") as rfile:
    counts = dict()
    for line in rfile:
        line = line.rstrip()
        line = line.translate(line.maketrans("", "", string.punctuation))
        line = line.lower()
        words = line.split()
        for word in words:
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1
    print(f"24:-  {counts}")
with open("mbox-short.txt", "r") as mbox_file:
    days = dict()
    for line in mbox_file:
        words = line.split()
        if line.startswith("From "):
            word = words[2]
            if word not in days:
                days[word] = 1
            else:
                days[word] += 1
    print(f"25:-  {days}")
def maximum_sender(func):
    with open(func, "r") as rfile:
        senders = dict()
        for line in rfile:
            if line.startswith("From "):
                words = line.split()
                word = words[1]
                if word not in senders:
                    senders[word] = 1
                else:
                    senders[word] += 1
        keys_ = list(senders.keys())
        keys_.sort()
        senders_1 = dict()
        for key in keys_:
            senders_1[key] = senders.get(key)
        return senders_1
print(f"26:-  {maximum_sender("mbox-short.txt")}")


