# Developed by Chinmay Mulay on Date: 18-04-2021
# Mini Library Management System
# Library --> Books [All books, borrow, return, track, donate]
# Admin --> Library [BookName] | Library --> Students [Name]

# Classes : Library and Students
class Library:

    def __init__(self, listBooks):
        self.books = listBooks

    def displayAvailbleBooks(self): 
        print(f"\nThere are {len(self.books)} books available:")
        for book in self.books: 
            print(" -> " + book)  
        print("\n")

    def borrowBook(self, name, bookName): 
        if bookName not in self.books:  
            print("Book is issues by someone else.")
        else:  
            track.append({name: bookName})
            print("Book issued")
            self.books.remove(bookName)

    def returnBook(self,
                   bookName):  
        print("Book returned successfully.")
        self.books.append(bookName)

    def donateBook(self,
                   bookName): 
        print("Thankyou for donating your book!")
        self.books.append(bookName)


class Student():
    def issueBook(self):  
        print("Do you want to issue book ?")
        self.book = input("Enter name of the book which you want to issue:")
        return self.book

    def returnBook(self):
        print("Do you want to return book?")
        name = input("Enter your name:")
        self.book = input("Enter the name of your book that you issued:")
        if {name: self.book} in track:
            track.remove({name: self.book})
        return self.book

    def donateBook(self):
        print("Do you want to donate book ?")
        self.book = input("Enter name of the book which you want to donate:")
        return self.book


if __name__ == "__main__":
    Library = Library(["Rich Dad Poor Dad", "The Secret", " Think and Grow Rich", "The Lean Start-Up", "The Monk and the Riddle", " How to Win Friends and Influence People"])  
    student = Student()
    track = []

    print("Welcome to Mini Library Management System")
    print(
        "What do you want to do:- \n1. View books\n2.Issue Book\n3. Return Book\n4.Donate Book\n5.Track Books\n6.Exit")

    while (True):
        try:
            response = int(input("Enter your choice:"))
            if response == 1:
                Library.displayAvailbleBooks()
            elif response == 2:
                Library.borrowBook(input("Enter your name:"), student.issueBook())
            elif response == 3:
                Library.returnBook(student.returnBook())
            elif response == 4:
                Library.donateBook(student.donateBook())
            elif response == 5:  # Logic for tracking issued books
                for i in track:
                    for key, value in i.items():
                        holder = key
                        book = value
                        print(f"{book} book is issued by {holder}.")
                print("\n")
                if len(track) == 0:
                    print("No book has been issued yet!. \n")
            elif response == 6:
                print("Thanks for using Mini Library Management System")
                print("Developed by - Chinmay Mulay")
                exit()
            else:
                print("Wrong Choice!")

        except Exception as e:
            print(e)
