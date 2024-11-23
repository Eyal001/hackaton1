import pg8000

import os
from dotenv import load_dotenv

load_dotenv()


connection = pg8000.connect(database =os.getenv('PGDATABASE'),
                              user = os.getenv('PGUSER'),
                              password = os.getenv('PGPASSWORD'),
                              host=os.getenv('PGHOST'),
                              port='5432')

cursor = connection.cursor()

class Users :
    def __init__(self):
        self.user_id = 0
        self.username = ''

    @classmethod
    def get_usernames(cls):
        query = f''' SELECT username FROM users '''
        cursor.execute(query)
        connection.commit()
        usernames = list(cursor.fetchall())
        return usernames

    @classmethod
    def sign_up (cls):
        usernames = Users.get_usernames()

        while True :

            user_name = input ('Chose a username : ').lower()
            if [user_name] not in usernames :
                password = input ('Chose a password : ')
                query = f''' INSERT INTO users (username, password) VALUES ('{user_name}', '{password}') ''' 
                cursor.execute(query)
                connection.commit()
                user = Users ()
                user.username = user_name

                cursor.execute(f'''SELECT user_id FROM users WHERE username = '{user_name}' ''')
                connection.commit()
                user.user_id = cursor.fetchone()[0]
                return user

            else : 
                print ('Sorry this username is not available')

    @classmethod 
    def sign_in (cls) :
        usernames = Users.get_usernames()
        while True :
            username = input ('username : ').lower()
            if [username] in usernames :
                cursor.execute(f''' SELECT user_id, password FROM users WHERE username = '{username}' ''' )
                connection.commit
                results = cursor.fetchone()
                good_password = results[1]
                userid = results[0]
                password = input ('Password : ')
                if password == good_password :
                    print ('Successfully logged in !')
                    user = Users()
                    user.username = username
                    user.user_id = userid
                    return user
                else :
                    print ('Wrong password, try again !')
            else :
                print ('This username does not exist, would you like to sign up ?')
                answer = input ('Y / N :')
                if answer == 'Y' :
                    Users.sign_up()
                else :
                    break



Users.sign_in()




connection.close()