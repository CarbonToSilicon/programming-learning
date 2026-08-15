# name = input(f"What is your name?\n")

# with open("Names.txt", "a") as file:

#     file.write((f"{name}\n"))

# #file.close() 
         ############################
#with open("Names.txt", "r") as read_file:
#     lines = read_file.readlines()
#     print(type(lines))
# for line in lines:
#     print("Hello,", line)
        ############################
# with open("Names.txt", "r") as read_file:
#     for line in read_file:
#         print("Hello,", line.rstrip())
                ###################
#
    #############################
# while True:
#     try:
#         status = input(f"Enter:\n1. For Sign in\n2. For Sign up\n")
#     except:
#         print("Input must be either '1' or 2''!")
    
#     if status == "2":
#         try:
#             username = input(f"Username can have characters from 5 to 15.\nEnter your username to login: ")
#             if len(username) < 15 and len(username) > 4:
#                 pass
#         except:
#             print("Please enter a valid username")

#         try:
#             t1 = '~!@#$%^&*()-_;:/<>?]'
#             t2 = 'QWERTYUIOPASDFGHJKLZXCVBNM'
#             t3 = "qwertyuiopasdfghjklzxcvbnm"
#             t4 = "1234567890"
#             password = input(f"Password must contain 4 types of characters (&, A, a, 1) and the length should be from 4 to 12 character\nEnter password:")
#             if any(c in t1 for c in password) and any(c in t2 for c in password) and any(c in t3 for c in password) and any(c in t4 for c in password) and len(password) > 2 and len(password) < 12)):
                
#     elif status == '1':
#             usernamel = input(f"Enter your username: ")
#             passwordl = input(f"Enter your password: ")
#     except:
#         print('g')

######################################################


# ... (Keep your t1-t4 variables and sha_128_custom function here) ...

# while True: # THE MAIN APP LOOP
#     print("\n--- MAIN MENU ---")
#     status = input("Enter:\n1. For Sign in\n2. For Sign up\n3. To Exit\n")
    
#     if status == '3':
#         print("Goodbye!")
#         break # Exits the whole app

#     if status == "2":
#         # --- SIGN UP LOGIC ---
#         # (Your existing username and password loops go here)
#         # ...
#         with open("secret_notes_accounts.csv", "a") as filepass:
#             hashed_p = sha_128_custom(password)
#             filepass.write(f"{username},{hashed_p}\n")
#         print("Registration complete! You can now sign in.")
#         # Notice: No 'break' here, so it loops back to the Main Menu

#     elif status == '1':
#         # --- SIGN IN LOGIC ---
#         while True:
#             u_match = input("Username: ")
#             p_match = input("Password: ")
#             p_encoded = sha_128_custom(p_match)
            
#             success = False
#             # ... (Your existing file reading logic) ...
            
#             if success:
#                 print(f"Access Granted to Secret Notes!")
#                 # Here is where you'd call your next function!
#                 break 
#             else:
#                 print("Try again or type 'exit' to go back.")
#                 if u_match == 'exit': break

#     else:
#         print("Invalid selection.")




# import os

# # ... (Inside your 'if success' block) ...

# if note_choice == "1":
#     # 1. Open Notepad for the user to write their notes
#     # We create an empty or existing temp file for them to edit
#     temp_filename = "temp_edit.txt"
#     user_marker = f"[{encoded_attempt_p}]"
    
#     # Extract current notes to the temp file first so they can see/edit them
#     with open("master_notes.txt", "r") as master, open(temp_filename, "w") as temp:
#         found_section = False
#         for line in master:
#             if line.strip() == user_marker:
#                 found_section = True
#                 continue
#             if found_section:
#                 if line.startswith("["): break # Hit next user
#                 temp.write(line)

#     print("Opening Notepad... Save and Close to update your notes.")
#     os.system(f"notepad.exe {temp_filename}")

#     # 2. READ the master file into the 'Sandwich' variables
#     header = ""
#     footer = ""
#     state = "HEADER"

#     with open("master_notes.txt", "r") as master:
#         for line in master:
#             if line.strip() == user_marker:
#                 state = "USER_SECTION"
#                 header += line # Keep the marker in the header
#                 continue
            
#             if state == "USER_SECTION" and line.startswith("["):
#                 state = "FOOTER"
            
#             if state == "HEADER":
#                 header += line
#             elif state == "FOOTER":
#                 footer += line

#     # 3. RE-ASSEMBLE the file
#     with open(temp_filename, "r") as temp:
#         new_user_data = temp.read()

#     with open("master_notes.txt", "w") as master:
#         master.write(header)           # Bottom slice of bread
#         master.write(new_user_data)    # The meat (updated notes)
#         if not new_user_data.endswith('\n'): master.write('\n')
#         master.write(footer)           # Top slice of bread

#     print("Master file updated successfully!")
#     os.remove(temp_filename) # Clean up the evidence




    # elif status == '1':
    #     # --- SIGN IN LOGIC ---
    #     while True:
    #         print("\n--- Login Screen (Type 'exit' to go back) ---")
    #         username_match = input("Enter your username: ")
    #         if username_match.lower() == 'exit': break # Escape hatch
            
    #         password_match = input("Enter your password: ")
    #         encoded_attempt_p = sha_128_custom(password_match)

    #         success = False

    #         try:
    #             with open("secret_notes_accounts.csv", "r") as f:
    #                 for line in f:
    #                     if "," not in line: continue 
    #                     stored_user, stored_pass = line.strip().split(",")
                        
    #                     if username_match == stored_user and encoded_attempt_p == stored_pass:
    #                         success = True
    #                         break 
    #         except FileNotFoundError:
    #             print("Error: No accounts found. Please sign up first.")
    #             break 

    #         if success:
    #             print(f"Login successful! Welcome {username_match}.")
    #             # This is where the actual "Secret Notes" logic would start
    #             break 
    #         else:
    #             # IMPORTANT: Tell the user it failed so they aren't confused
    #             print("!!! Invalid username or password. Please try again. !!!")

