from colorama import Fore, init
import time

# Initialize colorama
init(autoreset=True)

score = 0

# Loading Effect
print(Fore.YELLOW + "Initializing Cyber Security System...")
time.sleep(2)

# Game Title
print(Fore.CYAN + "===== CYBER SENTINEL =====")

# Player Name
name = input("Enter Agent Name: ")

print(Fore.GREEN + f"Welcome Agent {name}")

# Question 1
answer1 = input("Block suspicious IP? (yes/no): ")

if answer1 == "yes":
    print(Fore.GREEN + "Mission Successful")
    score += 10
else:
    print(Fore.RED + "Security Breach")

# Question 2
answer2 = input("Allow unknown hacker access? (yes/no): ")

if answer2 == "no":
    print(Fore.GREEN + "Correct Decision")
    score += 10
else:
    print(Fore.RED + "System Hacked")

# Question 3
answer3 = input("Quarantine infected file? (yes/no): ")

if answer3 == "yes":
    print(Fore.GREEN + "Threat Neutralized")
    score += 10
else:
    print(Fore.RED + "Virus Spread Detected")

# Final Score
print(Fore.CYAN + f"Final Score: {score}")

# Rank System
if score == 30:
    print(Fore.GREEN + "Rank: Elite Cyber Agent")

elif score >= 20:
    print(Fore.YELLOW + "Rank: Security Specialist")

else:
    print(Fore.RED + "Rank: Trainee")

# Save Score
file = open("scores.txt", "a")
file.write(name + " : " + str(score) + "\n")
file.close()