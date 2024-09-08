import subprocess
import os

def get_valid_commit_count():
    while True:
        try:
            ip = int(input("How many times do you want to commit? \n"))
            if ip > 0:
                return ip
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_auto_push_choice():
    while True:
        autoPush = input("Do you want to auto push? (y/n) \n").lower()
        if autoPush in ['y', 'n']:
            return autoPush
        print("Invalid choice. Please enter 'y' or 'n'.")

def update_file(file_name, new_value):
    with open(file_name, 'w') as file:
        file.write(str(new_value) + '\n')
    print(f"File '{file_name}' updated to: {new_value}")

def get_current_value(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            try:
                return int(file.read().strip())
            except ValueError:
                return 0  # Handle non-integer content
    return 0

# Get inputs
ip = get_valid_commit_count()
autoPush = get_auto_push_choice()

file_name = "counter.txt"

# Get the current value in the file or initialize to 0
current_value = get_current_value(file_name)

# Loop for committing changes
for i in range(ip):
    current_value += 1  # Increment the current value
    update_file(file_name, current_value)  # Update the file with the new value
    
    # Add the file to staging, then commit
    try:
        subprocess.run(['git', 'add', file_name], check=True)
        commit_message = f"Updated {file_name} to {current_value} - Commit {i+1} of {ip}"
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)
        print(f"Committed: {commit_message}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to commit: {e}")
        break

print(f"Committed {ip} times")

# Check if auto-push is required
if autoPush == 'y':
    try:
        subprocess.run(['git', 'push'], check=True)
        print("Pushed to remote successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to push: {e}")
