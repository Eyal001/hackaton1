# hackaton1 Eyal and Meryl

We made an app that help people relaxing and follow his feelings day by day . 

in the database.py :

We connected it using DB on neon, we have multiple tables 
-> users with user_id username and password 
-> exercises with exercise_id and name of the exercise 
-> user_exercises wich have for FK user_id and exercise_id, and a date to follow wich exercise did a user and when
->feelings with FK user_id, and relaxation stress and anger wich are numbers between 1 and 5. We use this table to display the graph .

in spotify.py :

We fetch API from spotify to search for music and get the preview URL that we are listenning to in the exercises

in sessions.py :
We are reading the json file 'exercises sessions.json' and display step by step a random exercise depending on the user choice 

in menu.py :
Waiting for the user to chose wich exercise he wants to do 

in graphique.py :
We have a questionary that enter the DATA inside the feelings table 
And we fetch this data depending on the user_id and display the graph of the user s feelings 

finally in main.py :
We connect everything together :
sign in so we crease a Users' class object 
and call the different functions depending on the user's choices.