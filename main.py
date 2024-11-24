from database import *
from menu import *

def main () :
    print ('Hello, welcome on my Stress Reduce App \nPlease sign in : ')
    user = Users.sign_in ()

    print ('''What do you want to do ?
           Choose a session (S)
           Show your graph feelings (G)''')
    
    while True :

        answer = input ('Answer (S / G) : ')
        if answer == 'S' :
            choose_session(user)
            get_feelings (user)
        
        elif answer == 'G' :
            plot_feelings(user)
            

        
        else :
            print ('Invalid answer, only S or G : ')


    
    
    

main ()