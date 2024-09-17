import tkinter as tk
from tkinter import messagebox

# Initialize the candidates and vote counts
candidates = {
    "Bob": 0,
    "Marry": 0,
    "Sarrh": 0,
    "John": 0
}

# Global variable for tracking voters left
voters_left = 0


# Function to cast a vote for a candidate
def vote(voter_input):
    voter_input = voter_input.strip().lower()
    candidates_lowercase = {candidate.lower(): candidate for candidate in candidates}

    if voter_input in candidates_lowercase:
        candidates[candidates_lowercase[voter_input]] += 1
        messagebox.showinfo("Vote Submitted", f"Thank you for voting for {candidates_lowercase[voter_input]}!")
    else:
        messagebox.showerror("Invalid Input", "Invalid candidate. Please try again.")
        return False  # Return False if the vote was not cast successfully

    return True  # Return True if the vote was successfully cast


# Function to display the voting result and announce the winner
def display_result():
    result_text = "Voting Results:\n\n"
    max_votes = -1
    winner = None

    for candidate, vote_count in candidates.items():
        result_text += f"{candidate} has {vote_count} votes.\n"
        if vote_count > max_votes:
            max_votes = vote_count
            winner = candidate
        elif vote_count == max_votes:
            winner = "It's a tie!"

    result_text += f"\nThe winner is: {winner}\n"
    result_window = tk.Toplevel(root)
    result_window.title("Voting Results")
    result_label = tk.Label(result_window, text=result_text, font=("Arial", 14), padx=20, pady=20)
    result_label.pack()


# Function to handle the voting process
def vote_for_candidate():
    voter_input = vote_input_entry.get()  # Get input from the entry box
    if vote(voter_input):  # Only decrease the number of voters if vote is successful
        global voters_left
        voters_left -= 1
        update_voters_left_label()

    if voters_left == 0:
        display_result()


# Function to update the number of voters left
def update_voters_left_label():
    voters_left_label.config(text=f"Voters left: {voters_left}")


# Function to start the voting process after entering the number of voters
def start_voting():
    global voters_left
    voters_left = int(num_voters_entry.get())  # Get number of voters
    if voters_left <= 0:
        messagebox.showerror("Invalid Input", "Please enter a valid number of voters.")
    else:
        show_voting_window()  # Open the voting window


# Function to show the voting window with candidates and voter input
def show_voting_window():
    voting_window = tk.Toplevel(root)
    voting_window.title("Voting Window")

    # Display candidates
    candidate_label = tk.Label(voting_window, text="Candidates:", font=("Arial", 14))
    candidate_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    for idx, candidate in enumerate(candidates):
        candidate_display = tk.Label(voting_window, text=candidate, font=("Arial", 12))
        candidate_display.grid(row=idx + 1, column=0, padx=20, pady=5)

    # Voter input and button
    voter_input_label = tk.Label(voting_window, text="Enter the candidate's name:", font=("Arial", 14))
    voter_input_label.grid(row=0, column=1, padx=10, pady=10)

    global vote_input_entry
    vote_input_entry = tk.Entry(voting_window, font=("Arial", 12))
    vote_input_entry.grid(row=1, column=1, padx=10, pady=5)

    vote_button = tk.Button(voting_window, text="Submit Vote", font=("Arial", 12), command=vote_for_candidate)
    vote_button.grid(row=2, column=1, padx=10, pady=10)

    # Label to display voters left
    global voters_left_label
    voters_left_label = tk.Label(voting_window, text=f"Voters left: {voters_left}", font=("Arial", 12))
    voters_left_label.grid(row=3, column=1, padx=10, pady=10)


# Tkinter GUI setup
root = tk.Tk()
root.title("Voting System")

# Create a label for voter instructions
instructions_label = tk.Label(root, text="Enter the number of voters:", font=("Arial", 14))
instructions_label.pack(pady=10)

# Entry box to enter number of voters
num_voters_entry = tk.Entry(root, font=("Arial", 12))
num_voters_entry.pack(pady=5)

# Button to start the voting process
start_button = tk.Button(root, text="Start Voting", font=("Arial", 12), command=start_voting)
start_button.pack(pady=10)

# Start Tkinter event loop
root.mainloop()
