import os

ip = int(input("How many times do you want to commit? \n"))
autoPush = input("Do you want to auto push? (y/n) \n")

# for loop
for i in range(ip):
   os.system(f'git commit --allow-empty -m "Commit {i} of {ip}"')

print("Commited " + str(ip) + " times")

if autoPush == 'y':
   os.system("git push")