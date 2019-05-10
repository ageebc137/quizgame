#Chemistry 101 Quiz Game
#Final Project for Stanford Python CS59 Summer 2017
#Allister Bernal & Kevin Haney


#Initial variables--questions, responses, correct answers
import string
import pandas as pd
from string import ascii_lowercase
df = pd.read_csv("QuizGame.csv")
categories = df.Category.unique()
points = 0

#Introduction of game
print("\nWelcome to the Bash-Your-Brain Quiz Game! \n\nWe will provide you with 5 multiple-choice questions. "
    "\nPlease select the correct response. \n\nAt the end of the quiz, your score will be tallied."
    " \n\nGood Luck. Hope you pass!\n")

name = input("Please enter your name: ")
pAnswer = input("Hello, " + name + ". " + "Would you like to play? (Y/N): ")
pAnswer = pAnswer.upper() #Convert Answer to Upper Case

while pAnswer != "N"  and pAnswer != "Y":
  pAnswer = input("Please provide a valid answer. Y or N: ")
  pAnswer = pAnswer.upper() #Convert Answer to Upper Case


#Quiz Game
if pAnswer == "N": #if user answers "N" then the game is over
  print("Game over")
  exit()
else:
    #prints the categories in the file.
    print("\nCategories: \n")
    for i in range(0, len(categories)):
        category = categories[i]
        category = string.capwords(category) #Capitalizes the first letter of the word
        print(category)
    subjectArea = input("\nPlease type in one of the above categories:") #Determine subject area
    subjectArea=subjectArea.lower()

    while not subjectArea in categories: #checks for a valid category input
        print("\nCategories:\n")
        for i in range(0, len(categories)):
            category = categories[i]
            category = string.capwords(category)  # Capitalizes the first letter of the word
            print(category)
        subjectArea = input("\n" + string.capwords(subjectArea) + " is not a category.\nPlease input one of the categories")
        subjectArea = subjectArea.lower()

    # Beginning of the quiz
    print("\nYou can take the " + subjectArea + " test.\n")

    subjectTest = df[df.Category == subjectArea]
    letters = subjectTest.columns.values[1:5]
    for i in range(0,len(subjectTest)): # Iterates through the subset of questions under the chosen subject
        print(subjectTest.iloc[i,0] + "\n")

        for j in range(1,5):
            letter = letters[j - 1]
            print(letter + ". " + subjectTest.iloc[i,j]) # Prints the choices and adds the corresponding letter.
        pAnswer = input("\nInsert your answer here: ")
        pAnswer = pAnswer.upper()

        while not pAnswer in letters: # checks for a valid input
            pAnswer = input("\nThat is not a valid choice.\nPlease input any of these letters (A, B, C, or D): ")
            pAnswer = pAnswer.upper()

        corrAnswer = subjectTest.iloc[i,5]
        if pAnswer == corrAnswer: #checks for the correct answer
            print("\n" + name + "... \nTHAT IS CORRECT!!!!")
            points+=1
        else:
            print("\n"+ name + ", umm... that is wrong")
        print("\nCorrect answer is: " + corrAnswer)

#Calculate Grade
print("\n")
if points/5*100 >= 90:
   grade = 'A'
   print("YOU ARE A QUIZ SUPERSTAR!!!!")
elif points/5*100 >= 80:
   grade= 'B'
   print("You are a quiz whiz!")
elif points/5*100 >= 70:
   grade= 'C'
   print("You get a pass.")
elif points/5*100 >= 60:
   grade = 'D'
   print("You may need to study a little more....")
else:
   grade = 'F'
   print("Probably best to keep your day job....")
#Game ends with results of the game, final score and letter grade
print("\n" + name + ", you scored " + str(points/5*100) + "%.")
print("Your Final Letter Grade was:", grade)
