class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name should be a string")
        self.name = name
        Author.all.append(self)
        
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self,book,date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self): 
        return sum(contract.royalties for contract in self.contracts())
    

class Book:
    all = []

    def __init__(self, title):
        if not isinstance(title, str):
            raise Exception("Title should be a string")
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        result = []
        for contract in Contract.all:
            if contract.book == self:
                result.append(contract.author)
        return result


class Contract:
    all = []
    
    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author should be an Author object")
        self._author = author
        
        if not isinstance(book, Book):
            raise Exception("Book should be a Book object")
        self._book = book
        
        if not isinstance(date, str):
            raise Exception("Date should be a string")
        self._date = date
        
        if not isinstance(royalties, int):
            raise Exception("Royalties should be an integer")
        self._royalties = royalties
        
        Contract.all.append(self)
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Author should be an Author object")
        self._author = value
    
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("Book should be a Book object")
        self._book = value
    
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("Date should be a string")
        self._date = value
    
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception("Royalties should be an integer")
        self._royalties = value

    @classmethod
    def contracts_by_date(cls, date):
        return[contract for contract in cls.all if date == contract.date]