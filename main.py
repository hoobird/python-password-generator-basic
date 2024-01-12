# Write you random password generator program here!
import random

def generate_password():
  characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!\"#$%&'()*+, -./:;<=>?@[\\]^_`{|}~"
  
  password_length = int(input("Enter the password length: "))
  password = ''.join(random.choice(characters) for i in range(password_length))
  
  print(f"Your generated password is: {password}")

generate_password()