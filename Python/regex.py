import re
def find_emails():
    with open('mbox.txt', 'r') as read_file:
        a_string = read_file.read()
        matches = re.findall(r"[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+", a_string)
        notes = f"{matches[:10]}\n\nThe re.findall() returns a list like the above example.\nThis is the code for this: 're.findall('r[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+', a_string)\n" #it returns list
        unique_set = {email for email in matches if not re.search(r'^[0-9]{12}', email)}
        sorted_emails = sorted(unique_set)
        emails = ""
        for i in sorted_emails: emails += i + "\n"
        count = len(sorted_emails)
        return notes, emails, count
    
print(find_emails()[0])
print(find_emails()[1])
print(f'\nThere are {find_emails()[2]} unique e-mail addresses in this file!\n')

###############################################################################################

def find_timestamps():
    f_name = "mbox.txt"
    with open(f_name, "r") as shortf:
        raw_list = []
        for line in shortf:
            line = line.rstrip()
            if line.startswith("From "):
                operation = re.search(r"[A-Z][a-z]+\s[A-Z][a-z]+\s+\d+\s\d\d:\d\d:\d\d\s\d{4}", line)
                if operation:
                    raw_list.append(operation)
        count = 0
        date_time = []
        for k in raw_list:
            count += 1
            # 1. Use .group() to get the full matched string
            full_string = k.group() 
            # 2. Split the string by spaces to get a list
            parts = full_string.split()
            # 3. Use [-1] on the resulting list (not the match object)
            date_time.append(f"{parts[0]} {parts[1]} {parts[2]} {parts[3]} {parts[4]}")
        return raw_list, "\n".join(date_time[:20]), count, f_name
    
raw_list, date_times, counts, f_name = find_timestamps()
print(raw_list[:5])
print(f"\n{date_times}\n....")
print(f"\nThere are total {counts} timestamps in {f_name} file.")

###############################################################################################

