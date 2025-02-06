##################################################
# Name: Alex Sorichetti
# Program: Book Storage
# Description: A program which takes in a CSV file
# and utilizes the data in the file for the purpose of 
# book listings.
##################################################
import csv

# Function to add a book to the reading list
def add_book(title, author, year):
    try:
        with open('books.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([title, author, year])
            return("Book Added Successfully")
    except FileNotFoundError:
        print("User does not have a books.csv file in the correct spot.")

# Function to list all books
def list_books():
    try:
        with open('books.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                print(f'Title: {row[0]}, Author: {row[1]}, Year: {row[2]}')
            return('All Books Listed')
                
    except FileNotFoundError:
        print("User does not have a books.csv file in the correct spot.")

# Function to search for a book by title
def search_book(title):
    try:
        with open('books.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0].lower() == title.lower():
                    result = f'Found: Title: {row[0]}, Author: {row[1]}, Year: {row[2]}'
                    print(result)
                    return (result)
            
            result = 'Book Not Found'
            return (result)
    except FileNotFoundError:
        print("User does not have a books.csv file in the correct spot.")

def delete_book():
    remove=open('books.csv', 'r+')
    lines = remove.readlines()
    lines.pop()
    remove=open('books.csv', 'w+')
    remove.writelines(lines)
    return("Deleted Successfully")

# Menu loop
def menu():
    i = 0
    while True:
        print("\n1. Add Book\n2. List Books\n3. Search Book\n4. Delete Last Entered Book\n5. Exit")
        choice = input("Select an option: ")
        
        if choice == '1':
            while i == 0:
             title = input("Enter book title: ")
             if title != "":
                i+=1
            i=0
            while i== 0:
             author = input("Enter author name: ")
             if author != "":
                i+=1
            i = 0
            while i == 0:
                try:
                    year = int(input("Enter year of publication: "))
                    if year != "":
                        i+=1
                except ValueError:
                    print("Sorry, the value entered is not a valid year.")
            i=0
            hold = add_book(title, author, year)
        elif choice == '2':
            hold = list_books()
        elif choice == '3':
            title = input("Enter book title to search: ")
            hold = search_book(title)
        elif choice == '4': 
            hold = delete_book()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.")

# Run the program
if __name__ == "__main__":
    menu()
