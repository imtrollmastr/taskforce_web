username = input("Enter given username: ")
access = input("Enter given access code: ")
currenttime = input("Enter current time: ")
if username == "tskforce_johann" and access == "9271" or username == "tskforce_user1" and access == "9271" or username == "tskforce_user2" and access == "9271" or username == "tskforce_user3" and access == "9271":
    print("Welcome, " + username + ".")
    print("Last logged in: " + currenttime)
    i = 0
    while i <100:
        inputcommand = input("State your command: ")
        if inputcommand == ".breakserver":
            while i == 0:
                print("0001010100010101010000111100000101010100101")
        elif inputcommand == ".chat":
            anotherusr = input("If there is another user, enter name here: ")
            print("User A: " + username)
            if not anotherusr == "":
                print("User B: " + anotherusr)
            i = 0
            while i <100:
                usrfind = input("Select user: ")
                if usrfind == "a":
                    msginput = input("Enter message here: ")
                    print(username + ": " + msginput)
                elif usrfind == "b":
                    msginput = input("Enter message here: ")
                    print(anotherusr + ": " + msginput)
        elif inputcommand == ".playgame":
            start = input("Type 'start' to play Adventure Road.")
            if start == "start":
                import time
                plrname = input("Enter player name: ")
                plrcity = input("Enter town name: ")
                print("One day, " + plrname + " went to grab some milk at a grocery store.")
                time.sleep(5)
                print("He realized no one was in the store, and ran away with the milk.")
                time.sleep(5)
                print("Suddenly, " + plrname + " dropped into a portal and became a knight.")
                time.sleep(5)
                print("He landed in " + plrcity + ", where a ruthless king ruled.")
                time.sleep(3)
                que1 = input("Will you assasinate the king or get some rest?")
                if que1 == "assasinate the king" or que1 == "assasinate":
                    que2 = input("You became the new king of" + plrcity +", will you be a nice or reasonable king?")
                    if que2 == "yes":
                        print("The citizens respect you and helped you advance " + plrcity)
                    elif que2 == "no":
                        print("The citizens overthrew you and you died.")
                elif que1 == "get some rest":
                    print("A troll put drops of poison in your mouth while you were snoring")
        elif inputcommand == ".checkaccount":
            print("Your username is: " + username)
            print("Your access code is: " + access)
            print("Last logged in was: " + currenttime)
        elif inputcommand == ".trigger":
            target = input("What is the name of your trigger target: ")
            if target == username:
                print("I am unable to trigger " + username + ".")
            else:
                print(target + " went to dispose waste, E-I-E-I-O")
        elif inputcommand == ".switchadmin":
            verificationusr = input("Enter an administrator username: ")
            verificationpsw = input("Enter administrator password: ")
            if verificationusr == "localadmin" and verificationpsw == "A2i9%Sf90a":
                print("Welcome, " + verificationusr + " to the administrator panel.")
                i = 0
                while i <100:
                    admincommand = input("State administrator only commands: ")
                    if admincommand == ".changeaccesscode":
                        changeaccessinput = input("Change access code to: ")
                        access = changeaccessinput
                        if access == changeaccessinput:
                            print("Access code successfully changed.")
                            print("Terminal will now shutdown the running program.")
                            import random
                            import time
                            loading = print("Loading...")
                            time.sleep(random.randint(1, 5))
                            loading = print("Loading..")
                            time.sleep(random.randint(1, 5))
                            loading = print("Loading.")
                            time.sleep(random.randint(1, 5))
                            loading = print("Loading..")
                            time.sleep(random.randint(1, 5))
                            loading = print("Loading...")
                            time.sleep(random.randint(1, 5))
                            loading = print("Loading..")
                            quit()
        else:
            print("You must state a command from the following list: ")
            print(".breakserver - Display infinite binary numbers across your terminal.")
            print(".checkaccount - Check your account information.")
            print(".trigger - Trigger someone except yourself.")
            print(".switchadmin - Switch to administrator login.")
else:
    print("Incorrect username or password.")