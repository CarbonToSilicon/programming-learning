with open("students.csv") as readf:
    for line in readf:
        name, City = line.rstrip().split(",")
        print(f"Welcome {name}!\n You live in {City}.")
        