import pdb
from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

author_repository.delete_all()
book_repository.delete_all()

author_1 = Author('Stephen', 'King')
author_repository.save(author_1)

book_1 = Book("IT", author_1, "Viking", "19/09/1986")
book_repository.save(book_1)

pdb.set_trace()