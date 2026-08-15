print("=== Personal Profile Builder ===")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
country = input("Enter your country: ")

current_year = 2025
birth_year = current_year - age

# this statment of code wan not introduced till the chapter 3
# it is optional -
initials = name[0] +name[name.find(" ") + 1]
name_length = len(name)

print(f"=== PROFILE ===")
print(f'Name: {name}')
print(f"Initials: {initials}")
print(f"Name length: {name_length} characters")
print(f"Age: {age} years old")
print(f"Birth year: {birth_year}")
print(f"Location: {city}, {country}")