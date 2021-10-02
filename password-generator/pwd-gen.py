import random
import os

class Password:
    def __init__(self, default_characters, run, file):
        self.run = run
        self.default_characters = default_characters
        self.file = file

    def pwd_generator(self):
        while self.run:
            pwd_length = int(input("How long would you like your secure password to be?: "))
            pwd_count = int(input("How many passwords would you like to generate?: "))
            password_list = []

            custom_chars_choice = input("Would you like to use a default list of characters? (alternative - you enter what characters you want in your passwords)(y or n): ")

            if custom_chars_choice.capitalize() == "Y":
                for x in range(0, pwd_count):
                    password = ""
                    for x in range(0, pwd_length):
                        password_char = random.choice(self.default_characters)
                        password += password_char
                    password_list.append(password)
                    self.run = False
            elif custom_chars_choice.capitalize() == "N":
                user_input = input("What characters would you like to include in your password? (enter them all in one line and without any spaces): ")

                custom_chars = [char for char in user_input]

                for x in range(0, pwd_count):
                    password = ""
                    for x in range(0, pwd_length):
                        password_char = random.choice(custom_chars)
                        password += password_char
                    password_list.append(password)
                    self.run = False

        with open(self.file, 'w') as f:
            for idx, password in enumerate(password_list):
                f.write(f"{idx + 1}) {password} {os.linesep}")

file1 = "passwords.txt"
file2 = "random_chars.txt"

with open(file2, 'r') as f:
    default_characters = [char for char in f.read()]

passwords = Password(default_characters, True, file1)
passwords.pwd_generator()