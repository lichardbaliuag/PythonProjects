# Connecting API with Authentication
'''
# With Authentication
#!/usr/bin/env python

import requests
from requests_ntlm import HttpNtlmAuth

username = '<DOMAIN>\\<UserName>'
password = '<Password>'
tfsApi = 'https://{myserver}/tfs/collectionName/_apis/projects?api-version=2.0'

tfsResponse = requests.get(tfsApi,auth=HttpNtlmAuth(username,password))
if(tfsResponse.ok):
    tfsResponse = tfsResponse.json()
    print(tfsResponse)
else:
    tfsResponse.raise_for_status()
'''
# Import modules
import random
import requests

# Saving the URL in a variable
url = "https://icanhazdadjoke.com/search"

# Create a function to get a user input for type of joke
# Then taking that input and searching the API for that topic and returning a random joke
def get_joke():
    # Gets user input for the term to search using GET request
    search_term = input("Let me tell you a joke, give me a topic: ")

    # Get request with JSON header and parameter term to search from users input
    response = requests.get(
        url,
        headers = {
            "Accept": "application/json"
        },
        params = {
            "term": search_term
        }
    )

    if(response.ok):
        print(response)
    else:
        response.raise_for_status

    # converts the JSON file to a python dict
    data = response.json()

    # Uses the key total_jokes from dict to get a value
    total = data["total_jokes"]

    # Based on if a joke on the search term was found and how many, will return the joke from the
    # request. Data is a dictionary, results is a key that returns a list value that holds dictionaries.     
    if total == 1:
        print(f"I have got one joke about {search_term}.")
        print(data["results"][0]["joke"])

    # Selects a random joke from total ammount of jokes found if there is more than one
    elif total > 1:
        print(f"I have found {total} jokes about {search_term}.")
        rund_num = random.randint(0, total - 1)
        print(data["results"][rund_num]["joke"])

    # No joke
    else:
        print(f"I'm sorry, could not find any joke for {search_term}.")

get_joke()


