#!/usr/bin/python

import json, requests

dados = data={"postId": 1, "name": "John Doe", "email": "john@doe.com", "body": "This is it!"}
response = requests.post("http://jsonplaceholder.typicode.com/comments/", data=dados)

print response.status_code

print response.content
