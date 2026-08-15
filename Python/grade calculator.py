print(f"=== Grade Claculator ===\n")
# math
while True:
    try:
        # takes input in string form
        math_input = input("\nEnter math score (0-100):\n ")
        # sets condition for how much decimals can they type
        if math_input.count('.') > 1:
            print=("Only one decimal point allowed!")
            continue
        #     
        if '.' in math_input:
            decimal_places = len(math_input.split('.')[1])
            if decimal_places > 2:
                print(f'Maximau 2 decimal places allowed!')
                continue
        math = float(math_input)
        if math > 100:
            print(f'Score must be less than or equal to100!')
            continue            
        if math < 0:
            print(f'Score must be positive!')
            continue            
        break
    except ValueError:
        print(f'Please enter a right value!\nTry again.')
# science
while True:
    try:
        science_input = input("\nEnter science score (0-100): \n")        
        if science_input.count('.') > 1:
            print=("Only one decimal point allowed!")
            continue
        if '.' in science_input:
            decimal_places = len(science_input.split('.')[1])
            if decimal_places > 2:
                print(f'Maximau 2 decimal places allowed!')
                continue
        science = float(science_input)
        if science > 100:
            print(f'Score must be less than or equal to100!')
            continue            
        if science < 0:
            print(f'Score must be positive!')
            continue
        break
    except ValueError:
        print(f'Please enter a right value!\nTry again.')
# english        
while True:
    try:
        english_input = input("\nEnter english score (0-100):\n ")
        if english_input.count('.') > 1:
            print=("Only one decimal point allowed!")
            continue
        if '.' in english_input:
            decimal_places = len(english_input.split('.')[1])
            if decimal_places > 2:
                print(f'Maximau 2 decimal places allowed!')
                continue
        english = float(english_input)
        if english > 100:
            print(f'Score must be less than or equal to100!')
            continue            
        if english < 0:
            print(f'Score must be positive!')
            continue
        break
    except ValueError:
        print(f'Please enter a right value!\nTry again.')
        
average = (math + science + english) / 3        

if average >= 90 and average <= 100:
    letter_grade = 'A'
    message = 'Excellent work!'
elif average >= 80 and average < 90:
    letter_grade = 'B'
    message = 'Good job!'
elif average >= 70 and average < 80:
    letter_grade = 'C'
    message = 'Satisfactory'
elif average >= 60 and average < 70:
    letter_grade = 'D'
    message = 'Needs improvement'
elif average < 60:
    letter_grade = 'F'
    message = 'Must retake'

honor_roll = average >= 95
passing = average >= 60
all_subj_pass = math >= 60 or science >= 60 or english >= 60
any_subj_excellent = math >= 90 or science >= 90 or english >= 90


print(f'\n=== GRADE REPORT ===')
print(f'Math: {math}')
print(f'Science: {science}')
print(f'English: {english}')
print(f'Average: {average: .2f}')
print(f'Letter Grade: {letter_grade}')
print(f'Comment: {message}')

print(f'\n=== ACHIEVEMENT ===')
print(f'Honor roll: {honor_roll}')
print(f'All subjects passing: {all_subj_pass}')
print(f'Excellent in any subject: {any_subj_excellent}')

