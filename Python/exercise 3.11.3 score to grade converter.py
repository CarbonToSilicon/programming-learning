print(f"=== Let's see your Grade using your score ===\n")
try:
    raw_score = float(input("Enter score (between 0.0 and 1.0): "))
    print(f"\n==Your Score===\n")
    if raw_score <= 1.0:
        if raw_score >= 0.9 and raw_score <= 1.0:
            print("A")
        elif raw_score >= 0.8 and raw_score < 0.9:
            print("B")
        elif raw_score >= 0.7 and raw_score < 0.8:
            print("C")
        elif raw_score >= 0.6 and raw_score < 0.7:
            print("D")
        else:
            print("F")
    else:
        print("Bad score")
except ValueError:
    print(f"\n==Your Score===\n")
    print("Bad score")
    
