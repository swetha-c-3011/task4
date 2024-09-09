class Book:

    def __init__(self,title,author,bookId):
        self.title=title
        self.author=author
        self.bookId=bookId
        self.book_dict={
            "title": title, "author": author, "book_Id": bookId
        }

    def display_book_details(self):

         print(self.title,self.author,self.bookId)

class Library:
    def __init__(self):

        self.booklist = []


    def add_book(self,title,author,bookId):
         if not any(d['book_Id'] == bookId for d in self.booklist):

             book_obj=Book(title,author,bookId)
             self.booklist.append(book_obj.book_dict)
             print(self.booklist)

         else:
             print(f"Book with ID {bookId} already exists.")


    def remove_book(self,bookId):

        if  any(d['book_Id'] == bookId for d in self.booklist):
            for item in range(len(self.booklist)):
                if(self.booklist[item]['book_Id']==bookId):
                    del self.booklist[item]
                    print("book id ",bookId," deleted")
                    break
        else:

            print("there is no book id ",bookId)

    def search_book(self,title):
        if any(d['title']==title for d in self.booklist):
         for item in range(len(self.booklist)):
             if (self.booklist[item]['title']==title):
                 print(self.booklist[item])
                 break
        else:
            print("the title you are searching for is not there")

    def __iter__(self):
        for books in self.booklist:
            yield books.values()


class User:
    borrow_lst = []
    lis_of_user = []
    def __init__(self,name,userid):
        self.name=name
        self.userid=userid
        self.user_detail={
            "name":name,
            "userid":userid
        }

    def display_user_details(self):

        print(User.lis_of_user)

class LibraryUser(User):
    def __init__(self, name, userid,library,userobj):
        super().__init__(name, userid)
        self.borrow_dict={}

        self.library = library
        self.userobj=userobj

        if not any(d['userid'] == userobj.userid for d in User.lis_of_user):
            User.lis_of_user.append(self.userobj.user_detail)

    def borrow_book(self,bookId,userid):
        if any(d['userid']==userid for d in User.lis_of_user):

            if  any(d['book_Id']==bookId for d in self.library.booklist )and   not any (d['bookId']== bookId for d  in User.borrow_lst)   :
                self.borrow_dict={
                    "userid":userid,
                    "bookId":bookId
                }
                User.borrow_lst.append(self.borrow_dict)
                print("please ,Return the book without any damages")

            else:

                print("bookId is not valid or this book is already borrowed by someone")
        else:

            print("user id is not valid")


    def return_book(self,bookId):

            if any(d['bookId'] == bookId for d in User.borrow_lst):
                for i in range(len(User.borrow_lst)):
                    if (User.borrow_lst[i]['bookId'] == bookId):
                        del User.borrow_lst[i]
                        print("Thank you,Visit Again")
                        break
            else:
                print("book_Id is not borrowed")


    def track_borrowed_books(self):
        print("borrowed list ",User.borrow_lst)




