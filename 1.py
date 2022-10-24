#!/usr/bin/python

#Tutorial de Python: https://www.geeksforgeeks.org/python-string-replace/?ref=leftbar-rightbar

tst=['89231','312','-03-','jhfskhfskh']

for i in tst:
	print (i)

#Inserindo variavel na lista
tst.append('hdkdks')

#Pesquisando a nova variavel no array
#print(tst[4])

for ARG	in tst:
	print (ARG)

#testando de numero é maior que 300
if tst[1] > '300':
	print ('Ops numero')
	print (tst[1])

	print ('------')

#Captura tipo de variavel
val1 = input("Enter the name: ")

# print the type of input value
print(type(val1))
print(val1)

#Substitui STRING
string = "grrks FOR grrks"

# replace all instances of 'r' (old) with 'e' (new)
new_string = string.replace("r", "e" )

print(string)
print(new_string)

#Substitui palavras
string = "geeks for geeks \ngeeks for geeks"

print(string)

# Prints the string by replacing only
# 3 occurrence of Geeks
print(string.replace("geeks", "GeeksforGeeks"))

#Substitui numero especifico de letras
string = "geeks for geeks geeks geeks geeks"

# Prints the string by replacing
# e by a
print(string.replace("e", "a"))

# Prints the string by replacing only
# 3 occurrence of ek by a
print(string.replace("ek", "a", 3))

print ('-----')

#validando email
email = 'userxyz.com@domain.com'
last_dot_pos = email.rfind('@', 1)
tld_string = email[last_dot_pos:]

if tld_string == "@domain.com":
	print("Email matched, tld:", tld_string)
else:
	print("Email not matched, tld:", tld_string)