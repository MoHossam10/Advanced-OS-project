import tkinter as tk

from optimal_algo import optimal_page_replacement
from Clook_Algorithm import CLOOK
from secondt import second_chance
from C_Scan_Algorithm import C_Scan

# Function to open screens for each algorithm
def open_algorithm_screen(algorithm):
    # Hide the main frame
    main_frame.pack_forget()
    
    # Create new frame for the algorithm screen
    algorithm_frame = tk.Frame(root)
    algorithm_frame.pack()

    # Implement logic to display specific content for each algorithm
    if algorithm == "Optimal Algorithm":
        # Display content for Algorithm 1
        algorithm_label = tk.Label(algorithm_frame, text="Enter numbers separated by spaces:")
        algorithm_label.pack()

        # Entry widget to take input from the user
        entry = tk.Entry(algorithm_frame)
        entry.pack(pady=5)

        # Label for number of frames
        num_frames_label = tk.Label(algorithm_frame, text="Enter number of frames:")
        num_frames_label.pack()

        # Entry widget for number of frames
        num_frames_entry = tk.Entry(algorithm_frame)
        num_frames_entry.pack(pady=5)

        error_label = tk.Label(algorithm_frame, text="", fg="red")  # Label to display error messages
        error_label.pack()

        # Label to display page hit
        page_hit_label = tk.Label(algorithm_frame, text="Page Hit: ")
        page_hit_label.pack()

        # Label to display page faults
        page_faults_label = tk.Label(algorithm_frame, text="Page Faults: ")
        page_faults_label.pack()

        def split_input():
            input_text = entry.get()
            num_frames = num_frames_entry.get()
            if ' ' not in input_text:
                error_label.config(text="Values must be separated by spaces.")
                return
            try:
                numbers = [int(num) for num in input_text.split()] 
                num_frames = int(num_frames)
                error_label.config(text="")  
                
                page_hit, page_faults = optimal_page_replacement(numbers, num_frames)
                page_hit_label.config(text="Page Hit: " + str(page_hit))
                page_faults_label.config(text="Page Faults: " + str(page_faults))
            except ValueError:
                error_label.config(text="Invalid input. Please enter integers only.")

        # Button to trigger splitting the input and simulating the algorithm
        split_button = tk.Button(algorithm_frame, text="Get result", command=split_input)
        split_button.pack(pady=5)
        
        # Button to go back to the main screen
        back_button = tk.Button(algorithm_frame, text="Back", command=lambda: back_to_main(algorithm_frame))
        back_button.pack(pady=5)

    elif algorithm == "C-look Algorithm":
        # Display content for C-look Algorithm
        algorithm_label = tk.Label(algorithm_frame, text="Enter numbers separated by spaces:")
        algorithm_label.pack()

        # Entry widget to take input from the user for the list
        entry = tk.Entry(algorithm_frame)
        entry.pack(pady=5)

        # Label for head position
        head_label = tk.Label(algorithm_frame, text="Enter head position:")
        head_label.pack()

        # Entry widget for head position
        head_entry = tk.Entry(algorithm_frame)
        head_entry.pack(pady=5)

        # Label for direction
        direction_label = tk.Label(algorithm_frame, text="Enter direction (left or right):")
        direction_label.pack()

        # Entry widget for direction
        direction_entry = tk.Entry(algorithm_frame)
        direction_entry.pack(pady=5)

        error_label = tk.Label(algorithm_frame, text="", fg="red")  # Label to display error messages
        error_label.pack()

        # Label to display total head movement
        total_movement_label = tk.Label(algorithm_frame, text="Total Head Movement: ")
        total_movement_label.pack()

        # Label to display order of disks served
        order_of_disks_label = tk.Label(algorithm_frame, text="Order of Disks Served: ")
        order_of_disks_label.pack()

        # Function to split input and simulate the algorithm
        def split_input():
            input_text = entry.get()
            head_pos = head_entry.get()
            direction = direction_entry.get().lower()

            if ' ' not in input_text:
                error_label.config(text="Values must be separated by spaces.")
                return
            try:
                numbers = [int(num) for num in input_text.split()]  # Convert each element to integer
                head_pos = int(head_pos)
                if direction not in ['left', 'right']:
                    error_label.config(text="Direction must be 'left' or 'right'.")
                    return
                error_label.config(text="")  # Clear error message if no error
                # Call function to simulate C-look Algorithm
                total_movement, order_of_disks_served = CLOOK(numbers, head_pos, direction)
                # Update labels with results
                total_movement_label.config(text="Total Head Movement: " + str(total_movement))
                order_of_disks_label.config(text="Order of Disks Served: " + ", ".join(map(str, order_of_disks_served)))
            except ValueError:
                error_label.config(text="Invalid input. Please enter integers for numbers and head position.")

        # Button to trigger splitting the input and simulating the algorithm
        split_button = tk.Button(algorithm_frame, text="Get result", command=split_input)
        split_button.pack(pady=5)
        
        # Button to go back to the main screen
        back_button = tk.Button(algorithm_frame, text="Back", command=lambda: back_to_main(algorithm_frame))
        back_button.pack(pady=5)
        
    elif algorithm == "Second Chance Algorithm":
        # Display content for Second Chance Algorithm
        algorithm_label = tk.Label(algorithm_frame, text="Enter numbers separated by spaces:")
        algorithm_label.pack()

        # Entry widget to take input from the user for the list
        entry = tk.Entry(algorithm_frame)
        entry.pack(pady=5)

        # Label for number of frames
        num_frames_label = tk.Label(algorithm_frame, text="Enter number of frames:")
        num_frames_label.pack()

        # Entry widget for number of frames
        num_frames_entry = tk.Entry(algorithm_frame)
        num_frames_entry.pack(pady=5)

        error_label = tk.Label(algorithm_frame, text="", fg="red")  # Label to display error messages
        error_label.pack()

        # Label to display page hit
        page_hit_label = tk.Label(algorithm_frame, text="Page Hit: ")
        page_hit_label.pack()

        # Label to display page faults
        page_faults_label = tk.Label(algorithm_frame, text="Page Faults: ")
        page_faults_label.pack()

        # Function to split input into a list of integers and simulate the algorithm
        def split_input():
            input_text = entry.get()
            num_frames = num_frames_entry.get()
            if ' ' not in input_text:
                error_label.config(text="Values must be separated by spaces.")
                return
            try:
                numbers = [int(num) for num in input_text.split()]  # Convert each element to integer
                num_frames = int(num_frames)
                error_label.config(text="")  # Clear error message if no error
                # Call function to simulate Second Chance Algorithm
                page_hit, page_faults = second_chance(numbers, num_frames)
                # Update labels with results
                page_hit_label.config(text="Page Hit: " + str(page_hit))
                page_faults_label.config(text="Page Faults: " + str(page_faults))
            except ValueError:
                error_label.config(text="Invalid input. Please enter integers only.")

        # Button to trigger splitting the input and simulating the algorithm
        split_button = tk.Button(algorithm_frame, text="Get result", command=split_input)
        split_button.pack(pady=5)
        
        # Button to go back to the main screen
        back_button = tk.Button(algorithm_frame, text="Back", command=lambda: back_to_main(algorithm_frame))
        back_button.pack(pady=5)
        
    elif algorithm =="C-Scan Algorithm":
        # Display content for C-look Algorithm
        algorithm_label = tk.Label(algorithm_frame, text="Enter numbers separated by spaces:")
        algorithm_label.pack()

        # Entry widget to take input from the user for the list
        entry = tk.Entry(algorithm_frame)
        entry.pack(pady=5)

        # Label for head position
        head_label = tk.Label(algorithm_frame, text="Enter head position:")
        head_label.pack()

        # Entry widget for head position
        head_entry = tk.Entry(algorithm_frame)
        head_entry.pack(pady=5)

        # Label for direction
        direction_label = tk.Label(algorithm_frame, text="Enter direction (left or right):")
        direction_label.pack()

        # Entry widget for direction
        direction_entry = tk.Entry(algorithm_frame)
        direction_entry.pack(pady=5)
        # Label for head position
        number_of_cylinders_label = tk.Label(algorithm_frame, text="Enter number of cylinders:")
        number_of_cylinders_label.pack()

        # Entry widget for head position
        number_of_cylinders_entry = tk.Entry(algorithm_frame)
        number_of_cylinders_entry.pack(pady=5)

        error_label = tk.Label(algorithm_frame, text="", fg="red")  # Label to display error messages
        error_label.pack()

        # Label to display total head movement
        total_movement_label = tk.Label(algorithm_frame, text="Total Head Movement: ")
        total_movement_label.pack()

        # Label to display order of disks served
        order_of_disks_label = tk.Label(algorithm_frame, text="Order of Disks Served: ")
        order_of_disks_label.pack()

        # Function to split input and simulate the algorithm
        def split_input():
            input_text = entry.get()
            head_pos = head_entry.get()
            direction = direction_entry.get().lower()
            number_of_cylinders=number_of_cylinders_entry.get()
            if ' ' not in input_text:
                error_label.config(text="Values must be separated by spaces.")
                return
            try:
                numbers = [int(num) for num in input_text.split()]  # Convert each element to integer
                head_pos = int(head_pos)
                if direction not in ['left', 'right']:
                    error_label.config(text="Direction must be 'left' or 'right'.")
                    return
                error_label.config(text="")  # Clear error message if no error

                # Call function to simulate C-look Algorithm
                total_movement, order_of_disks_served = C_Scan(numbers, head_pos, direction,number_of_cylinders)
                # Update labels with results
                total_movement_label.config(text="Total Head Movement: " + str(total_movement))
                order_of_disks_label.config(text="Order of Disks Served: " + ", ".join(map(str, order_of_disks_served)))
            except ValueError:
                error_label.config(text="Invalid input. Please enter integers for numbers and head position.")

        # Button to trigger splitting the input and simulating the algorithm
        split_button = tk.Button(algorithm_frame, text="Get result", command=split_input)
        split_button.pack(pady=5)

        # Button to go back to the main screen
        back_button = tk.Button(algorithm_frame, text="Back", command=lambda: back_to_main(algorithm_frame))
        back_button.pack(pady=5)

# Function to create the main screen
def create_main_screen():
    global main_frame
    main_frame = tk.Frame(root)
    main_frame.pack()

    # Add buttons for each algorithm
    algorithms = ["Optimal Algorithm", "C-look Algorithm", "Second Chance Algorithm", "C-Scan Algorithm"]
    for algorithm in algorithms:
        button = tk.Button(main_frame, text=algorithm, command=lambda alg=algorithm: open_algorithm_screen(alg))
        button.pack(pady=10)

# Function to go back to the main screen
def back_to_main(frame):
    frame.pack_forget()
    create_main_screen()

# Main Tkinter window
root = tk.Tk()
root.title("Algorithm Selector")

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set window size to match screen width and height
root.geometry("%dx%d+0+0" % (screen_width, screen_height))

# Create main screen
create_main_screen()

# Run the Tkinter event loop
root.mainloop()
