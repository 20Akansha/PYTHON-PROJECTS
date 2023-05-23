import random

print("Welcome to Password Generator ")

characters="abcdefghijklmnopqrstuvwxyz12345678910.,ABCDEFGHIJKLMNOPQRSTUVWXYZ$%^&*@#()><"
num=int(input("How many passwords you want ? : "))

len=int(input("What should be length of your password ? : "))

print("These are your Passwords : ")

for pwd in range(num):
  passwords=""
  for p in range(len):
    passwords+=random.choice(characters)
  print(passwords)  
