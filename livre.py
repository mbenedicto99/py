s='Beginning'
a=s.find('nig')
b=s.count('n')
c=len(s)
d=s.isupper()

#print (s.replace('n','N',d))

#LAMBDA TEST

books = [
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "Animal Farm", "author": "George Orwell", "year": 1945},
]

sorted_books = sorted(books, key=lambda x: x['title'])

for book in sorted_books:
    print(book)