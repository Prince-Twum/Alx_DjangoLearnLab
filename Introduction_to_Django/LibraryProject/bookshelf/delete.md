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