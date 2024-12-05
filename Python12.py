class Employee:
    def __init__(self):
        print("Employee created")

    def __del__(self):
        print("Employee deleted")

ob = Employee()
del ob

#Library Management System

class Library:
    def __init__(self, book_list, name):
        self.book_list = book_list
        self.name = name
        self.LendDict = {}

    def displaybooks(self):
        print(f"Welcome to the Library: {self.name}")
        for book in self.book_list:
            print(book)
    
    def lendbook(self, user, book):
        if book not in self.book_list:
            print("Sorry, we do not have that book in the Library")
        elif book in self.LendDict:
            print("The book is already lended")
        else:
            self.LendDict[book] = user
            print("The database has been updated")

    def addbook(self, book):
        self.book_list.append(book)
        print("The book has been added")

    def returnbook(self, book):
        if book in self.LendDict:
            del self.LendDict[book]
        else:
            print("The book has not been lended")

if __name__ == '__main__':
    books = Library([
        'Python', 'Rich Dad Poor Dad', 'Harry Potter', 'C++ Basics', 'Algorithms by CLRS', 'The Lord of the Rings', 'Of Mice and Men'], "Let's Upskill")
    user_name = input("Welcome to our library! Please enter your name: ")

    while True:
        print(
            f"\nHello {user_name}, welcome to the {books.name} library. Please choose an option:"
        )
        print(
            "1. Display Books\n2. Lend a Book\n3. Add a Book\n4. Return a Book\n5. Quit"
        )
        user_choice = input("Enter your choice to continue: ")

        if user_choice not in ['1', '2', '3', '4', '5']:
            print("Please enter a valid option.")
            continue

        if user_choice == '1':
            books.displaybooks()
        elif user_choice == '2':
            book = input("Enter the name of the book you want to lend: ")
            books.lendbook(user_name, book)
        elif user_choice == '3':
            book = input("Enter the name of the book you want to add: ")
            books.addbook(book)
        elif user_choice == '4':
            book = input("Enter the name of the book you want to return: ")
            books.returnbook(book)
        elif user_choice == '5':
            print(f"Thank you for using the library, {user_name}. Goodbye!")