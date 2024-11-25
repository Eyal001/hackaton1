import pg8000
import getpass
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
                password = getpass.getpass ('Chose a password : ')
                query = f''' INSERT INTO users (username, password) VALUES ('{user_name}', '{password}') ''' 
                cursor.execute(query)
                connection.commit()
                user = Users ()
                user.username = user_name

                cursor.execute(f'''SELECT user_id FROM users WHERE username = '{user_name}' ''')
                connection.commit()
                user.user_id = cursor.fetchone()[0]
                print ('Now sign in please : ')
                Users.sign_in ()
                return user

            else : 
                print ('Sorry this username is not available')

    @classmethod 
    def sign_in (cls) :
        usernames = Users.get_usernames()
        while True :
            username = input ('Enter your username : ').lower()
            if [username] in usernames :
                cursor.execute(f''' SELECT user_id, password FROM users WHERE username = '{username}' ''' )
                connection.commit
                results = cursor.fetchone()
                good_password = results[1]
                userid = results[0]
                password = getpass.getpass  ('Enter your password : ')
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
                answer = input ('Y / N :').lower()
                if answer == 'y' :
                    user = Users.sign_up()
                    return user
                else :
                    break

    def save_exercise (self, exercise) :
        cursor.execute (f''' SELECT exercise_id FROM exercises WHERE name = '{exercise}' ''')
        connection.commit
        exercise_id = cursor.fetchone()[0]

        cursor.execute(f'''INSERT INTO user_exercises (user_id, exercise_id) VALUES ({self.user_id}, {exercise_id})''')
        connection.commit()

    def save_feelings(self, notes):
    # Check if an entry exists for today
        query = f'''
            SELECT COUNT(*) 
            FROM feelings 
            WHERE user_id = {self.user_id} AND date = CURRENT_DATE;
        '''
        cursor.execute(query)
        exists = cursor.fetchone()[0] > 0

        if exists:
            # Update the existing record
            query = f'''
                UPDATE feelings
                SET relaxation = {notes[0]}, stress = {notes[1]}, anger = {notes[2]}
                WHERE user_id = {self.user_id} AND date = CURRENT_DATE;
            '''
        else:
            # Insert a new record
            query = f'''
                INSERT INTO feelings (user_id, relaxation, stress, anger, date)
                VALUES ({self.user_id}, {notes[0]}, {notes[1]}, {notes[2]}, CURRENT_DATE);
            '''
        cursor.execute(query)
        connection.commit()

    def fetch_user_feelings(self):
        query = f'''
            SELECT relaxation, stress, anger , date
            FROM feelings 
            WHERE user_id = {self.user_id}
            ORDER BY date;
        '''
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    








# connection.close()