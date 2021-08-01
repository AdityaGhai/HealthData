class Library:
    def __init__(self, listofbook, library_name):
        self.books= listofbook
        self.library_name=library_name

    def display_book(self):
        print(f"Available books are- {self.books}")
    @property
    def lend(self):
        lended_book={}
        book_lend=input("Enter the name of book you want: ")
        if book_lend in self.books:
            name = input("Enter your Name: ")
            print(f"Here {name}, This is your book- {book_lend}")
            lended_book[name]=book_lend
            self.books.remove(book_lend)
        else:
            print("Sorry we don't have that book right now.")

    def add(self):
        add_book = input("Enter the name of book you want to add: ")
        if add_book not in self.books:
            self.books.append(add_book)
        else:
            print("This book is already in library")

    def return_book(self):
        ret_book = input("Enter the name of book you want to return: ")
        self.books.append(ret_book)
        print("Thank You for returning the book. ")


aditya = Library(["Maths", "Biology", "Physics", "Chemistry"], "Aditya Library")

print(f"\t\t\tWelcome to {aditya.library_name}\n")

if __name__ == '__main__':
    while True:
         print("\n")
         aditya.display_book()
         choose = input("\nChoose 1 for lend a book\nChoose 2 for add a book\nChoose 3 for return a book\n Press 'q to quit")
         if choose == '1':
             aditya.lend
         elif choose == '2':
             aditya.add()
         elif choose == '3':
             aditya.return_book()
         elif choose == "q":
             break
         else:
             print("Invalid credentials")




