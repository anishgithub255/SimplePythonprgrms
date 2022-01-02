print ("Welcome to my quiz game")

playing = input("Do you want to play? ")
score=0

if playing.lower() != "yes":
    quit()

print("Okay! Lets play :)" )

answer = input("What is the full form of CPU? ").lower()
if answer == "central processing unit":
    print ("Correct!")
    score += 1
else :
    print("Incorrect!")

answer = input("What is the full form of RAM? ").lower()
if answer == "randum access unit":
    print ("Correct!")
    score += 1
else :
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4)*100) + " %.")