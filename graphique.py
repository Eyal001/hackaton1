import matplotlib.pyplot as plt
from database import *


def get_feelings(user):
    questions = [
        "How do you evaluate your relaxation level today ? (1 à 5)",
        "What is your stress level today ? (1 à 5)",
        "How do you rate your anger level today ? (1 à 5)"
    ]
    notes = []
    for question in questions:
        while True:
            try:
                note = int(input(question + " "))
                if note in {1, 2, 3, 4, 5} :
                    if 1 <= note <= 5:
                        notes.append(note)
                        break
                else:
                    print("Enter a number between 1 and 5.")
            except ValueError:
                print("Enter a valid number.")
    user.save_feelings(notes)
    return notes


def plot_feelings(user):
    data = user.fetch_user_feelings()
    
    if not data:
        print("No feelings data found for the user.")
        return
    
    # Extracting values from the data
    dates = [entry[3] for entry in data]  
    relaxation = [entry[0] for entry in data] 
    stress = [entry[1] for entry in data]  
    anger = [entry[2] for entry in data]  
    
    # Plotting the graph
    plt.figure(figsize=(10, 6))
    
    # Plot each feeling level
    plt.plot(dates, relaxation, label="Relaxation", marker="o", linestyle="-", color="blue")
    plt.plot(dates, stress, label="Stress", marker="o", linestyle="--", color="green")
    plt.plot(dates, anger, label="Anger", marker="o", linestyle=":", color="red")
    
    # Formatting the plot
    plt.title(f"Feelings Evolution for {user.username.title()}", fontsize=16)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Feeling Level (1-5)", fontsize=12)
    
    # Formatting the dates on x-axis
    plt.xticks(dates, [date.strftime("%Y-%m-%d") for date in dates], rotation=45, fontsize=10)
    
    # Show the legend and grid
    plt.legend(fontsize=12)
    plt.grid(alpha=0.3)
    plt.tight_layout()
    
    # Display the plot
    plt.show()

