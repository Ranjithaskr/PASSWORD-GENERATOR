import random
import string

def generate_password(length):
    
    uppercase_letters=string.ascii_uppercase
    lowercase_letters=string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    
    password =''.join(random.choice(all_characters)for _ in range(length))

    return password
        
   
def main():
    
    try:
        length = int(input(" Enter the desired length of the password:"))
        if length < 1:
            print("password length must be at least 1 character.")
            return
        
        
        password = generate_password(length)
        print(f"Generated Password:{password}")

    except ValueError:
        print("Invalid input. please enter a positive integer.")  


if __name__  == "__main__":
   main()
