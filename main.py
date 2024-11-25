from database import *
from menu import *

def main () :
    
    print ('Hello, welcome on my Stress Reduce App \nPlease sign in : ')
    user = Users.sign_in ()

    if isinstance(user, Users):


        print ('''What do you want to do ?
            Choose a session (S)
            Show your graph feelings (G)
            Fill the questionary (Q)
            Exit (E)''')
        
        while True :

            answer = input ('Answer ((S)ession / (G)raph / (Q)uestionary / (E)xit) : ').lower()
            if answer == 's' :
                choose_session(user)
                

            
            elif answer == 'g' :
                plot_feelings(user)

            elif answer == 'q' :
                get_feelings (user)
                
            elif answer == 'e' :
                print ('See you soon ! Exiting...')
                break

            
            else :
                print ('Invalid answer, only S, G, Q or E : ')
    
    else : 
        print ('You need to sign up first!')


    
    
    

main ()