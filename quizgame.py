print("Welcome to quiz game!")

playing = input("Do you want to play? ")
if playing.lower() == "yes" or playing.lower() == "y":
    print("Alright, let's play!")
else:
    quit()
score = 0

answer = input("Who is the most followed celebrity in instagram? ")
if answer.lower() == "christiano ronaldo":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("Who is the most followed local celebrity in facebook? ")
if answer.lower() == "anne curtis":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What is calcifer's color? ")
if answer.lower() == "gray":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

print("You answered: " + str(score) + " items correctly.")
print("With a rating of: " + str((score / 3) * 100) + "%")