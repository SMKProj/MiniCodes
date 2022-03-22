# Test Average and Grade 
# Write a program that asks the user to enter ﬁve test scores.
# The program should display a letter grade for each score and the average test score.
# Write the following functions in the program: 
# • calc_average This function should accept ﬁve test scores as arguments and return the average of the scores. 
# • determine_grade This function should accept a test score as an argument and return a letter grade for the 
# score based on the following grading scale: 

scores = []
score_grade = []
print("__________________________________________________________")
print("You are requested to enter score values between 0 and 100")
print("__________________________________________________________")
try:
    for x in range(5):
        s = int(input("Enter score values: "))
        if s < 0:
            raise ValueError 
        else:
            scores.append(s)
except ValueError:
    print("You are requested to enter positive integer values only")
else:
    def calc_avg(scores):
        t = sum(scores)
        len_scores = len(scores)
        avg = t / len_scores
        print("Average Test Score is : ", avg)
        return avg

    calc_avg(scores)
    
    def determine_grade (score_point):
        if 90 <= score_point <= 100:
            score_grade.append([score_point, "A"])
        elif 80 <= score_point <= 89:
            score_grade.append([score_point, "B"])
        elif 70 <= score_point <= 79:
            score_grade.append([score_point, "C"])
        elif 60 <= score_point <= 69:
            score_grade.append([score_point, "D"])
        else:
            score_grade.append([score_point, "F"])
    
    for i in scores:
        determine_grade(i)
    
    print("-------------------------------")
    for j in range(len(score_grade)):
        print(score_grade[j])
    print("-------------------------")

    