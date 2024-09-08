
import unittest
from book_lib import Book, Library

class TestBook(unittest.TestCase):
    
    def test_book_valid(self):
        # Test valid book creation
        book = Book(1, 'To Kill a Mockingbird', 'Harper Lee')
        self.assertEqual(book.detail_buku(), [1, 'To Kill a Mockingbird', 'Harper Lee'])
   
    def test_book_invalid_id(self):
        # Test book with invalid id
        book = Book('invalid', '1984', 'George Orwell')
        self.assertEqual(book.detail_buku(), [None, 'Unknown Title', 'Unknown Author'])
     
    def test_book_empty_title(self):
        # Test book with empty title
        book = Book(2, '', 'George Orwell')
        self.assertEqual(book.detail_buku(), [None, 'Unknown Title', 'Unknown Author'])

    def test_book_empty_author(self):
        # Test book with empty author
        book = Book(3, '1984', '')
        self.assertEqual(book.detail_buku(), [None, 'Unknown Title', 'Unknown Author'])


class TestLibrary(unittest.TestCase):

    def setUp(self):
        # Create an empty library for each test
        self.library = Library([])
        print('Inisiasi library: ',self.library)
   
    def test_add_book(self):
        # Test adding a valid book to the library
        self.library.add_book(1, '1984', 'George Orwell')
        self.assertIn([1, '1984', 'George Orwell'], self.library.lib)
 
    def test_remove_book(self):
        # Test removing a book from the library
        self.library.add_book(1, '1984', 'George Orwell')
        book = Book(1, '1984', 'George Orwell')
        self.library.remove_book(book)
        self.assertNotIn([1, '1984', 'George Orwell'], self.library.lib)

    def test_search_book_by_title(self):
        # Test searching for a book by title
        self.library.add_book(1, '1984', 'George Orwell')
        self.library.add_book(2, 'To Kill a Mockingbird', 'Harper Lee')
        self.assertTrue(self.library.search_book(book_title='1984'))

    def test_search_book_by_author(self):
        # Test searching for a book by author
        self.library.add_book(1, '1984', 'George Orwell')
        self.assertTrue(self.library.search_book(book_author='George Orwell'))

    def test_search_book_not_found(self):
        # Test searching for a book that doesn't exist
        self.assertFalse(self.library.search_book(book_author='Nonexistent Book'))
      
    def test_display_lib(self):
        # Test displaying the library
        self.library.add_book(1, '1984', 'George Orwell')
        self.assertEqual([[1, '1984', 'George Orwell']],self.library.lib)

if __name__ == '__main__':
    unittest.main()
