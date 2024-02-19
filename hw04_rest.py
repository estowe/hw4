#!/bin/python3
import requests

# Replace with your GitHub token
TOKEN = 'your_github_token'

# Headers for authorization and setting response content type to JSON
headers = {
    'Authorization': f'token {TOKEN}',
    'Accept': 'application/vnd.github.v3+json',
}

def get_user(username):
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def create_repo(repo_name):
    url = 'https://api.github.com/user/repos'
    data = {
        'name': repo_name,
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        return response.json()
    else:
        return None

# Test the functions
print(get_user('octocat'))
print(create_repo('test-repo'))
