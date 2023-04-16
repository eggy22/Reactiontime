import tkinter as tk
import random
import time


# Define a function to start the test
def start_test():
    global start_time # Declare the variable as global
    start_button.config(state="disabled")
    wait_time = random.uniform(1, 5) # Generate a random wait time between 1 and 5 seconds
    time.sleep(wait_time)
    box.config(bg="green") # Change the color of the box to green
    start_time = time.time() # Record the start time

# Define a function to handle the click on the box
def box_clicked(event):
    end_time = time.time() # Record the end time
    reaction_time = round((end_time - start_time) * 1000, 2) # Calculate the reaction time in milliseconds
    result_label.config(text=f"Your reaction time is {reaction_time}ms")
    box.config(text=f"{reaction_time}ms", bg="red", fg="white", font=("Helvetica", 18)) # Display the reaction time inside the box with a larger font and change the color to red
    start_button.config(state="normal")

# Create the main window
root = tk.Tk()
root.title("Reaction Time Test")

# Create the start button
start_button = tk.Button(root, text="Click to Start", command=start_test, bg="red", fg="white", font=("Helvetica", 18))
start_button.pack(pady=10)

# Create the box
box = tk.Label(root, bg="red", width=150, height=50)
box.pack(pady=10)
box.bind("<Button-1>", box_clicked)

# Create the result label
result_label = tk.Label(root, text="", font=("Helvetica", 18))
result_label.pack(pady=10)

# Start the tkinter event loop
root.mainloop()
