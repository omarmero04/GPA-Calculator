print("=================== -Welcome to GPA calculator- ===================\n")
while True:
 nam=input("Please, enter your name ").title()
 while True:
    try:
        num = int(input(f"Hello {nam}, please enter the number of subjects you want to calculate: "))
        if num > 0:
            break
        else:
            print(" Please enter a real positive number of subjects.\a")
    except ValueError:
        print(" You didn't enter a number. Please enter a valid number.\a")

 sum_h = 0
 sum_x = 0
 list_nam=[]
 list_gra=[]

 for number in range(num) :
  sub_nam = input("Enter the subject name ").title()
  list_nam.append(sub_nam)
  while True:
   try:  
     credit_h = int(input(f"Enter the credit hour of the {sub_nam} "))
     if credit_h > 0:
        break
     else:
         print(" Please enter a real positive number of credit hours.\a")
   except ValueError:
        print(" You didn't enter a number. Please enter a valid number.\a")
  while True:
     try:      
      grade = float(input(f"Enter the grade of the {sub_nam} (0-4) "))
      if 0 <= grade <= 4:
         break
      else:
         print("Enter your grade from range 0 - 4 please \a ")
     except ValueError:
        print("Not a vaild number please enter a number \a")

  list_gra.append(grade)
  print("----------------------------------------------")
  x = credit_h * grade 
  sum_x = sum_x + x
  h = credit_h
  sum_h = sum_h + h


 print("\n")
 print("----------------------------------------------")
 print("|Subject\t\t|\t\tGrade|")
 print("----------------------------------------------")
 for number in range(num):
  print(f"|{list_nam[number]:<12}\t\t|\t\t{list_gra[number]:<6}|")

 print("----------------------------------------------")

 gpa = sum_x / sum_h 
 print(f"Dear, {nam} your GPA = {gpa}")

 if gpa == 4 :
    print("Excellent A+")
 elif gpa < 4 and gpa >= 3.7 :
    print("Excellent A")
 elif gpa < 3.7 and gpa >= 3.3 :
    print("Excellent A-")
 elif gpa < 3.3 and gpa >= 3.0 :
    print("Great B+")
 elif gpa < 3 and gpa >= 2.7 :
    print("Great B")
 elif gpa < 2.7 and gpa >= 2.3 :
    print("Great B-")
 elif gpa < 2.3 and gpa >= 2 :
    print("Good C+")
 elif gpa < 2 and gpa >= 1.7 :
    print("Good C")
 elif gpa < 1.7 and gpa >= 1.3 :
    print("Good C-")
 elif gpa < 1.3 and gpa >= 1 :
    print("Pass D+") 
 elif gpa < 1 and gpa >= 0.7 :
    print("Pass D")
 elif gpa < 0.7 and gpa > 0 :
    print("Pass D-")
 elif gpa == 0 :
    print("Fail F")

 check=int(input("Do you want to do another calculation for yes press 1 no press 0 ? "))
 if check == 0:
  print("Goodluck Amigo see you soon")
  break 