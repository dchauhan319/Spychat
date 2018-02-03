print "Hello"
print "Welcome to Spychat"
spy_exist = raw_input("Already exist Y or N")
if spy_exist.upper()== "Y" :
    spy_name = raw_input("What is your Spy name")
    if len(spy_name)>=2:
        print spy_name
        spy_sal = raw_input("What should we call you Mr. or Miss")
        spy_name= spy_sal+" "+spy_name
        print "Alright "+ spy_name + " "+ "Lets know more about you"
        spy_age= input("Enter your age")
        if (spy_age)>13 and (spy_age)<50 :
            print "You are eligible to be a spy"
            spy_rating = input("What is your Spy rating")
            if spy_rating >= 5.0:
                print "Great Spy"
            elif spy_rating < 5.0 or spy_rating > 3.0:
                print "Good Spy"
            else:
                print "Bad Spy"
        else:
            print "Wrong choice"
    else:
        print "Invalid name"
else:
    print "Invalid Spy"