# Create a Python script that performs the following:
# Prompt the user to type a string input as the variable for your destination URL.
# Prompt the user to select a HTTP Method of the following options:
# GET
# POST
# PUT
# DELETE
# HEAD
# PATCH
# OPTIONS
# Print to the screen the entire request your script is about to send. Ask the user to confirm before proceeding.
# Add some comments of what these request are doing to your script
# Using the requests library, perform a GET request to your github.
# For the given header, translate the codes into plain terms that print to the screen; for example, a 404 error should print Site not found to the terminal instead of 404.
#response = requests.get()
# For the given URL, print response header information to the screen.

from urllib import response
import requests

# Prompt the user to enter a destination URL
url = input("Enter the destination URL: ")

# Prompt the user to select an HTTP Method
b = input("Choose Method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ")

# Display the entire request to the user and ask for confirm
print(f"\nPreparing to send {b} request to {url}\n")

# Confirm before proceeding
confirm = input("Do you want to proceed? (yes/no): ").lower()

if confirm != 'yes':
    print("Request canceled.")
    exit()

# Perform the HTTP request using the requests library
response = requests.request(b, url)

# Translate HTTP status codes to plain terms
status_code = {
    200: 'OK',
    201: 'Created',
    204: 'No Content',
    400: 'Bad Request',
    401: 'Unauthorized',
    403: 'Forbidden',
    404: 'Not Found',
    405: 'Method Not Allowed',
    500: 'Internal Server Error',
}

# Print translated status message
message = status_code.get(response.status_code, 'Unknown Status')
print(f"\nResponse Status: {response.status_code} - {message}\n")