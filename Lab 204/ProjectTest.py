import random
import string


def generate_email(name):
    # Convert the name to lowercase and remove spaces
    clean_name = name.lower().replace(" ", "")
    
    # Generate the email address
    email = f"{clean_name}@example.com"
    
    return email

# Get user input for the name
user_name = input("Enter your first and last name: ")

# Generate the email
user_email = generate_email(user_name)

pass

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation


def generate_password(length=8):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password using the specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Call the function to generate and display the password
generated_password = generate_password()


# Display the generated email
print(f"Your company email address is: {user_email}")
print(f"Your temporary password is: {generated_password}")