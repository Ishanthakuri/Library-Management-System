from datetime import datetime

class LibraryManagement():
    #Constructor for LibraryManagement Class.
    def __init__(self,librarianName,librarianID):
        #initializing
        self.librarianName = librarianName
        self.librarianID = librarianID
        self.borrowedDate = datetime.now()
        self.returnedDate = datetime.now()
        self.book_dict = {} 
        bookId = 1001 
        #reading bookList text file by using open function and read mode
        bookTextFile = open("bookList.txt", "r")
        bookList = bookTextFile.readlines()#reading each line and storing in a list.
        #using for each loop to iterate 
        for each in bookList:
            #separate and keep in index number in list.
            section = each.split(',')
            #updating the book_dict dictionary as 2D and assigned index number.
            self.book_dict.update({str(bookId):{"bookTitle":section[0],"author":section[1],"quantity":section[2],"price":section[3]}})
            bookId += 1 #adding 1 in book id 
        bookTextFile.close()#closing the bookTextFile.
        
    def display_books(self):
        """function to display the updated books."""
        print("\n\t\t\t\t////////////////////////////////////////////////////////////////////////////")
        print("\t\t\t\t                              AVAILABLE-BOOKS                                     ")
        print("\t\t\t\t////////////////////////////////////////////////////////////////////////////\n")
        print("\n\t\t\t\tBook ID\t\tBook Title-[Author]\n")
        print("\t\t\t\t---------------------------------------------------------------------------\n")
        #using for each loop to iterate all the key and value in dictionary.
        for key, value in self.book_dict.items():
            print("\t\t\t\t|",key,"\t\t|",value.get("bookTitle"),"-[",value.get("author"),"]","\n")
            print("\t\t\t\t|\t\t|"" Stock:",value.get("quantity"),"\t\t","Borrow Price: NRs",value.get("price"))
            print("\t\t\t\t---------------------------------------------------------------------------\n")
        print("\t\tNOTE: Your book borrowed duration is 10 day.Make sure to return otherwise,fine will be charged (NRS 5 per day).\n")

    def borrow_Book(self):
        """function to borrow the available books"""
        borrowStudentName = input("\nEnter Student Name: ")#taking value of student name. 
        borrowStudentId = input("\nEnter Student College id: ")#taking value of college id.

        bookIdInput = input("\nEnter Book ID: ")#taking value of book id.
        #condition for values if they are empty.
        if (borrowStudentName == '' or borrowStudentId == ''or bookIdInput == ''):
            print("\n\tEmpty value, Access denied.\n")
            return self.borrow_Book()
        #appending borrowStudentId in collegeId text file.
        collegeIDText = open("collegeId.txt","a")     
        collegeIDText.write(borrowStudentId+",") #adding comma
        collegeIDText.close() 

        #condition to check the bookIdInput stored in dictionary keys.
        if bookIdInput in self.book_dict.keys():
            #condition to check the quantity is grater than 0
            if int(self.book_dict[bookIdInput]['quantity']) > 0:

                #message for user.
                print("\n\t",borrowStudentName,"have successfully borrowed ",self.book_dict[bookIdInput]['bookTitle']," book.","\n\t Date & Time: ",str(self.borrowedDate),"\n")

                #this variable execute when the quantity is grater than 0
                borrowPrice = int(self.book_dict[bookIdInput]['price'])#assigning entered bookid and matching price from the dictionary.
                available = int(self.book_dict[bookIdInput]['quantity'])#assigning entered bookid and matching quantity from the dictionary.
                available -= 1 #decreasing the book quantity by 1.
                self.book_dict[bookIdInput]['quantity'] = str(available) #adding updated quantity in dictionary.

                #appending the bookIdInput in history text file.
                historyTextFile = open("bookIdHistory.txt","a")
                historyTextFile.write(bookIdInput)
                historyTextFile.write(",")
                historyTextFile.close() #closing historyTextFile.

                #rewriting the current available quantity in book list text file.
                updateTextFile = open("bookList.txt",'w')
                for i in self.book_dict:
                    updateTextFile.write(self.book_dict[i]['bookTitle']+",")
                    updateTextFile.write(self.book_dict[i]['author']+",")
                    updateTextFile.write(self.book_dict[i]['quantity']+",")
                    updateTextFile.write(self.book_dict[i]['price'])
                updateTextFile.close()#closing the update text file.

                #appending borrow note in borrow text file.
                borrowFile = open("["+borrowStudentId+"]"+"(Borrow_File).txt", "a")
                #writing for borrow note interface.
                borrowFile.write("+------------------------------------------------------------+\n")
                borrowFile.write("                Borrowed by: "+borrowStudentName +"\n") 
                borrowFile.write("                College Id: "+borrowStudentId +"\n")
                borrowFile.write("Date & Time : " +str(self.borrowedDate)+"\n")
                borrowFile.write("Book Id: "+bookIdInput+"\n")
                borrowFile.write("Book Name: "+self.book_dict[bookIdInput]['bookTitle']+"\n")
                borrowFile.write("Book Author: "+self.book_dict[bookIdInput]['author']+"\n")   
                borrowFile.write("Borrow Price: "+"NRs "+ str(borrowPrice)+"\n")
                borrowFile.write("Approved by: "+ self.librarianName+"["+self.librarianID+"]"+"\n")
                borrowFile.write("+------------------------------------------------------------+\n")
                borrowFile.close()#closing the borrow File.          

            #condition if the quantity in dictionary equals zero.
            elif int(self.book_dict[bookIdInput]['quantity']) == 0:
                #message for user.
                print("\n\tLooks like the book is not available.\n")
                #asking user for recommendation.
                recommendInput = input("Do you want to give book recommendation for us?(ok/no): ").lower()
                if recommendInput == 'ok':
                    print("\n---------------Recommendation Box----------------\n")
                    SBookName =input("Book Name: ")
                    SAuthorName = input("\nAuthor Name: ")
                    SLocation =input("\nWhere book can be found: ")
                    #appending on suggestion text file.
                    suggestionText = open("suggestionText.txt","a")
                    suggestionText.write("+------------------------------------+\n")
                    suggestionText.write("Book Name: "+SBookName)
                    suggestionText.write("\n")
                    suggestionText.write("Author Name: "+SAuthorName)
                    suggestionText.write("\n")
                    suggestionText.write("Location: "+SLocation)
                    suggestionText.write("\nRecommended by: "+ borrowStudentName+"["+borrowStudentId+"]")
                    suggestionText.write("\n+------------------------------------+\n")
                    suggestionText.close()
                    #message for user.
                    print("\n\tThank you we will get this book as soon as possible.\n")
                else:
                    print()#none
        
        else:
            #message for user if book id value is invalid.
            print("\n\tThis book does not exist.\n")
                 
     
    def return_Book(self):
        """function for when a book is being returned"""
        try:
            #reading the updated book id history text file by using open function with read mode.
            historyTextFile = open("bookIdHistory.txt","r")
            checking = historyTextFile.readline().split(",")#reading each line and storing value in list and slipting the bookid with their respective comma.
            historyTextFile.close()#closing history text file.

            #condition to check if the checking list is empty.
            if checking == ['']:
                #message for user.
                print("\n\t Looks like no books are borrowed.\n")
            else:     
                returnStudentName = input("\nEnter Student Name: ")#taking student name.
                returnStudentId = input("\nEnter Student College Id: ")#taking student id.
                #condition to check if the values are empty.
                if(returnStudentName == '' or returnStudentId == ''):
                    print("\n\tEmpty value, Access denied.")
                    return self.return_Book()
                #reading the college id text file.
                readCollegeId = open("collegeId.txt","r")
                reading = readCollegeId.readline()# reading each line in college id text file.
                readCollegeId.close()#closing the text file.
                list1 = reading.split(",")#spliting the book id with respective text file in storing in a list.
               
                #condition to check if the student id exist on list1
                if returnStudentId in list1:
                    
                    returnIdInput = input("\nEnter Book ID: ")#taking value of return id 
                    #condition to check if the return id is empty.
                    if(returnIdInput == ''):
                        print("\n\tEmpty value, Access denied.")
                        return self.return_Book()    
                
                    #giving condition if the returnIdInput exist in book_dict dictionary
                    if returnIdInput in self.book_dict.keys():
                        #condition to check in checking
                        if not returnIdInput in checking:
                            print("\n\tThis book is not borrowed yet.")
                            return self.return_Book()
                    
                        #taking input from user for day   
                        day = int(input("\nHow many days did you borrowed "+returnIdInput+" id book? "))
                        if day <1 :
                            print("\n\t*ERROR!*     Invalid day,Day can't be Negative.    *ERROR!*")
                            return self.return_Book()
                        borrowPrice = int(self.book_dict[returnIdInput]['price'])#assigning entered return id and matching price from the dictionary.   
                        #increasing the quantity by 1
                        available = int(self.book_dict[returnIdInput]['quantity'])#assigning entered return id and matching quantity from the dictionary
                        available += 1 #increasing the book quantity by 1.
                        self.book_dict[returnIdInput]['quantity'] = str(available) #adding in dictionary

                        #rewriting on bookList.txt.
                        updateTextFile = open("bookList.txt",'w')
                        #using for each loop to store the data in the dictionary
                        for i in self.book_dict:
                            updateTextFile.write(self.book_dict[i]['bookTitle']+",")
                            updateTextFile.write(self.book_dict[i]['author']+",")
                            updateTextFile.write(self.book_dict[i]['quantity']+",")
                            updateTextFile.write(self.book_dict[i]['price'])
                        updateTextFile.close()#closing the updateTextFile
                        #giving condition to check in bookIdHistory.txt if bookId exist,it will remove.
                        if returnIdInput in checking:    
                            historyTextFile_W = open("bookIdHistory.txt","w")
                            checking.remove(returnIdInput)#removing the returnIdInput      
                            checking.remove('')#removing all the book id and comma in bookIdHistory text
                            #using for each loop.
                            for i in checking:
                                historyTextFile_W.write(i+",")#adding the remaining bookId with comma in bookIdHistory text.
                            historyTextFile_W.close()#closing the history text file
                        
                        #removing the return student id from the list1
                        list1.remove(returnStudentId)
                        list1.remove("")#removing all the student id and comma in bookIdHistory text
                        #writing in the college text file.
                        removeCollegeId = open("collegeId.txt","w")
                        for k in list1:
                            removeCollegeId.write(k+",")#adding the remaining bookId with comma in bookIdHistory text.
                        removeCollegeId.close() #closing the text file.
                        

                        #giving condition for duration of books.
                        if day > 10:
                            
                            CountFineDay = day - 10 #subtracting 10 with entered day by user
                            fine = CountFineDay * 5 #multiplying 5 with the subtracted value.
                            total = fine + borrowPrice #adding the fine and borrowPrice.
                            #message for user of fine.
                            print("\n\t",returnStudentName,"have to pay NRs",fine,"as fine for returning the book late.") 
                            #Concating string and value for user 
                            print("\n\t",returnStudentName,"have successfully returned ",self.book_dict[returnIdInput]['bookTitle']," book.","\n\t Date & Time: "+str(self.returnedDate)+"\n")

                            #appending if days are more then 10 on return text file for respective college id.
                            returnFileFine = open("["+returnStudentId+"]"+"(Return_File).txt","a")
                            #return file note interface.
                            returnFileFine.write("+-----------------------------------------------------------+\n")
                            returnFileFine.write("                Returned by: "+returnStudentName +"\n") 
                            returnFileFine.write("                College Id: "+returnStudentId +"\n")
                            returnFileFine.write("Date & Time : " +str(self.returnedDate)+"\n")
                            returnFileFine.write("Book id: "+returnIdInput+"\n")
                            returnFileFine.write("Book Name: "+self.book_dict[returnIdInput]['bookTitle']+"\n")
                            returnFileFine.write("Book Author: "+self.book_dict[returnIdInput]['author']+"\n")  
                            returnFileFine.write("Borrow Price: "+"NRs "+str(borrowPrice)+"\n")
                            returnFileFine.write(str(CountFineDay)+" days late fine: "+"NRs "+str(fine)+"\n")
                            returnFileFine.write("Total: "+"NRs "+ str(total)+"\n")
                            returnFileFine.write("Approved by: "+ self.librarianName+"["+self.librarianID+"]"+"\n")
                            returnFileFine.write("+-----------------------------------------------------------+\n")
                            returnFileFine.close() 

                            
                        elif day <= 10:
                           
                            #appending if days are less then 10 on return file for respective college id
                            returnFile = open("["+returnStudentId+"]"+"(Return_File).txt","a")
                            #return file note interface.
                            returnFile.write("+-----------------------------------------------------------+\n")
                            returnFile.write("                Returned by: "+returnStudentName +"\n") 
                            returnFile.write("                College Id: "+returnStudentId +"\n")
                            returnFile.write("Date & Time : " +str(self.returnedDate)+"\n")
                            returnFile.write("Book id: "+returnIdInput+"\n")
                            returnFile.write("Book Name: "+self.book_dict[returnIdInput]['bookTitle']+"\n")  
                            returnFile.write("Book Author: "+self.book_dict[returnIdInput]['author']+"\n")
                            returnFile.write("Borrow Price: "+"NRs "+ str(borrowPrice)+"\n")
                            returnFile.write("Approved by: "+ self.librarianName+"["+self.librarianID+"]"+"\n")
                            returnFile.write("+-----------------------------------------------------------+\n")
                            returnFile.close() 
                            
                            #message for user of returning.
                            print("\n\t",returnStudentName,"have successfully returned ",self.book_dict[returnIdInput]['bookTitle']," book.","\n\t Date & Time: ",str(self.returnedDate)+"\n")
                    else:
                        print("\n\tThis book does not exist.")
                else:
                    #message for user if the borrow id and return id didn't match.
                    print("\n*ERROR!*    College Id must match while returning a book.     *ERROR!*\n")
        #excepting file not found error.
        except (FileNotFoundError): 
            print("\n\t Looks like no books are borrowed.\n")
            print()
        #excepting value error from day.
        except:
            print("\n *ERROR!*              Invalid input                 *ERROR!*\n")
            print("\n *ERROR!*       Words are not acceptable on day.     *ERROR!*\n")
        
