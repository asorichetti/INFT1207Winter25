import unittest
import csv
from Lab2_AlexS import add_book, list_books, search_book, delete_book

class TestReadingList(unittest.TestCase):
     def test_add_book(self):
        """Test adding a book."""
        add_book("Test Book", "Author Name", "2022")
        with open("books.csv", "r") as file:
            reader = csv.reader(file)
            rows = list(reader)
        self.assertIn(["Test Book", "Author Name", "2022"], rows)

     def test_search_book(self):
        """Test searching for an existing book."""
        output_result = search_book("Test Book")  # Now it returns a value
        expected_output = "Found: Title: Test Book, Author: Author Name, Year: 2022"
        self.assertEqual(output_result, expected_output, "search_book did not return the expected output.")

     def test_list_book(self):
         """Test listing all existing books."""
         output_result = list_books()
         self.assertEqual(output_result, "All Books Listed")

     def test_delete_book(self):
         """Test deeleting the last book entry by comparing CSV Length"""
         with open('books.csv', 'r') as file:
             reader = csv.reader(file)
             rows = list(reader)

         initial_length = len(rows)-1
         self.assertGreater(initial_length, 0, "Cannot delete from an empty list")

         delete_book()
         with open('books.csv', 'r') as file:
             reader = csv.reader(file)
             rows_after_delete = list(reader)
         new_length = len(rows_after_delete)-1
         self.assertEqual(new_length, initial_length-1, "delete_book() did not remove the last entry correctly.")
         
         def test_add_outer(self):
            """Test adding a book."""
            add_book("Test Book", "Author Name", "John", "2022")
            with open("books.csv", "r") as file:
                reader = csv.reader(file)
                rows = list(reader)
         self.assertIn(["Test Book", "Author Name", "2022"], rows)
if __name__ == '__main__':
    unittest.main()