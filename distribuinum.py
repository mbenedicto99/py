#!/usr/bin/python

numbers = [12,23,34,432,12,4,23,5,23]

even = []
odd = []

while len(numbers) > 0 :
	number = numbers.pop()
	if(number % 2 == 0):
		even.append(number)
	else:
		odd.append(number)
print(even)
print(odd)
