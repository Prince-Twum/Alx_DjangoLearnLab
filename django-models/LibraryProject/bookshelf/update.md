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