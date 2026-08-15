print("<<<It is case sensetive>>>")

mfile = open('mbox.txt')
rfile = mfile.read()

target_string = input(f"Type what you are looking for.\n")

# Find the first occurrence
lenfind = rfile.find(target_string)

locates = []
counter = 0

# Check if the first one exists before looping
if lenfind != -1:
    locates.append(str(lenfind))
    counter += 1
    
    # Loop to find subsequent occurrences
    while True:
        # searching from the character AFTER the last found position
        # We pass lenfind + 1 as the second argument to .find()
        lenfind = rfile.find(target_string, lenfind + 1)
        
        # If .find() returns -1, no more matches found
        if lenfind == -1:
            break
            
        locates.append(str(lenfind))
        counter += 1

print("Count:", counter)
#print("Locations:", locates)

mfile.close()