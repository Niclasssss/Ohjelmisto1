kt = "python"
salasana = "rules"

i = 1
while i <= 5:
    yritys1 = input("Enter username: ")
    yritys2 = input("Enter password: ")
    if yritys1 == kt and yritys2 == salasana:
        print("Welcome")
        break
    else:
        print("Incorrect username or password. Please try again.")
        i = i + 1
if i > 5:
    print("Access denied")