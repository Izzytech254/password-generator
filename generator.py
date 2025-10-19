import random
import string
print("Smart Password Generator")
length = int(input("enter the desired password length: "))
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for i in range(length))
print(f"\nYour new strong password is:\n  {password}")
