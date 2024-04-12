#DOC 334 individual course work
# Studeny ID : 20210767
# Creating a book keeping program for ABC book store

# Create variables
wlcm_txt = " "
user_choice = 0
user_input = 0
user_action = 0
search_opt = 0
user_input = " "
edit_opt = 0
chap_opt = 0
sub_opt = 0

import mysql.connector

# Opening and establishing data base connection
conDict = {'host' : 'localhost',
           'database' : 'abc_book_store',
           'user' : 'root',
           'password' : ''}
db = mysql.connector.connect(**conDict)
cursor = db.cursor()

# Create functions
def BookSearch (user_input): #To search books according to user preference
    cursor.execute("SELECT * FROM book WHERE BookNo='"+user_input+"'OR Title='"+user_input+"'OR Author='"+user_input+"'OR Publisher='"+user_input+"'")
    data = cursor.fetchall()
    for item in data:
        print ("Book Number : ",item[0])
        print ("Book title : ",item[1])
        print ("Subject code: ",item[2])
        print ("Book author :",item[3])
        print ("Book publisher : ",item[4])
        print ("Bookprice : Rs.",item[5])
        print ("Location of the book : ",item[6])
        print() # To leave a line to seperate data of two books

def GetBookNo ():# Read book number from user
    user_bookNo = input("Enter the book number : ")
    return (user_bookNo)

def GetBookTitle ():# Read book title from user
    user_title = input("Enter the book title : ")
    return (user_title)

def GetAuthor ():# Read book author from user
    user_author = input("Enter the author : ")
    return (user_author)

def GetPublisher ():# Read book publisher from user
    user_publisher = input("Enter the publisher : ")
    return (user_publisher)

def GetPrice ():# Read book price from user
    user_price = input("Enter the price of the book : ")
    return (user_price)

def GetLocation ():# Read book price from user
    user_location = input("Enter the location : ")
    return (user_location)

def GetSubCode ():# Read book price from user
    user_subCode = input("Enter the subject code : ")
    return (user_subCode)

def GetChapNo ():# Read book price from user
    user_chapNo = input("Enter the chapter number : ")
    return (user_chapNo)

def GetChapTitle ():# Read book price from user
    user_chaptitle = input("Enter the chapter title : ")
    return (user_chaptitle)

def GetStartPg ():# Read book price from user
    user_startPg = input("Enter the chapter starting page : ")
    return (user_startPg)

def GetEndPg ():# Read book price from user
    user_endPg = input("Enter the chapter ending page : ")
    return (user_endPg)

def GetSubName ():# Read Subject name from user
    user_subName = input("Enter the subject name : ")
    return (user_subName)

def DBcommands (): # Final SQL queries
    db.commit()
    print(cursor.rowcount, " Record Effected ")

####### Main Process #######
wlcm_txt = (" ABC BOOK STORE ")
print (wlcm_txt.center(50,'*'))

# Getting the category user wants to perform action in
user_choice= int(input("""Please specify the category you wish to take action,
(1) Book related\n(2) Chapter related\n(3) Subject related
Enter the number of your requirement : """))

# Book related actions (Main option1)
if user_choice == 1:
    user_action =int(input("""\nPlease refer the options below; \n (1) Search for a book \n (2) Add a new book
 (3) Edit a existing book \n (4) Delete a book\nPlease enter the number of the action required : """))

    #Process to search books
    if user_action == 1:
        print("""\nHow would you prefer to search your book ?
(1) Search by book number
(2) Search by book title
(3) Search by author
(4) Search by publisher """)
        search_opt = int(input("Enter the number of the prefered search option : "))
        if search_opt == 1: # Search by book number
            BookSearch(GetBookNo())

        elif search_opt == 2: # Search by book title
            BookSearch(GetBookTitle ())

        elif search_opt == 3: # Search by the book author
            BookSearch(GetAuthor ())

        elif search_opt == 4: # Search by the book publisher
            BookSearch(GetPublisher ())

    #Process to add a new book (option 2)
    elif user_action == 2:
        # SQL Statements
        SQLtext = "INSERT INTO book (BookNo,Title,SubjectCode,Author,Publisher,Price,Location) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        # Calling functions
        userValues = (GetBookNo(),GetBookTitle(),GetSubCode(),GetAuthor(),GetPublisher(),GetPrice(),GetLocation())
        cursor.execute(SQLtext,userValues)
        DBcommands ()

    #Process to edit a existing book (option 3)
    elif user_action == 3 :
        print("""\nWhich column would you prefer to edit ?
(1) Edit book title
(2) Edit book author
(3) Edit book publisher
(4) Edit book price
(5) Edit Location of the book
(6) Edit the subject code""")
        edit_opt = int(input("Enter the number of the prefered edit option : "))
        print("First enter the data you want to replace the current entry with then the relavent book number,")

        if edit_opt == 1: #edit book title
            upd_data = "UPDATE book SET Title='"+GetBookTitle ()+"' WHERE BookNo="+GetBookNo()

        elif edit_opt == 2: #edit book author
            upd_data = "UPDATE book SET Author='"+GetAuthor()+"' WHERE BookNo="+GetBookNo()

        elif edit_opt == 3: #edit book publisher
            upd_data = "UPDATE book SET Publisher='"+GetPublisher()+"' WHERE BookNo="+GetBookNo()

        elif edit_opt == 4: #edit book price
            upd_data = "UPDATE book SET Price='"+GetPrice()+"' WHERE BookNo="+GetBookNo()

        elif edit_opt == 5:#edit book location 
            upd_data = "UPDATE book SET Location='"+GetLocation()+"' WHERE BookNo="+GetBookNo()

        elif edit_opt == 6: #edit book subject code
            upd_data = "UPDATE book SET SubjectCode='"+GetSubCode()+"' WHERE BookNo="+GetBookNo()
        cursor.execute(upd_data)
        DBcommands ()

    #Process to delete a existing book (option 3)
    elif user_action == 4 :
        cursor.execute ("DELETE FROM book WHERE BookNo = "+ GetBookNo()+"")
        DBcommands ()

# Chapter related actions (Main option2)
elif user_choice == 2:
    chap_opt =int(input("""\nPlease refer the options below; \n (1) Search chapter information of a book \n (2) Add a new chapter
 (3) Edit an existing chapter \n (4) Delete a chapter\nPlease enter the number of the action required : """))

    #Process to search chapters with a book number
    if chap_opt == 1:
        cursor.execute("SELECT * FROM chapter WHERE BookNo= '"+ GetBookNo ()+"'")
        data = cursor.fetchall()
        for item in data:
            print ("Book Number : ",item[0])
            print ("Chapter number: ",item[1])
            print ("Chapter title: ",item[2])
            print ("Starting page : ",item[3])
            print ("Ending page : ",item[4])
            print() # To leave a line to seperate data of two books
            
    #Process to add a new chapter
    elif chap_opt == 2 :
        SQLtext = "INSERT INTO chapter (BookNo,ChapterNo,ChapterTitle,StartingPgNo,EndingPgNo) VALUES (%s,%s,%s,%s,%s)"
        userValues = (GetBookNo(),GetChapNo(),GetChapTitle(),GetStartPg(),GetEndPg())
        cursor.execute(SQLtext,userValues)
        DBcommands ()

    #Process to edit a existing chapter (option 3)
    elif chap_opt == 3 :
        print("""\nWhich column would you prefer to edit ?
(1) Edit chapter title
(2) Edit chapter starting page
(3) Edit chapter ending page""")
        chap_edit = int(input("Enter the number of the edit option : "))
        print("\nFirst enter the data you want to replace the current entry with then the relavent book and chapter numbers,")
        
        if chap_edit == 1:# Update chapter title
            upd_data = "UPDATE chapter SET ChapterTitle='"+GetChapTitle()+"' WHERE BookNo='"+GetBookNo()+"'AND ChapterNo="+GetChapNo()

        elif chap_edit == 2: # Update chapter starting page
            upd_data = "UPDATE chapter SET StartingPgNo='"+GetStartPg()+"' WHERE BookNo='"+GetBookNo()+"'AND ChapterNo="+GetChapNo()

        elif chap_edit == 3:# Update chapter ending page
            upd_data = "UPDATE chapter SET EndingPgNo='"+GetEndPg()+"' WHERE BookNo='"+GetBookNo()+"'AND ChapterNo="+GetChapNo()
        cursor.execute(upd_data)
        DBcommands ()
        
    #Process to delete a existing chapter (option 3)
    elif chap_opt == 4 :
        print ("\nEnter the book and chapter numbers of the entry which needs to be deleted")
        cursor.execute ("DELETE FROM chapter WHERE BookNo ='"+ GetBookNo()+"'AND ChapterNo="+GetChapNo()+"")
        DBcommands ()

# Subject related actions (Main option3)
elif user_choice == 3:
    sub_opt =int(input("""\nPlease refer the options below; \n (1) Search for a subject \n (2) Add a new subject
 (3) Edit an existing subject name \n (4) Delete a subject\nPlease enter the number of the action required : """))

    #Process to search subject
    if sub_opt == 1:
        cursor.execute("SELECT * FROM subject WHERE SubjectCode= '"+ GetSubCode()+"'")
        data = cursor.fetchall()
        for item in data:
            print ("Subject Code : ",item[0])
            print ("Subject name: ",item[1])
            
    #Process to add a new subject
    elif sub_opt == 2 :
        SQLtext = "INSERT INTO subject (SubjectCode,Name) VALUES (%s,%s)"
        userValues = (GetSubCode(),GetSubName())
        cursor.execute(SQLtext,userValues)
        DBcommands ()

    #Process to edit a existing subject (option 3)
    elif sub_opt == 3 :
        print("\nFirst enter the data you want to replace the current entry with then the relavent subject number,")
        cursor.execute ("UPDATE subject SET Name='"+GetSubName()+"' WHERE SubjectCode="+GetSubCode()+"")
        DBcommands ()

    #Process to delete a existing subject (option 3)
    elif sub_opt == 4 :
        print ("\nEnter the subject code of the entry which needs to be deleted")
        cursor.execute ("DELETE FROM subject WHERE SubjectCode ="+ GetSubCode()+"")
        DBcommands ()

