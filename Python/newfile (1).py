name = input("What is your name? ")
age = int(input("How old are you? "))

if age <= 12:
    age_group = "kid"
elif age > 12 and age <= 19:
    age_group = "teen"
elif age > 20 and age <= 65:
    age_group ="adult"
else:
    age_group = "senior"
    
city = input("In which city do you live? ")

while True:
    gender0 = str(input("What is your gender?\n-Male\n-Female\n-Other\nEnter:  "))
    if gender0 == "Male":
        gender = "Male"
        break
    elif gender0 == "Female":
         gender = "Female"
         break
    elif gender0 == "Other":
         gender = "Other"
         break
    else:
        print("Please select a valid gender. ")

print(f'Welcome {name}! I am your virtual assistant. {city} is a beautiful city. ')

















