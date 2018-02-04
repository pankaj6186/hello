from detail import spy_salutation, spy_name, spy_age, spy_rating
def start_chat(spy_salutation, spy_name, spy_age, spy_rating):
    show_menu=True
    while show_menu:
        menu_choice=input("what u want to do? \n 1.add a status.\n0.Exit \n")
        if menu_choice==1:
            spy_status=raw_input("add your status")
            print"Updated status is "+spy_status
        elif menu_choice==0:
            show_menu = False
            print"Exit successfull"
        else:


            print"invalid choice"

print"Hello"
print"welcome to the world of spy"
print'let\'s get started'


spy_exist=raw_input("Are you an exsting user(Y or N)")
if spy_exist.upper() =="Y":
    print "welcome "+spy_salutation+ spy_name+" age is %d:"%(spy_age)+" rating is %.3f"%(spy_rating)+" proud to be on board"

    start_chat(spy_salutation, spy_name, spy_age, spy_rating)
elif spy_exist.upper() =="N":

    spy_name=raw_input("please enter ur name")
    if len(spy_name)>3:

        spy_salutation=raw_input("what i call u(Mr. or Ms.)")
        print "welcome "+ spy_salutation +spy_name +" to the world of possibilities of spy"
        print"Glad to meet u.I would like to know more about u."

        spy_age=input("what is your age ")
        if 12<spy_age<50:
            print "%s"%(spy_age) + " is valid to be the age of a spy"

            spy_rating=input("please enter ur rating")
            if spy_rating >= 5:
                print"Good spy"
            elif 3.5<=spy_rating<5:
                print"average spy"
            elif spy_rating<3.5:
                print"bad spy"


            else:
                print"not a valid rating"

            print"AUTHENTICATION COMPLETE.Welcome" + spy_name + " age is %d: " %(spy_age) + " and rating is %.3f" % (spy_rating) + " Proud to be on board."
            start_chat(spy_salutation,spy_name, spy_age, spy_rating)





        else:
            print"not appropriatep age to be a spy"

    else:
        print "invalid name enter a valid name"
else:
    print"invalid choice"


