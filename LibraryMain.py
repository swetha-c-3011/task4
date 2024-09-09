from LibrarayModule import Library
from LibrarayModule import User
from LibrarayModule import LibraryUser

class Python_Switch:
    def __init__self(self):
        pass

    def implement_switch(self):
        libObj = Library()
        libUserObj = ""
        while True:


            num = input("press 1:To add books "
                        "\n press 2 : To remove Books "
                        "\npress 3: To search for a boom"
                        "\n press 4 To use genrator"
                        " \n press 5:To Borrow user"


                        "\n press 7: To return books"
                        "\n press 8: To track borrowed books"
                        "\n press 9: To exit")


            match num:
                case "1":


                    inp_title=input("enter the title of the book")
                    inp_author=input("enter the authoir name")
                    inp_id=input("enter the id")
                    libObj.add_book(inp_title,inp_author,inp_id)

                case "2":
                    removebook=input("enter the book which needs to be removed")
                    libObj.remove_book(removebook)
                case "3":
                    searchbooktitle=input("enter the title of the book which needs to be searched")
                    libObj.search_book(searchbooktitle)
                case "4":
                    libObj.__iter__()
                    for book in libObj:
                        print(book)
                case "5":
                    u_name=input("enter your name")
                    u_id=input("enter your user_id")
                    user_obj=User(u_name,u_id)
                    libUserObj = LibraryUser(u_name, u_id, libObj,user_obj)
                    bookborrowid = input("enter the id of the book to borrow  books from library ")
                    libUserObj.display_user_details()
                    libUserObj.borrow_book(bookborrowid, u_id)
                case "7":
                    returnbookid=input("enter thw id of the book which needs to be returned")

                    libUserObj.return_book(returnbookid)
                case "8":
                    libUserObj.track_borrowed_books()
                case "9":
                    print("exit program")
                    break
                case _:
                    print("the input you have given is not valid")



call_switch=Python_Switch()
call_switch.implement_switch()




# libUserObj.return_book("2","123")
#     libUserObj.track_borrowed_books()
    # libObj.add_book("scnd_book","scnd_author","2")
    # libObj.generator()
    # libObj.add_book("a","fstauthor","1")
    # libObj.add_book("ab","2ndauthor","1")
    # libObj.remove_book("1")
    # libObj.search_book("scnd_book")