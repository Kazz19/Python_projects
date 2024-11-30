import random as rd 
import string
import uuid  

def generator():
    
    rd.seed(bin(uuid.getnode())) # seed based on the mac address of the executing device (normally)

    # Input management with error cases 
    length = input("Enter the length required: ")
    while not (length.isdigit() and int(length) >= 12):
        if not length.isdigit():
            print("Warning: Length has to be an integer!\n")
        elif int(length) < 12:
            print("Warning: Length must be at least 12!\n")
        length = input("Enter the length required: ")
    
    # Conversion type of length
    length = int(length)
    
    print("------ What do you want to have in your password ? ------\n")
    print("1. Letters (Upper and lower letters Aa) only \n")
    print("2. With digits (Aa1)\n")
    print("3. With symbols (Aa1%)\n")
    print("---------------------------------------------------------")
    alphabet_type = input("Write your answer here : ")
    
    while not(alphabet_type.isdigit()):
        print("Warning : Your answer has to be between 1 and 3 \n")
        print("------ What do you want to have in your password ? ------\n")
        print("1. Letters (Upper and lower letters Aa) only \n")
        print("2. With digits (Aa1)\n")
        print("3. With symbols (Aa1%)\n")
        print("---------------------------------------------------------")
        alphabet_type = input("Write your answer here : ")
    
    if alphabet_type == "1":
        alphabet = string.ascii_letters
    elif alphabet_type == "2":
        alphabet = string.ascii_letters + string.digits 
    elif alphabet_type == "3":
        alphabet = string.ascii_letters + string.digits + string.punctuation

    # Available string for the password generated including 
    # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~

    # Generates the password by taking random choices in the alphabet length times 
    password = ''.join(rd.choice(alphabet) for i in range(length))
    
    print(f"Your password has been successfully created here : {password}")
    
    return password 
    
## ----------------------------------- MAIN ----------------------------------- ## 

if __name__ == '__main__':
    new_pass = generator()