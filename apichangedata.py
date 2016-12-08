#!/usr/bin/python

dados = {"email": "john@doe.com"}
response = requests.put("http://jsonplaceholder.typicode.com/comments/10", data=dados)

response = requests.delete("http://jsonplaceholder.typicode.com/comments/10")

response = requests.get("http://jsonplaceholder.typicode.com/posts/2/comments")
