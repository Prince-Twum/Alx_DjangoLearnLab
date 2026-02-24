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

Python Command:
Book.objects.all()

Expected Output:
<QuerySet [<Book: 1984>]>

---

## 3. Update

Python Command:
b = Book.objects.get(title="1984")
b.title = "Nineteen Eighty-Four"
b.save()
b.title

Expected Output:
'Nineteen Eighty-Four'

---

## 4. Delete

Python Command:
b.delete()
Book.objects.all()

Expected Output:
<QuerySet []>