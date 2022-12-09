import requests
""" A script that shows how to query an api and get a list of available operations. 
It also creates a generic function to do the operations and provide examples
of how to call the operations on that api. 
"""

# Base URL for the API
BASE_URL = 'https://api.example.com/v1'

# Function to query the API
def query_api(endpoint, method='GET', params=None, data=None):
  # Construct the full URL for the API endpoint
  url = f'{BASE_URL}/{endpoint}'

  # Send a request to the API with the specified method, query parameters, and data
  response = requests.request(method, url, params=params, json=data)

  # Return the response from the API
  return response.json()

# Function to get the list of available operations from the API
def get_operations():
  # Query the API to get a list of available operations
  response = query_api('operations')

  # Return the list of available operations
  return response['operations']

# Generic function to call an operation on the API
def call_operation(operation, params=None, data=None):
  # Query the API to call the specified operation with the given parameters and data
  return query_api(operation, params=params, data=data)

# Example client function to get a list of users from the API
def get_users():
  return call_operation('users')

# Example client function to get a specific user from the API
def get_user(user_id):
  return call_operation(f'users/{user_id}')

# Example client function to update a user's name in the API
def update_user_name(user_id, name):
  # Use the 'PUT' method to update the user's name in the API
  return call_operation(f'users/{user_id}', method='PUT', data={'name': name})
