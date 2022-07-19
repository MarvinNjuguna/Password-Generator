#This program creates different unique passwords based the number of passwords a user would prefer
import random

random_chars = "abcdefghiklmnopqrstvxyzABCDEFGHIKLMNOPQRSTVXYZ0123456789!@#$%"

while 1:
  password_len = int(input("How long would you like your password: "))
  password_count = int(input("How many passwords would you like: "))
  for x in range(0, password_count):
    password = ""
    for x in range(0, password_len):
      password_char = random.choice(random_chars)
      password = password + password_char
    print("Your password is: {}".format(password))