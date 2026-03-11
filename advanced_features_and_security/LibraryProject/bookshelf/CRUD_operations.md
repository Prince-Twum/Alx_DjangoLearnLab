# CRUD Operations in Django Shell

## 1. Create

Python Command:
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book

Expected Output:
<Book: 1984>

---

## 2. Retrieve

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

---

## 3. Update
## Update Book

from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Check updated title
book.title

# Expected Output:
'Nineteen Eighty-Four'

---

## 4. Delete

## Delete Book

from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Check that no books remain
Book.objects.all()

# Expected Output:
<QuerySet []>