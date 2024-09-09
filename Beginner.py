# Lets user know what this program will do
print("Please login");

# Opens accounts txt file
user_file = open("user.txt", "r")

# Flag to terminate while loop
log_in_status = False
# Runs loop until username and password are correct
while log_in_status == False:
    # Asks user for username and stores as variable
    usernameInput = input("Username:");
    # Asks user for password and stores as variable
    passwordInput = input("Password:");
    # Reads each line of the text file line by line
    # admin, adm1n
    for line in user_file:
        # Stores each line in file as a username/password combo
        username, password = line.split(sep=", ")
        # If username and password match, breaks out of the loop and sets complete to  True
        if usernameInput == username and passwordInput == password:
            complete = True
            break
        # Sets complete to False and loops back    
        else:
            complete = False
            continue
if complete == True:
    print("Welcome to the GitHub remote version!"); #Optimized the print function