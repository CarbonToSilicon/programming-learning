import re

string_ = "Pick a 'folower' from the 'garden'!"
pattern_ = re.compile(r"\s'[a-z]+'\s")
print(type(pattern_))
match_o = pattern_.search(string_) #Search "anywhere" only first occurence in any string, returns a "match object" if found
print(match_o) #re.Pattern
print(type(match_o)) #re.Match
if match_o:
    print(match_o.group())
    print(match_o.start())
    print(match_o.end())
    print(match_o.span())


match_o = pattern_.match(string_) #Only search in the very "begining" of any string, returns a "match object" if found otherwise a "None"
print(match_o)
if match_o:
    print(match_o.group())
    print(match_o.start())
    print(match_o.end())
    print(match_o.span())
string_ = " 'pick' a 'folower' from the garden!"
match_o = pattern_.match(string_)
print(match_o)
print(type(match_o)) #re.Match
if match_o:
    print(match_o.group())
    print(match_o.start())
    print(match_o.end())
    pr = (match_o.span())
    print(pr)
    print(type(pr))


match_o = re.findall("e", string_) #search for "all nonlaping search patterns" in a string returns the "strings that matched" the pattren in a "list"
print(match_o)
print(type(match_o)) #list
match_o = re.findall("eat", string_)
print(match_o)


pattern_ = re.compile(r"e")
string_ = "There are a lot of flowers in the flowery flower field."
for match in pattern_.finditer(string_):
    print(match)

string_ = "forms of a word are color, colour "
print(re.findall(r"colou?r", string_))

string_ = "apple, banana, cherry, date"
print(re.findall(r"apple,.*,", string_))
print(re.findall(r"apple,.*?,", string_))

string_ = "100 dollars, 50 euros, 20 dollars, 32dollars"
print(re.findall(r"\d+(?= dollars)", string_))
print(re.findall(r"\d+(?=dollars)", string_))
print(re.findall(r"\d+(?=\s+dollars)", string_))
print(re.findall(r"\d+(?=\s*dollars)", string_))

string_ = "100 dollars, 50 euros, 20 dollars, 32dollars"

print(re.findall(r"\d+(?! dollars)", string_))
print(re.findall(r"\d+(?!dollars)", string_))
print(re.findall(r"\d+(?!\s+dollars)", string_))
print(re.findall(r"\d+(?!\s*dollars)", string_))

# Place \b after \d+ to force the engine to look at the full number
print(re.findall(r"\d+\b(?!\s*dollars)", string_))
# Output: ['50']
import re

text = "John Doe, age 30"

# Non-capturing group (?: ) groups the first/last name but doesn't isolate them
# Named group (?P<name> ) labels the age group for easy access
pattern = r"(?:[A-Z][a-z]+\s[A-Z][a-z]+), age (?P<a>\d+)"

match = re.search(pattern, text)
if match:
    # Access the group by its assigned name
    print(match.group("a"))
    # Output: '30'
    
    # Notice the name 'John Doe' is omitted from groups() because it was non-capturing
    print(match.groups())
    # Output: ('30',)
