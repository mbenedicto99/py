import json, requests

response = requests.get("http://jsonplaceholder.typicode.com/comments")

#CODE Resultado
print(response.status_code)
# print (response.content)

comments = json.loads(response.content)

# Objeto especifico

print (comments[0]['body'])
s = " separador "
print (s.center(30, '%'))
print (comments[0]['name'])
print (s.center(30, '%'))

# for comment in comments[0:10]:
#	print comment['name']