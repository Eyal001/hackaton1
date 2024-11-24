from database import *
from menu import *

def main () :
    print ('Hello, welcome on my Stress Reduce App \nPlease sign in : ')
    user = Users.sign_in ()

    print ('''What do you want to do ?
           Choose a session (S)
           Show your graph feelings (G)
           Fill the questionary (Q)
           Exit (E)''')
    
    while True :

        answer = input ('Answer (S / G / Q) : ')
        if answer == 'S' :
            choose_session(user)
            get_feelings (user)
            plot_feelings(user)
            break

        
        elif answer == 'G' :
            plot_feelings(user)

        elif answer == 'Q' :
            get_feelings (user)
            
        elif answer == 'E' :
            print ('See you soon ! Exiting...')
            break

        
        else :
            print ('Invalid answer, only S, G, Q or E : ')


    
    
    

main ()