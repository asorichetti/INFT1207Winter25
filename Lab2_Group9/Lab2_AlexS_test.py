import unittest
import csv
from Lab2_AlexS import add_book, list_books, search_book

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



if __name__ == '__main__':
    unittest.main()