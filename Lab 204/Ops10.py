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