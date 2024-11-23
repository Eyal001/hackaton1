import time
import json
import random
from spotify import *


def load_json():
  with open("exercises_sessions.json", 'r') as file:
    data = json.load(file)
    return data
 
data = load_json()  
  
def select_random_session(exercise_type):
  filtered_sessions = [session for session in data["relaxation_exercises"] if session["type"] == exercise_type]
  selected_session = random.choice(filtered_sessions)
  return selected_session

def display_instructions(session, interval_secondes=30):
  print(f"Starting the session: {session['name']}\n")
  instructions = session["description"]
  
  for index, instruction in enumerate(instructions):
    print(f"Step {index}: {instruction}")
    time.sleep(interval_secondes)
  
def show_all_instruction(session, duration_in_minutes):
  print(f"Starting the session: {session['name']}\n")
  
  print(session["description"])
  
  total_time_sec = duration_in_minutes * 60
  print(f"\nSession will end in {duration_in_minutes} minutes.")
  time.sleep(total_time_sec)
  print(f"\n{session['name']} session finished!")
  
  

def yoga_session():
  stop_event = threading.Event()
  music_thread = threading.Thread(target=play_sound, args=("yoga", stop_event))
  music_thread.start()
  try:
    session = select_random_session("Yoga")
    display_instructions(session, 30)
  finally:
    stop_event.set()
    music_thread.join()
    print(f"End of the session {session['name']}")
    



def meditation_session():
  stop_event = threading.Event()
  music_thread = threading.Thread(target=play_sound, args=("water", stop_event))
  music_thread.start()
  try:
    session = select_random_session("Meditation")
    display_instructions(session, 30)
  finally:
    stop_event.set()
    music_thread.join()
    print(f"End of the session {session['name']}")
    
    
    

def focus_session():
  stop_event = threading.Event()
  music_thread = threading.Thread(target=play_sound, args=("focus", stop_event))
  music_thread.start()
  try:
    session = select_random_session("Focus")
    display_instructions(session, 30)
  finally:
    stop_event.set()
    music_thread.join()
    print(f"End of the session {session['name']}")
    


def breathing_session():
  stop_event = threading.Event()
  music_thread = threading.Thread(target=play_sound, args=("breathing meditation", stop_event))
  music_thread.start()
  try:
    session = select_random_session("Breathing")
    show_all_instruction(session, 1)
  finally:
    stop_event.set()
    music_thread.join()
    print(f"End of the session {session['name']}")
    
    
    
    

def sleep_session():
  stop_event = threading.Event()
  music_thread = threading.Thread(target=play_sound, args=("water", stop_event))
  music_thread.start()
  try:
    session = select_random_session("Sleep")
    display_instructions(session, 30)
  finally:
    stop_event.set()
    music_thread.join()
    print(f"End of the session {session['name']}")
