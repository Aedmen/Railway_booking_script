raj = ["1","2","3","4","5","6","7","8","9","10"]
jan = ["1","2","3","4","5","6","7","8","9","10"]
naga = ["1","2","3","4","5","6","7","8","9","10"]
bg = ["1","2","3","4","5","6","7","8","9","10"]


class Train:

    def bookATicket(self,name,date,type,train):
        self.name = name
        self.date = date
        self.type = type
        self.train = train
        i_raj = 0
        i_jan = 0
        i_naga = 0
        i_bg = 0
        ticket = 0
        i = 0
        if train == "1":
            for i_raj in range(len(raj)):
                if raj[i].isdigit() is True:
                    raj.pop(i_raj)
                    raj.insert(i_raj,name.lower())
                    ticket = raj.index(name.lower())+1
                    break
                else:
                    i+=1
        elif train == "2":
            for i_jan in range(len(jan)):
                if jan[i].isdigit() is True:
                    jan.pop(i_jan)
                    jan.insert(i_jan,name.lower())
                    ticket = jan.index(name.lower())+1
                    break
                else:
                    i+=1
        elif train == "3":
            for i_naga in range(len(naga)):
                if naga[i].isdigit() is True:
                    naga.pop(i_naga)
                    naga.insert(i_naga,name.lower())
                    ticket = naga.index(name.lower())+1
                    break
                else:
                    i+=1
        else:
            for i_bg in range(len(bg)):
                if bg[i].isdigit() is True:
                    bg.pop(i_bg)
                    bg.insert(i_bg,name.lower())
                    ticket = bg.index(name.lower())+1
                    break
                else:
                    i+=1
        

        print(f"Your seat has been booked according to the details : \nName = {self.name}\nDate = {self.date}\nType of seat = {self.type}\nTrain = {self.train}\nTicket number: {ticket}")
    
    
    def trainStatus(self,name,train):
        self.name = name
        self.train = train
        ticket = 0
        confirmed = False
        name = name.lower()


        i = 0
        if train == 1:
            for i in range(len(raj)):
                if raj[i] == name.lower():
                    ticket = (raj.index(name.lower())+1)
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
        name = name.lower()

        i = 1
        cancel = False
        cancel_statement = False
        while cancel is False:
            if train == 1:
                for i in range(len(raj)):
                    if raj[i] == name:
                        raj.remove(name)
                        raj.insert(i,str(i+1))
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
                        jan.insert(i,str(i+1))
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
                        naga.insert(i,str(i+1))        
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
                        bg.insert(i,str(i+1))
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

