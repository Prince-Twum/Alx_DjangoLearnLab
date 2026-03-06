## Retrieve Book

from bookshelf.models import Book

# Retrieve all books
Book.objects.all()

# Retrieve the specific book using get
b = Book.objects.get(title="1984")
b.title
b.author
b.publication_year

# Expected Output:
<Book: 1984>
'Nineteen Eighty-Four'  
'George Orwell'
1949