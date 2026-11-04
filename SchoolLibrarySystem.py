#Step 1:Create class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._borrowed = False
        print("New book added: " , self.title)
        
    def borrow(self):
        self._borrowed = True
        print("Success, you just borrowed a book!:" , self.title)
        
    def return_book(self):
        self._borrowed = False
        print("Sucess, you just returned a book!:" , self.title)
        
print("-----LOADING ALL THE BOOKS IN INVENTORY-----")

book1 = Book("Harry Potter - 1", "J.K. Rowling")
book2 = Book("The Hobbit", "J.R.R. Tolkien")
book3 = Book("Wings of Fire", "A.P.J. Abdul Kalam & Arun Tiwari")
book4 = Book("The Discovery of India", "Jawaharlal Nehru")

book1.borrow()

book3.borrow()

print("-------------")

book2.return_book()

book4.return_book()

print("-----------------------------------------------------------------")
