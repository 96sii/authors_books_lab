class Book:
    def __init__(self, title, author, publisher, release_date, id=None):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.release_date = release_date
        self.id = id