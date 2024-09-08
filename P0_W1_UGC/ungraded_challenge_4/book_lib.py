
# Membuat class Book + Try-Except
class Book:
    def __init__(self, id, title, author):
        try:
            # Validate id
            if not isinstance(id, int) or id <= 0:
                raise ValueError("ID must be a positive integer")

            # Validate title and author
            if not title or not author:
                raise ValueError("Title and author cannot be empty")

            # Assign attributes if all validations pass
            self.id = id
            self.title = title
            self.author = author

        except ValueError as v:
            print(f"Error: {v}")
            # Set default values
            self.id = None
            self.title = "Unknown Title"
            self.author = "Unknown Author"
    
    def detail_buku(self):
        return [self.id, self.title, self.author]

# Membuat class Library
class Library():
    def __init__(self, lib):
        self.lib = lib

    def add_book(self,id,title,author):    
        a_book = Book(id,title,author)
        self.lib.append(a_book.detail_buku())
        
    def remove_book(self,b_book):
        self.lib = [i for i in self.lib if i != b_book.detail_buku()]

    def search_book(self, book_title = None, book_author = None):
        i = 0
        valid = False
        while i <= len(self.lib)-1:
            if self.lib[i][1] == book_title or self.lib[i][2] == book_author:
                print(self.lib[i])
                valid = True
                break
            i += 1
              
        if valid == False:
            print("The book is not found")
        
        return valid
                    
    def display_lib(self):
        print (self.lib)
