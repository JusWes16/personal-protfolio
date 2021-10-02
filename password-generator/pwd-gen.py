# The random library allows this program to find random characters from a list of characters
import random
# The os library is the miscellaneous operating system interfaces library. It covers a lot of 
# operating system functionality and is used in this program to separate passwords in a file by 
# a blank line.
import os

# Initiates a class called Password to hold all of the password generator code
class Password:
    # The __init__() function is used to create a new instance of the Password class. 
    # To create an instance of the Password class it needs three variables to be passed in,
    # default_characters, run (true or false), and a file
    def __init__(self, default_characters, run, file):
        self.run = run
        self.default_characters = default_characters
        self.file = file

    # The pwd_generator() method is the function that is called to create the passwords. It is passed the 
    # self parameter which allows it to access the variables defined in the __init__() function
    def pwd_generator(self):
        # While loop runs until run is set equal to False
        while self.run:
            # Gets password length and number of passwords from the user
            pwd_length = int(input("How long would you like your secure password to be?: "))
            pwd_count = int(input("How many passwords would you like to generate?: "))
            # Sets a variable password_list to hold all of the created passwords
            password_list = []

            # Gets users choice to use default characters or input their own
            custom_chars_choice = input("Would you like to use a default list of characters? (alternative - you enter what characters you want in your passwords) (y or n): ")

            # If Elif statement executes 2 different password generation processes based on their answer to the question about
            if custom_chars_choice.capitalize() == "Y":
                # Loops through the pwd_count and pwd_length based on the values given above. password_char is chosen randomly 
                # from default_characters and combind to make one password. That password it appended to the password_list.
                # Run is set to False once all of the passwords have been generated to end the loop.
                for x in range(0, pwd_count):
                    password = ""
                    for x in range(0, pwd_length):
                        password_char = random.choice(self.default_characters)
                        password += password_char
                    password_list.append(password)
                    self.run = False
            elif custom_chars_choice.capitalize() == "N":
                # The user enters a string of desired characters without any spaces between them.
                user_input = input("What characters would you like to include in your password? (enter them all in one line and without any spaces): ")

                # The string of characters is looped through and converted to an array 
                custom_chars = [char for char in user_input]

                # This for loops does the same thing as the one above only using the custom_chars instead of the 
                # default_chars
                for x in range(0, pwd_count):
                    password = ""
                    for x in range(0, pwd_length):
                        password_char = random.choice(custom_chars)
                        password += password_char
                    password_list.append(password)
                    self.run = False

        # Opens the file that was passed in when the class was initialized and prepares to write to it. 
        # The list of passwords, password_list, is converted into an enumerated object, [(0, password1), (1,password2), ...]
        # the index + 1 and the password are written to the file. os.linesep inserts a new line after each password for readability
        with open(self.file, 'w') as f:
            for idx, password in enumerate(password_list):
                f.write(f"{idx + 1}) {password} {os.linesep}")

# Declaration of 2 files. One for the default characters the other for the finished password list
file1 = "passwords.txt"
file2 = "random_chars.txt"

# Opens and reads the random_chars.txt file and converts the contents into a Python list
with open(file2, 'r') as f:
    default_characters = [char for char in f.read()]

# Initializes a new instance of the Password class passing in the 3 variables required
passwords = Password(default_characters, True, file1)
# Calls the pwd_generator() method in the Password class
passwords.pwd_generator()