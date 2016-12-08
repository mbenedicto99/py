#!/usr/bin/python

import json, requests

response = requests.get("http://jsonplaceholder.typicode.com/comments")

print response.status_code

#print response.content

comments = json.loads(response.content)

print comments[0] ['body']

for comment in comments[0:10]:
	print comment['name']

#Objeto especifico


response = requests.get("http://jsonplaceholder.typicode.com/comments")

comment = json.loads (response.content)

print comment[0] ['name']
