import subprocess

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

# Get validated inputs
ip = get_valid_commit_count()
autoPush = get_auto_push_choice()

# for loop for git commits
for i in range(ip):
    commit_message = f"🥵 Commit {i+1} of {ip}"
    try:
        subprocess.run(['git', 'commit', '--allow-empty', '-m', commit_message], check=True)
        print(f"Committed: {commit_message}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to commit: {e}")

print(f"Committed {ip} times")

# Check if auto-push is required
if autoPush == 'y':
    try:
        subprocess.run(['git', 'push'], check=True)
        print("Pushed to remote successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to push: {e}")
