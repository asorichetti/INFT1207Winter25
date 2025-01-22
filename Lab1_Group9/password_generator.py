##########################################################
# Name: Alex Sorichetti
# Student ID: 101000609
# Description: A program to create a random secure password
###########################################################

import random
import string

#Finds random letters, numbers, and symbols for password
def password_inputs(password_length):
    password_checker = 0
    #check that password components are within desired length, and that user input is valid
    while password_checker == 0:
        try:
            a = int(input("please input the total amount of letters: "))
            b = int(input("Please input the total amount of numbers: "))
            c = int(input("Please input the total amount of symbols: "))
            if a+b+c == password_length:
                password_checker = 1
            else:
                print("Sorry, the numbers you entered do not add up to your desired password length. \n Please be sure to enter values that will total your desired password length.")
        except ValueError:
            print("Please only input numbers for the prompts, not letters or symbols.")
    for i in range (0,a,1):
        password_holder.append(random.choice(string.ascii_letters))
    for i in range (0,b,1):
        password_holder.append(random.choice(string.digits))
    for i in range(0,c,1):
        password_holder.append(random.choice(string.punctuation))

#Function to join list password_holder into final password
def password_joiner():
    #Shuffles the list into a random order
    random.shuffle(password_holder)
    password = "".join(password_holder)
    return(password)

def write_output_file(file_name, password):
     with open (file_name, "w") as file:
        file.write(f"Password: {password}\n")



print("Welcome to the Random Password Generator!")
password_checker = 0
#Check if password length is in range and make sure user input is valid
while password_checker == 0 :
    try:
        password_length = int(input("Please input the total length of your password (Minimum of 8 Characters, Maximum of 20): "))
        if 8 <= password_length <= 20:
            password_checker = 1
        else:
            print("Inputted number outside range, please input a number from 8 to 20.")
    except ValueError:
        print("Please input a numeric value and not a string.")
password_holder = []
password_inputs(password_length)
password = password_joiner()
print("Strong Password: ", password)
write_output_file("Lab1_Group9\Output.txt", password)
print("\n Password successfully written to 'Output.txt'")
