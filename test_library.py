import unittest

from library import Library

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library("books.json")
        self.library.books = []
        self.title = "Python Basics"
        self.author = "Paul Heyman"
        self.result = self.library.add_book("Python Basics", "Paul Heyman")

    def test_add_book(self):

        self.assertTrue(self.result)
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, self.title)
        self.assertEqual(self.library.books[0].author, self.author)

    
    def test_add_duplicate_book(self):
        result = self.library.add_book(self.title, self.author)

        self.assertFalse(result)
        self.assertEqual(len(self.library.books), 1)


    def test_find_book(self):
        
        result = self.library.find_book(1)

        self.assertIsNotNone(result)
        self.assertEqual(result.title, self.title)
        self.assertEqual(result.author, self.author)
        self.assertFalse(self.library.find_book(2))


    def test_find_non_existent_book(self):

        result = self.library.find_book(2)

        self.assertIsNone(result)


    def test_remove_book(self):
        
        result = self.library.remove_book(1)

        self.assertTrue(result)
        self.assertEqual(len(self.library.books), 0)

    def test_remove_non_existent_book(self):

        result = self.library.remove_book(2)

        self.assertFalse(result)
        self.assertEqual(len(self.library.books), 1)


    def test_update_book(self):
    
        result = self.library.update_book(1, "Advanced Python", "Paul Shaw")

        self.assertTrue(result)
        self.assertEqual(result.book_id, 1)
        self.assertEqual(result.title, "Advanced Python")
        self.assertEqual(result.author, "Paul Shaw")



    def test_update_non_existent_book(self):

        result = self.library.update_book(2, "Advanced Python", "Paul Shaw")

        self.assertFalse(result)
        

    def test_load_books(self):

        result = self.library.load_books()


        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, self.title)
        self.assertEqual(self.library.books[0].author, self.author)


if __name__ == "__main__":
    unittest.main()