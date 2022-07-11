from libraryManagement import LibraryManagement

run = True #declaring variable
#User Interface
print()
print("\t\t\t\t\t///////////////////////////////////////////////////////")
print("\t\t\t\t\t               Islington College Library               ")
print("\t\t\t\t\t///////////////////////////////////////////////////////")
print("\t\t\t\t\tOpen time: 9AM")
print("\t\t\t\t\tClose time: 5PM\n")

while run:#main loop
    librarianName = input("\tEnter librarian name: ")#taking the libraian name.
    librarianID = input("\n\tEnter librarian Id: ")#taking the libraian id.
    try: 
        #condition to check if the values are empty.
        if (librarianName == '' or librarianID == ''):
            print("\n\tEmpty value, Access denied.\n")
            run = True            
        else:
            #creating instance of LibraryManagement class to obj
            obj = LibraryManagement(librarianName,librarianID)
    
            def menu():
                try:
                    #Using dictionary for just printing.
                    menu_dict = {"0":"Exit","1":"Display Books","2":"Borrow Book","3":"Return Book"}
                    print("\n///////////////////////////////////////////////")
                    print("                 MAIN MENU                     ")
                    print("///////////////////////////////////////////////\n")
                    #using for each loop to iterate the key and value in menu dictionary.
                    for key,value in menu_dict.items():
                        print("Press:",key, "for",value)
                    cmd = int(input("\nChoice and enter your command here: ").lower())#taking command.
                    return cmd
                #excepting value error from cmd.
                except(ValueError):
                    print("\n *ERROR!*              Invalid input                 *ERROR!*\n")
                    print("\n *ERROR!*         Words are not acceptable.          *ERROR!*\n")
                
            while run:
                try:
                    #initializing menu function with command.
                    command = menu()
                    #condition if the command equals 0
                    if command == 0:
                        exit = input("\nAre you sure you want to exit?(y/n): ").lower()#taking input from user y or n
                        if exit == '' or exit == '':
                            print("\n\tEmpty value, Access denied.\n")
                        elif exit == 'y'or exit == 'yes':
                            print("\n\tSuccessfully exited.\n")
                            run = False #breaking the loop
                        else:
                            run = True 
                    #condition if the command equals 1
                    if command == 1:
                        obj.display_books()#calling the display book function.
                    #condition if the command equals 2
                    if command == 2:
                        print("\nYOU SELECTED: BORROW")
                        obj.borrow_Book()#calling the borrow book function.
                    #condition if the command equals 3
                    if command == 3:
                        print("\nYou SELECTED: RETURN")
                        obj.return_Book()#calling the return book function.
                    #condition if the command is greater then 4
                    if command >= 4:
                        print("\n *ERROR!*              Invalid input                 *ERROR!*\n")
                        print("\n *ERROR!*           Command doesn't exist            *ERROR!*\n")
                        run = True #continue the loop
                #expecting type error.
                except(TypeError):
                    print()
    except:
        print("SOMETHING IS NOT RIGHT.")