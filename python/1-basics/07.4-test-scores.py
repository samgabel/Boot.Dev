# Compare answer_sheet to student_answers
# return name and rounded percentage (ie. Name: 00%)

def get_test_score(answer_sheet, student_answers):
    score = 0

    student_name = student_answers.pop(0)
    
    for i in range(len(answer_sheet)):
        if answer_sheet[i] == student_answers[i]:
            score += 1
            
    percentage_float = score / len(answer_sheet) * 100
    percentage = round(percentage_float)

    return student_name, percentage


def main(a, b):
    name, percent = get_test_score(a, b)
    print(f"{name}: {percent}%")

#------------------------------------------------------------------

key = ["A", "C", "B", "C", "A", "D", "E", "A", "A"]
stu = ["John", "A", "D", "B", "C", "B", "D", "E", "A", "B"]  # student_answers are prepended with their name

main(key, stu)
