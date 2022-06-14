# Not complete
# The actual question is a lot simpler, this is just a personal project
# Try implimenting a function called cancel ticket
# Basically maintain a list of seats available and if a certain seat number has canceled his seat then append his seat in the list
raj = [1,2,3,4,5,6,7,8,9,10]
jan = [1,2,3,4,5,6,7,8,9,10]
naga = [1,2,3,4,5,6,7,8,9,10]
bg = [1,2,3,4,5,6,7,8,9,10]

i_raj = 0
i_jan = 0
i_naga = 0
i_bg = 0




class Train:

    def bookATicket(self,name,date,type,train):
        self.name = name
        self.date = date
        self.type = type
        self.train = train



        global i_raj
        global i_jan
        global i_naga
        global i_bg
        
        if train == "1":
            raj.pop(i_raj)
            raj.insert(i_raj,self.name)
            ticket = raj.index(name)+1
            i_raj += 1
        elif train == "2":
            jan.pop(i_jan)
            jan.insert(i_jan,self.name)
            ticket = jan.index(name)+1
        elif train == "3":
            naga.pop(i_naga)
            naga.insert(i_naga,self.name)
            ticket = naga.index(name)+1
        else:
            bg.pop(i_bg)
            bg.insert(i_bg,self.name)
            ticket = bg.index(name)+1
        

        print(f"Your seat has been booked according to the details : \nName = {self.name}\nDate = {self.date}\nType of seat = {self.type}\nTrain = {self.train}\nTicket number: {ticket}")
    
    
    def trainStatus(self,name,train):
        self.name = name
        self.train = train
        ticket = 0
        confirmed = False


        i = 0
        if train == 1:
            for i in range(len(raj)):
                if raj[i] == name:
                    ticket = (raj.index(name)+1)
                    confirmed = True
                    break
                   
                else:
                    confirmed  = False
        elif train == 2:
            for i in range(len(jan)):
                if jan[i] == name:
                    ticket = (jan.index(name)+1)
                    confirmed = True
                    break
                else:
                    confirmed  = False
        elif train == 3:
            for i in range(len(naga)):
                if naga[i] == name:
                    ticket = (naga.index(name)+1)
                    confirmed = True
                    break
                else:
                    confirmed  = False
        else:
            for i in range(len(bg)):
                if bg[i] == name:
                    ticket = (bg.index(name)+1)
                    confirmed = True
                    break
                else:
                    confirmed  = False
    
        if confirmed is True:
            print(f"You have a seat confirmed in this train. Your seat number is {ticket}")
        else:
            print("Sorry we cant find a seat corresponding to your name in this train.")

    @staticmethod
    def getInfo():
        print("The trains available are\n1. Rajdhani Express\n2. Janshatapdi\n3. Nagaland Express\n4. B.G. Express")

    def cancelTicket(self,name,train):
        self.name = name
        self.train = train


        i = 1
        cancel = False
        cancel_statement = False
        while cancel is False:
            if train == 1:
                for i in range(len(raj)):
                    if raj[i] == name:
                        raj.remove(name)
                        raj.insert(i,i+1)
                        cancel_statement = True
                        cancel = True
                        break
                    else:
                        cancel = True
                        cancel_statement = False
            elif train == 2:
                for i in range(len(jan)):
                    if jan[i] == name:
                        jan.remove(name)
                        jan.insert(i,i+1)
                        cancel_statement = True
                        cancel = True
                        break
                    else:
                        cancel = True
                        cancel_statement = False
            elif train == 3:
                for i in range(len(naga)):
                    if naga[i] == name:
                        naga.remove(name)        
                        naga.insert(i,i+1)        
                        cancel_statement = True
                        cancel = True
                        break
                    else:
                        cancel = True
                        cancel_statement = False
            elif train == 4:
                for i in range(len(bg)):
                    if bg[i] == name:
                        bg.remove(name)
                        bg.insert(i,i+1)
                        cancel_statement = True
                        cancel = True
                        break
                    else:
                        cancel = True
                        cancel_statement = False
            else:
                print("Please enter a valid input")
                cancel = False
        if cancel_statement is True:
            print("The ticket corresponding to this has been cancelled")
        else:
            print("We couldnt find any ticket corresponding to this name")
    @staticmethod                
    def final():
        final = True
        while final is True:
                again = input("Do you want to go back and use a different feature\nEnter 'Y' to proceed and 'N' to decline : ")
                if again.lower() == "y":
                    final = False
                    return True
                elif again.lower() == "n":
                    final = False
                    return False
                else:
                    print("Please enter a valid input")
                    final = True
a = Train()
intro = False
print("WELCOME TO THE RAILWAY BOOKING SERVICE!")
while intro is False:
    repeat = True
    c = input("Enter 'Y' to proceed and 'N' to decline : ")
    while c.lower() == "y" and repeat is True:
        b = input("Enter the number according to the service you require\n1. Book a ticket\n2. Check your seat status\n3. Get about the trains available\n4. Cancel Ticket\nEnter your option here : ")
        intro = True
        if b == "1":
            name = input("Enter your name = ")
            date = input("Enter date of travel = ")
            type = input("Enter the type of seat you want = ")
            train = input("Enter the number according to the train you wish to book\n1. Rajdhani Express\n2. Janshatapdi\n3. Nagaland Express\n4. B.G. Express\nEnter your option here : ")
            a.bookATicket(name,date,type,train)
            repeat = a.final()
        elif b == "2":
            name = input("Please enter your name to check your seat status : ")
            train = int(input("Enter the number according to the train you booked your ticket\n1. Rajdhani Express\n2. Janshatapdi\n3. Nagaland Express\n4. B.G. Express\nEnter your option here : "))
            a.trainStatus(name,train)
            repeat = a.final()
        elif b == "3":
            a.getInfo()
            repeat = a.final()
        elif b == "4":
            name = input("Enter the name of the ticket you want to cancel : ")
            train = int(input("Enter the train number \n1. Rajdhani Express\n2. Janshatapdi\n3. Nagaland Express\n4. B.G. Express\nEnter your option here : "))
            a.cancelTicket(name,train)
            repeat = a.final()
        else:
            print("Please enter a valid input")

    if c.lower() == "n" or repeat is False:
        print("Thank you for choosing our service")
        intro = True

    else:
        print("This is not a valid input. Please try again")
        intro = False

