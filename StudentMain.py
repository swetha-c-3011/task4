from schoolmanagement.Student import School, Student,AdvancedSchool


class SchoolMain:
    def __init__self(self):
        pass

    def implement_switch(self):
        StudentObj=""
        SchollObj=""
        try:
            while True:
                num=input("\nPress 1 To  add student"
                          "\nPress 2 To remove student"
                          "\nPress 3 To search Student"
                          "\npress 4 To use generator"
                          "\npress 5 To find students whose avg is higher than given input"
                          "\npress 6 To exit")
                match num:
                    case "1":
                        name = input("enter your name").strip().lower()
                        try:
                            id = int(input("enter your id"))
                            if  id<0 :
                                raise ValueError("ID must be a >0 .")
                            # print("Here")
                            # for d in Student.collection_of_dict:
                            #     print(type(d))

                            # if not any (d['student_id']==id for d in Student.collection_of_dict):
                            StudentObj = Student(id, name)
                            SchollObj = School(StudentObj)

                            num = int(input("number of marks to be added"))
                            SchollObj.addmarks(num,id)
                        except ValueError as val_err:
                            print(f"ValueError occurred: {val_err}")
                        except Exception as e:
                            print(f"An error occurred while adding a student: {e}")

                    case "2":
                        try:
                            id = int(input("enter the id of the student to removed"))
                            if id<0:
                                raise ValueError("ID must be a number.")
                            SchollObj.removeStudent(id)
                        except ValueError as val_err:
                            print(f"ValueError occurred: {val_err}")
                        except Exception as e:
                            print(f"An error occurred while adding a student: {e}")

                    case "3":
                        try:
                            id=int(input("enter the id of the student to search"))
                            if  id<0:
                                raise ValueError("ID must be a number.")
                            SchollObj.searchStudent(id)
                        except ValueError as val_err:
                            print(f"ValueError occurred: {val_err}")
                        except Exception as e:
                            print(f"An error occurred while adding a student: {e}")

                    case "4":
                        try:
                            SchollObj.__iter__()
                            for student in SchollObj:
                                print("printing from iterator : ", student)
                        except TypeError as type_err:
                            print(f"TypeError occurred: {type_err}")
                        except Exception as e:
                            print(f"An error occurred while using the iterator: {e}")
                    case "5":
                        try:
                            avg=float(input("enter the average"))
                            if 100<avg < 0:
                                raise ValueError("Average must be a number.")

                            AdvancedObj = AdvancedSchool(StudentObj)
                            AdvancedObj.find_students_above(avg)


                        except ValueError as val_err:
                            print(f"ValueError occurred: {val_err}")
                        except Exception as e:
                            print(f"An error occurred while adding a student: {e}")
                    case "6":
                        print("program exit")
                        break
                    case _:
                        print("provide a value input between 1 - 6")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")


obj=SchoolMain()
obj.implement_switch()









