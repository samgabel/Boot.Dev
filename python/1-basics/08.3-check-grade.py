def get_english_grade(student):
    desired_course = "English_1010"
    grade = student["type"]["student"]["courses"][desired_course]["current_grade"]

    courses = student["type"]["student"]["courses"]

    if "English_1010" in courses:
        return grade


def main(a):
    func = get_english_grade(a)
    print(func)

#---------------------------------------------------------

student = {
    "type": {
        "student": {
            "name": "Allan",
            "courses": {
                "math_1050": {
                    "current_grade": "B",
                },
                "English_1010": {
                    "current_grade": "A-",
                },
            },
        }
    }
}

main(student)
