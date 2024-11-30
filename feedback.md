## Meryl and Eyal
1. Your hackathon is really great, your code is well structured, clean and readable. The idea is well thinked and the exection and the result are really good. 
2. I like that you weren't afraid to use modules and python's functionalities we didn't learn in class. That is a really good point for a developer!
3. I can tell by your readme fiile that you know what youve done and how youve done it, I will just suggest next time that every one will explain his part so meryl will explain what she has done in this project and Eyal will explain his part, instead of talking by "we".
4. As I said the code is really great adn readable but ive noticed one small issue, more a code building error: in the file sessions.py all of the sessions function are really repetitive they repeat them self expect of a few words. I would suggest next time to focus also on how you can make your code better and smaller. In thus case you could concact the functions on one and pass what you need to be change as an argument.

1. Your hackathon project is exellent! The code is well-structured, clean, and readable. The idea is well-thought-out, and the execution and results are great.
2. I liked that you weren't afraid to use modules and Python functionalities that we didn't learn in class. That shows initiative and is a great quality for a developer!
3. From your README file, I can tell that you clearly understand what you've done and how you've done it. However, I suggest that next time, each team member explains their specific work. For example, Meryl could describe her part, and Eyal could detail his part, rather than using "we" to describe everything.
4. As mentioned, the code is really great and readable, but I noticed a small issue, more of a structural issue. In the sessions.py file, all of the session functions are repetitive and only differ by a few words. Next time, try to improve your code by combining similar functions into one and using arguments to change the specific parts. This will make the code shorter and easier to manage.

def sessions(sound, session_name):
    stop_event = threading.Event()

    # Start the music in a separate thread
    music_thread = threading.Thread(target=play_sound, args=(sound, stop_event))
    music_thread.start()

    # Start the listener for the exit command in another thread
    exit_thread = threading.Thread(target=listen_for_exit, args=(stop_event,))
    exit_thread.start()

    try:
        session = select_random_session(session_name)
        display_instructions(session, 30, stop_event)
    finally:
        # Ensure both threads stop gracefully
        stop_event.set()
        music_thread.join()  # Wait for music thread to finish
        exit_thread.join()   # Wait for exit thread to finish
        print(f"End of the session {session['name']}")

sessions("yoga", "Yoga")
sessions("water", "Mediatation")
sessions("focus", "Focus")
sessions("breathing meditation", "Breathing")
sessions("water", "Sleep")

Here i concat for you 100 lines of code in 25, the magic of functions✨✨

5. Kol Akavod you did a wonderfull job!
