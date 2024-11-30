import hashlib
import getpass

# We are using a dictionnary as a password manager
# Other possibilities are available but for a first project we'll use this

# Structure of the dict_dict_storage = {(username,hashed_password); {Platform;(username,password)} }

# Cons of this structure : Cannot add 2 accounts for the same platform

dict_storage = {}

## ------------------------------------------ STEP 1 Functions ------------------------------------------ ##
def create_account(username : str,password : str):
    # Manage username and password 
    
    password_verify = getpass.getpass("Please verify your password : ")
    
    # Manage password verification
    while not (password == password_verify):
        print("Warning : Your two passwords are needed to be the same ! \n")
        password = getpass.getpass("Enter your password : ")
    
        password_verify = getpass.getpass("Please verify your password : ")
        print("\n")
        
    # Store password using the sha256 algorithm 
    # password.encode() converts str(password) to bytes which is the input of hashlib.sha256 function
    # hexdigest converts the output to a human-readable language
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    dict_storage[(username,hashed_password)] = {}
    print("************************")
    print(f"Your account has been successfully created with {username} as its username !")
    print("---------------------------------------------------------")


# Returns the stored passwords dict of the account 
def login(username : str,password : str):  
    
    tries = 1
    
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    while ((username,hashed_password) not in dict_storage.keys() and tries < 3):
        print(f"Warning : Incorrect username or password, you only have {3-tries} tries left")
        print("---------------------------------------------------------")
        username = input("Enter your username : ")
        password = getpass.getpass("Enter your password : ")
        tries += 1
    
    if (tries == 3):
        print("You have been unsuccessfully logged in... Try again later")
        print("---------------------------------------------------------")
        return False

    else : 
        print("You have been successfully logged in !")
        print("---------------------------------------------------------")
        return dict_storage[(username,hashed_password)]

## ------------------------------------------ STEP 2 Functions ------------------------------------------ ##

def add_platform(account_dict : dict):

    platform = input("Enter a platform to add to the data base : ")
    
    if not (platform in account_dict.keys()):
        plat_user = input("Enter the username used : ")
        plat_password = getpass.getpass("Enter your password : ")
        
        account_dict[platform] = (plat_user,plat_password)
    
        print(f"{platform} has been successfully added ! ")
        print("---------------------------------------------------------")

    else:
        print("You cannot have two accounts for the same platform !")
        mod = input("Would you like to modify it ? (Yes/No) ")
        if (mod == "Yes"):
            step = input("What do you want to modify 1 for username, 2 for password ? ")
            modify(account_dict,int(step),platform)
        else:
            print("---------------------------------------------------------")
            
def show_all(account_dict : dict):
        print("---------------------------------------------------------")
        print("Platforms and usernames : ")
        print("************************")
        for platform in account_dict.keys():
            print(f"Platform : {platform} - username : {account_dict[platform][0]}")
        print("---------------------------------------------------------")
    
def find(account_dict : dict):
    print("---------------------------------------------------------")
    platform = input("Which platform are you looking for ? ")
    print("\n")
    if platform in account_dict:
        print(f"Platform : {platform}")
        print(f"Username : {account_dict[platform][0]}")
        print(f"Password : {account_dict[platform][1]}")
        print("---------------------------------------------------------")
        return account_dict[platform]
    else :
        print("Your platform has not been found")
        print("---------------------------------------------------------")
        return False
    
def modify(account_dict : dict,step3 : int, platform : str):
    print("---------------------------------------------------------")
    if step3 == 1: # Modify username 
        new = input("What new username do you want ? ")
        account_dict[platform] = (new,account_dict[platform][1])
    else : # Modify password 
        new = getpass.getpass("What new password do you want ? ")
        account_dict[platform] = (account_dict[platform][0],new)
    print("Your modification has been successful !")
    print("---------------------------------------------------------")

    
def suppress(dict_account : dict, platform : str):
    del dict_account[platform]
    print("Suppression successful")
    print("---------------------------------------------------------")

    
def main():
    
    print("-------- Welcome to your python password manager ! --------")
    print(" \n")
    while True:
        print("***********MENU***********")
        print("Enter :")
        print("1. Create an account ")
        print("2. Login into your account")
        print("3. Exit")
        print("************************")

        step1 = input("Write the number of the action you want to do : ")
        print("---------------------------------------------------------")

        while  not (step1.isdigit()):
            print(" \n")
            print("Warning : Your answer has to be a digit ! ")
            print("***********MENU***********")
            print("Enter :")
            print("1. Create an account ")
            print("2. Login into your account")
            print("3. Exit")
            print("************************")

            step1 = input("Write the number of the action you want to do : ")
            print("---------------------------------------------------------")    
        
        step1 =  int(step1) 
        
        if step1 == 1 or step1 == 2: 
            
            # Creating an account also comes with a logged session just after 
            username = input("Enter your username : ")
            password = getpass.getpass("Enter your password : ")
            if step1 == 1 :
                create_account(username,password)
                dict_account = login(username,password)
            else:
                dict_account = login(username,password)
                if(dict_account == False):
                    print("***********MENU***********")
                    print("Enter :")
                    print("1. Create an account ")
                    print("2. Login into your account")
                    print("3. Exit")
                    print("************************")

                    step1 = input("Write the number of the action you want to do : ")
                    print("---------------------------------------------------------")   
                else :
                    while True:
                        print("\n")
                        print("***********MENU***********")
                        print("1. View all your platforms and usernames ")
                        print("2. Modify a platform ")
                        print("3. Add a new platform")
                        print("4. Suppress a platform")
                        print("5. Find a specific platform")
                        print("6. Loggout")
                        print("************************")
                        step2 = input("What do you want to do ? ")
                        
                        while  not (step2.isdigit()):  
                            print("\n")
                            print("Warning : Your answer has to be a digit ! ")
                            print("***********MENU***********")
                            print("1. View all your platforms and usernames ")
                            print("2. Modify a platform ")
                            print("3. Add a new platform")
                            print("4. Suppress a platform")
                            print("5. Find a specific platform (username + password)")
                            print("6. Loggout")
                            print("************************")
                            step2 = input("What do you want to do ? ")
                        
                        step2 = int(step2)
                        
                        if step2 == 1:
                            show_all(dict_account)
                        elif step2 == 2:
                            platform = input("Which platform are you looking for ? ")
                            step3 = input("What do you want to modify 1 for username, 2 for password ? ")
                            modify(dict_account,int(step3),platform)
                        elif step2 == 3:
                            add_platform(dict_account)
                        elif step2 == 4:
                            platform = input("Which platform are you looking for ? ")
                            suppress(dict_account,platform)
                        elif step2 == 5:
                            find(dict_account)
                        else: 
                            print("---------------------------------------------------------")
                            print("Logged out!")
                            print("---------------------------------------------------------")
                            break               
        else:
            print("Thanks for using PYTHON password manager ! ")
            return True
        

## ----------------------------------- MAIN ----------------------------------- ## 
if __name__ == '__main__':
    main()