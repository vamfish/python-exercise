import re

userreg = re.compile(r"[!@#$%^&*]")
filereg = re.compile(r"[^!?@$%#]\.txt")

check = input("What do you want to check: Username or Filename? ")

if check == "Username":
    username = input("Please enter a Username: ")
    result = userreg.search(username)
    if result:
        print("Your Username is invalid! Recheck it!")
    else:
        print("Your Username is valid! Congratulations!")
elif check == "Filename":
    filename = input("Please enter a Filename (ended with .txt): ")
    result = filereg.search(filename)
    if result:
        print("Your Filename is valid! Congratulations!")
    else:
        print("Your Filename is invalid! Recheck it!")
else:
    print("This is not checkable!")