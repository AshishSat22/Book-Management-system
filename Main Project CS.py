import mysql.connector


DB=mysql.connector.connect(host="localhost",
                           user="root",
                           password="ashish",
                           database="book_store"
)

C=DB.cursor()


#ADMIN FUNCTIONS

def ADD():
              book=str(input("Enter Book Name: "))
              genre=str(input("Genre:"))
              quantity=int(input("Enter quantity:"))        
              author=str(input("Enter author name:"))
              publication=str(input("Enter publication house:"))
              price=int(input("Enter the price:"))
              C.execute("INSERT INTO available_books values('{}','{}',{},'{}','{}',{})".format(book,genre,quantity,author,publication,price))

              DB.commit()
              print("""++++++++++++++++++++++++SUCCESSFULLY ADDED++++++++++++++++++++++++""")
              n=int(input("""Want To Continue:
                    Yes: 1
                    NO: 2
                    OPTION: """ ))
              if n==1:
                  ADD()
              if n==2:
                  Staff()
              


def NewStaff():
    fname=str(input("Enter Fullname:"))
    gender=str(input("Gender(M/F/O):"))
    age=int(input("Age:"))
    phno=int(input("Staff phone no.:"))
    add=str(input("Address:"))
               
    C.execute(("INSERT INTO staff_details values('{}','{}',{},{},'{}')".format(fname,gender,age,phno,add)))
    DB.commit()
               
    print("""+++++++++++++++++++++++++++++
                +STAFF IS SUCCESSFULLY ADDED+
            +++++++++++++++++++++++++++++""")
    
    n=int(input("""Want To Continue:
                    Yes: 1
                    NO: 2
                    OPTION: """ ))
    if n==1:
        NewStaff()
    if n==2:
        Staff()
    


def RemoveStaff():
    n=(input("Staff Name to Remove: "))
    C.execute("DELETE FROM staff_details WHERE Name=('{}') ".format(n))
                      
    DB.commit()
    print("Above Employee is promoted to Customer")
    n=int(input("""Want To Continue:
                    Yes: 1
                    NO: 2
                    OPTION: """ ))
    if n==1:
        RemoveStaff()
    if n==2:
        Staff()
    

def StaffDetailfS():
    spl_statement= "Select * from staff_details"
    C.execute(spl_statement)
    output =C.fetchall()
    for x in output:
        print("************************************")
        print("Name of Employ:", x[0])
        print("Gender of Employ:", x[1])
        print("Age of Employ:", x[2])
        print("Phone No of Employ", x[3])
        print("Address of Employ:", x[4])
        print("************************************")
    n=int(input("""Want To Continue:
                    Yes: 1
                    NO: 2
                    OPTION: """ ))
    if n==1:
        StaffDetailS()
    if n==2:
        Staff()
        

def SellRec():
    C.execute("select * from sell_rec")
    for u in C:
        print("*********************************************")
        print("Buyer Name: ",u[0])
        print("Buyer Mobile Number: ",u[1])
        print("Book Purchased: ",u[2])
        print("Quantity Brought: ",u[3])
        print("Price of Book: ",u[4])
        print("**********************************************")
    n=int(input("""Want To Continue:
                    Yes: 1
                    NO: 2
                    OPTION: """ ))
    if n==1:
        SellRec()
    if n==2:
        Staff()                        


def DelRec():
    bb=input("Are you sure(Y/N):").upper()
    if bb=="Y":
        C.execute("delete from sell_rec")
        DB.commit()
    n=int(input("""Want To Continue:
                    Yes: 1
                    NO: 2
                    OPTION: """ ))
    if n==1:
        DelRec()
    if n==2:
        Staff()   
    

def TotalIncome():
    C.execute("select sum(price) from sell_rec")
    for x in C:
        print("Total Sell Till Date",x)
    n=int(input("""Want To Continue:
                    Yes: 1
                    NO: 2
                    OPTION: """ ))
    if n==1:
        TotalIncome()
    if n==2:
        Staff()    


def AvailablefS():
    C.execute("select * from available_books order by bookname")

    for v in C:
        print("****************************************************")
        print("Book Name: ",v[0])
        print("Book Genre: ",v[1])
        print("Book Available: ",v[2])
        print("Book Author: ",v[3])
        print("Publication House: ",v[4])
        print("Book Price:  ", v[5])
        print("****************************************************")
    n=int(input("""Want To Continue:
                    Yes: 1
                    NO: 2
                    OPTION: """ ))
    if n==1:
        AvailablefS()
    if n==2:
        Staff()    


#***************************************BUYER FUNCTION********************************************

def AvailablefU():
    C.execute("select * from available_books order by bookname")

    for v in C:
        print("****************************************************")
        print("Book Name: ",v[0])
        print("Book Genre: ",v[1])
        print("Book Available: ",v[2])
        print("Book Author: ",v[3])
        print("Publication House: ",v[4])
        print("Book Price:  ", v[5])
        print("****************************************************")
    n=int(input("""Want To Continue:
                    Yes: 1
                    NO: 2
                    OPTION: """ ))
    if n==1:
        AvailablefU()
    if n==2:
        Buyer()    

def StaffDetailfU():
    spl_statement= "Select * from staff_details"
    C.execute(spl_statement)
    output =C.fetchall()
    for x in output:
        print("************************************")
        print("Name of Employ:", x[0])
        print("Gender of Employ:", x[1])
        print("Age of Employ:", x[2])
        print("Phone No of Employ", x[3])
        print("Address of Employ:", x[4])
        print("************************************")
    n=int(input("""Want To Continue:
                    Yes: 1
                    NO: 2
                    OPTION: """ ))
    if n==1:
        StaffDetailfU()
    if n==2:
        Buyer()




def Purchase():
           print("AVAILABLE BOOKS...")
           C.execute("select * from available_Books ")
           for i in C:
                print("****************************************************")
                print("Book Name: ",i[0])
                print("Book Genre: ",i[1])
                print("Book Available: ",i[2])
                print("Book Author: ",i[3])
                print("Publication House: ",i[4])
                print("Book Price:  ", i[5])
                print("****************************************************")


           cusname=str(input("Enter customer name:"))
           phno=int(input("Enter phone number:"))
           book=str(input("Enter Book Name:"))
           price=int(input("Enter the price:"))
           n=int(input("Enter quantity:"))
           C.execute("select quantity from available_books where bookname='"+book+"'")
           k=C.fetchone()

           if max(k)<n:
               print(n,"Books are not available!!!!")
           else:
              C.execute("select bookname from available_books where bookname='"+book+"'")
              log=C.fetchone()

              if log is not None:
                  C.execute("insert into Sell_rec values('"+cusname+"','"+str(phno)+"','"+book+"','"+str(n)+"','"+str(price)+"')")
                  C.execute("update Available_Books set quantity=quantity-'"+str(n)+"' where BookName='"+book+"'")
                  DB.commit()
                  print("""++++++++++++++++++++++
                            ++BOOK HAS BEEN SOLD++
                            ++++++++++++++++++++++""")
              else:
                 print("BOOK IS NOT AVAILABLE!!!!!!!")

              n=int(input("""Want To Continue:
                    Yes: 1
                    NO: 2
                    OPTION: """ ))
              if n==1:
                 Purchase()
              if n==2:
                Buyer()
    
           
def UsingName():
               o=input("Enter Book to search:")

               C.execute("select bookname from available_books where bookname ='"+o+"'")
               t=C.fetchone()

               if t != None:
                         print("""++++++++++++++++++++
                                ++BOOK IS IN STOCK++
                                ++++++++++++++++++++""")
               else:
                         print("BOOK IS NOT IN STOCK!!!!!!!")
                         
               n=int(input("""Want To Continue:
                    Yes: 1
                    NO: 2
                    OPTION: """ ))
               if n==1:
                 UsingName()
               if n==2:
                 Buyer()

    
def UsingGenre():
      g=input("Enter genre to search:")
      C.execute("select genre from available_books where genre= '"+g+"'")
      poll=C.fetchall()
      if poll is not None:
                                    print("""++++++++++++++++++++
                                               ++BOOK IS IN STOCK++
                                               ++++++++++++++++++++""")
                                
                                    C.execute("select * from available_books where genre='"+g+"'")
                                
                                    for y in C:
                                           print("*******************************************")
                                           print("Book Name: ",y[0])
                                           print("Book Genre: ",y[1])
                                           print("Quantity Available: ",y[2])
                                           print("Book Author", y[3])
                                           print("Book Publication: ",y[4])
                                           print("Book Price: ", y[5])
                                           print("*******************************************")

                                    else:
                                           print("BOOKS OF SUCH GENRE ARE NOT AVAILABLE!!!!!!!!!")

      n=int(input("""Want To Continue:
                    Yes: 1
                    NO: 2
                    OPTION: """ ))
      if n==1:
                        UsingGenre()
      if n==2:
                        Buyer() 

def UsingAuthor():
               o=input("Enter Book's Author to search:")

               C.execute("select bookname from available_books where Author ='"+o+"'")
               t=C.fetchone()
              
               if t != None:
                         print("""++++++++++++++++++++
                                ++BOOK IS IN STOCK++
                                ++++++++++++++++++++""")
               else:
                         print("BOOK IS NOT IN STOCK!!!!!!!")
      
               n=int(input("""Want To Continue:
                    Yes: 1
                    NO: 2
                    OPTION: """ ))
               if n==1:
                        UsingGenre()
               if n==2:
                        Buyer()

                    
def Staff():
        print(""" 1:Add Books
                2.Staff Details
                3.Sell Record
                4.Total Income after the Latest Reset
                5. See Available Book
                6. Exit""")
    
        n=int(input("Enter Your Choice: "))
        

#To Add Books into the database

        if n==1:
             ADD()
        
        
#Choice For New Staff, Fire staff, View Staff

         
        if n==2:
             print("""1:New staff entry)
                   2:Remove staff
                   3:Existing staff details""")

             ch=int(input("Enter your choice: "))
             

#NEW STAFF ENTRY

         
             if ch==1:
                 NewStaff()

#REMOVE STAFF
                    
                
             if ch==2:
                 RemoveStaff()

#EXISTING STAFF DETAILS
                      

             if ch==3:
                 StaffDetailfS()
             
#To See Selling histroy & altering it                        


        if n==3:
            print("""1:Sell history details
                  2:Reset Sell history""")
        
            ty=int(input("Enter your choice:"))

            if ty==1:
                SellRec()
            if ty==2:
                DelRec()

#To view total Total Income                         

        if n==4:
            TotalIncome()

#Viewing Available Book As Staff
                  
        if n==5:
            AvailablefS()
            
#Break

        if n==6:
            return


def Buyer():

#USER Choices

                
        print("""1.Purchase Books
               2.Search Books
               3.Available Books
               4.Staff Details
               5. Exit""")

        r=int(input("Enter Your Choice: "))

#TO PURCHASE BOOK    

        if r==1:
            Purchase()

        
#Searching of books using Name,Genre,Author
        
        if r==2:
            print("""1:Search by name
                      2:Search by genre
                      3:Search by author""")

            l=int(input("Search by What : "))

#Searching Using Name of Book

            if l==1:
                UsingName()

#Searching Using Genre of Book
                
            if l==2:
                UsingGenre()
                
#Searching Using Author Name

            if l==3:
                UsingAuthor()


#To See Available Books
        
        if r==3:
            AvailablefU()

#To See Present Staff Details
            
        if r==4:
            StaffDetailfS()


    








print("**********************************************Welcome To Book Store***************************************************")
while 1:
    
    a=int(input("""Enter as Employee: 1
                        Enter as User: 2
                        Exit : 3
                        Enter : """ ))

    if a==1:
            Staff()

    if a==2:
        print('''''****************BOOK SHOP*********************
           1. Signup
           2. login''')
        s=int(input("Enter Your Choice: "))
        

#Sign-Up

        if s==1:
           user_name=input("USERNAME(ex: abcd1234): ")
           password=input("PASSWORD: ")
       
           C.execute("insert into signup values('"+user_name+"','"+password+"')")
           DB.commit()

           print("Sign Up Completed")
           

#Log in
       
        else:
            user2= input("Enter Your Username: ")
            C.execute("select username from Signup where username='"+user2+"'")
            b=C.fetchone()
            b1=input("Enter Your Password: ")
            C.execute("select password from signup where password='"+b1+"'")
            a2=C.fetchone()
            if a2 is not None:
                    print("************************Login Success********************")

        Buyer()
        

    if a==3:
        break
