import random
#This program takes grade from students and then tell them if they passed or failed the class and also tell them their GPA and score
#ask for name and number of classes you took
name = input("what is your name \n")
print("Hello "+ name + " Welcome to the course grading app" )
#verify if user is human
flag = True
while(flag):
  print("<<<<Human verification>>>>")
  Ran = str(random.randrange(1,20))
  print(Ran)
  get_verification = input("<<<<Enter the number you see on the screen for human verification>>>>\n")
  
  if Ran == str(get_verification):
    flag = False
  elif get_verification == "":
    print("<<<<Human verification error>>>\nYou did not enter a number\nPlease enter a number!!!")
    flag = True
  else:
    print("<<<<Human verification error>>>\nYour code does not match\nPlease try again!!!")
    flag = True
#funtions



f= True
while(f):
  numOfClassesTaken = input("how many class did you take in your previous semester\n")
  if numOfClassesTaken.isdigit():
    numOfClassesTaken = int(numOfClassesTaken)
    f = False
  elif numOfClassesTaken.isalpha():
    print("your input is not an integer\nYour input should be an integer\nPlease try again")
    f = True

#ask for the classes you took and grade for the class
result = 0
count = 1

average = 0
classNameList =[]
gradeList = []
temp = True


print("What classes did you take ? \n")
for i in range(numOfClassesTaken) :
  className = input( str(count) +". Classes Name\n")
  grade = float(input( "Grade for the class\n"))
  count = count+1
  classNameList.append(className)
  gradeList.append(grade)

#instruction menu
def instructionMenuF():
  print("press 0 to see  instruction menu again")
  print("press for 1 for your average in percentage")
  print("press 2 for your GPA ")
  print("press 3 to know if your you passed or failed a class")
  print("press 4 to print out the result")
  print("print 9 to exit from for the program")

#calculate average in percentage
def calAverage():
  total = 0
  for i in range(len(gradeList)):
    total = total + gradeList[i]
  average = total/len(gradeList)
  print(str(average)+"%")
#calculate GPA
def GPA():
  total =0
  for i in range(len(gradeList)):
    total = total + gradeList[i]
  GPA = ((total/(len(gradeList)*100))*4)
  return GPA
def Print():
  print(" Class Name \tGrade")
  count =1
  for i in range(len(gradeList)):
    print(str(count) +".    "+ str(classNameList[i]) +"        "+ str(gradeList[i]))
    count = count+1

#Calculate of if the student failed or passed the class
def PassedOrFailedcalc():
  ClassP_F = input("What class do you want to know if you failed or passed ?\n")
  def calcF_P() :
    postionOfTheClass = classNameList.index(ClassP_F)
    getGPA = gradeList[postionOfTheClass]
    hisGPA = ((getGPA/100)*4)
    if hisGPA == 4.0:
      print("your GPA is A\nYou passed the class")
    elif hisGPA >= 3.7:
      print("your GPA is A-\nYou passed the class")
    elif hisGPA >= 3.3:
      print("your GPA is B+\nYou passed the class")
    elif hisGPA >= 3.0:
      print("your GPA is B\nYou passed the class")
    elif hisGPA >= 2.7:
      print("your GPA is B-\nYou passed the class")
    elif hisGPA >= 2.3:
      print("your GPA is C+\nYou passed the class")
    elif hisGPA >= 2.0:
      print("your GPA is C\nYou passed the class")
    elif hisGPA >= 1.7:
      print("your GPA is C-\nYou passed the class")
    elif hisGPA >= 1.0:
      print("your GPA is D\nYou failed the class")
    elif hisGPA >= 0.7:
      print("your GPA is D-\nYou failed the class")
    elif hisGPA >= 0.0:
      print("your GPA is F\nYou failed the class")
  return calcF_P()

while(temp):
  numChoice = int(input("press 0 for instruction menu\n"))
  if numChoice == 0:
    print(instructionMenuF())

  elif numChoice == 1:
    print(calAverage())

  elif numChoice == 2:
    print(GPA())

  elif numChoice == 3:
    print(PassedOrFailedcalc())
  elif numChoice ==4:
    print(Print())



  elif numChoice == 9:
    print("Thank you!!!! for using this program\nHave a good one")
    temp = False
