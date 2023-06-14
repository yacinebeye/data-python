# Creating a loop for 5 elements

myscore=[]
sum=0
for i in range(5):

    while True: 
        try: 
            score = (int(input(f'Enter test score {i+1} : ')))
            sum=sum+score

# Adding error handling for invalid input            
            if score < 0 or score > 100:  
                print (ValueError("Invalid score , please try again"))
            break
                #return myscore 
        except ValueError as error:
            print(error)

# getting the average of the scores and printing it 
avg=sum/5.0
print ("-------------------------")
print("Average score :", str(avg))

# determining the grade for each score and getting it printed with the use of elif and a function
def determine_grade(myscore): 
    if avg < 60:  
        print("Letter grade = F")
    elif avg >= 60 or avg <=69:
         print("Letter grade = D")
    elif avg >= 70 or avg <=79:
         print("Letter grade = C") 
    elif avg >= 80 or avg <=89:
         print("Letter grade = B")
    elif avg >= 90:
         print("Letter grade = A ")
 
grade = determine_grade(myscore)
# print (grade)

