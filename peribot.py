import json
from webbot import Browser

# Load configuration from config.json file
with open('config.json') as config_file:
    config = json.load(config_file)

# Extract values from the config
address = config['address']
username = config['username']
password = config['password']

# Create a browser instance
web = Browser()
web.go_to(address)

# Fill in the login form
web.type(username, into='username_field_id')
web.type(password, into='password_field_id')

web.click('Submit')

# Perform additional actions on the logged-in page

web.close()
