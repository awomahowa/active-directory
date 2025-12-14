print ("Welcome to my simple color fruit quiz game!")

playing = input("Do you want to play? (yes/no) \n")
if playing.lower() == "yes" or playing.lower() == "y":
    print("Alright, let's play!")
else:
    quit()
score = 0

answer = input("What are the colors of apples?\na) Green/Red\nb) Yellow\nc) Pink\n")
if answer.lower() == "a":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What are the colors of strawberries?\na) Green\nb) Yellow\nc) Red\n")
if answer.lower() == "c":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What are the colors of bananas?\na) Red\nb) Yellow/Green\nc) Pink\n")
if answer.lower() == "b":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You have answered " + str(score) + " questions correctly.")
print("With a rating of: " + str((score / 3) * 100 ) + "%")