# import requests
# # from swagger_parser import SwaggerParser
# from swagger_parser import Sw
# # URL of the Swagger specification
# swagger_url = 'https://path.to/swagger.json'
#
# # Parse the Swagger specification
# parser = SwaggerParser(swagger_path=swagger_url)
#
# # Get all endpoints from the Swagger specification
# endpoints = parser.paths
#
# # Function to make a request to an endpoint
# def make_request(method, url, params=None, data=None):
#     response = requests.request(method, url, params=params, json=data)
#     return response
#
# # Iterate over each endpoint and make a request
# for path, methods in endpoints.items():
#     for method, details in methods.items():
#         url = f"{parser.specification['host']}{path}"
#         response = make_request(method, url)
#         print(f"Endpoint: {method.upper()} {url}")
#         print(f"Status Code: {response.status_code}")
#         print(f"Response: {response.text}\n")
#
# import requests
# from openapi_parser import *
#
# # URL of the Swagger specification
# swagger_url = 'https://petstore.swagger.io/v2/swagger.json'
#
# # Parse the Swagger specification
# parser = OpenAPIParser.from_file(swagger_url)
#
# # Get all endpoints from the Swagger specification
# endpoints = parser.paths
#
# # Function to make a request to an endpoint
# def make_request(method, url, params=None, data=None):
#     response = requests.request(method, url, params=params, json=data)
#     return response
#
# # Iterate over each endpoint and make a request
# for path, methods in endpoints.items():
#     for method, details in methods.items():
#         url = f"{parser.specification['host']}{path}"
#         response = make_request(method, url)
#         print(f"Endpoint: {method.upper()} {url}")
#         print(f"Status Code: {response.status_code}")
#         print(f"Response: {response.text}\n")

import requests
import json
from openapi_spec_validator import validate_spec
# from openapi_spec_validator.schemas import read

# URL of the Swagger specification
swagger_url = 'https://petstore.swagger.io/v2/swagger.json'

# Fetch the Swagger specification
response = requests.get(swagger_url)
swagger_spec = response.json()

# Validate the Swagger specification
try:
    validate_spec(swagger_spec)
    print("Swagger specification is valid.")
except Exception as e:
    print(f"Swagger specification is invalid: {e}")
    exit()

# Function to make a request to an endpoint
def make_request(method, url, params=None, data=None):
    response = requests.request(method, url, params=params, json=data)
    return response

# Get all endpoints from the Swagger specification
for path, methods in swagger_spec['paths'].items():
    for method, details in methods.items():
        url = f"{swagger_spec['host']}{path}"
        response = make_request(method, url)
        print(f"Endpoint: {method.upper()} {url}")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}\n")
