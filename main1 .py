#ієрархічний словник, доступ до оцінок: курс -> група -> ім'я -> предмет
student_info = {
    "Перший курс": {
        "ІВ 41": {
            "Мельник Олег Васильович": {
                "Математика": [82, 80, 76],
                "Python": [65, 70, 75, 68],
                "Фізика": [78, 64],
                "Алгебра": [78, 80]
            },
            "Гнатюк Віктор Петрович": {
                "Математика": [76, 78, 80],
                "Python": [70, 68, 72],
                "Алгебра": [82, 81, 80],
                "Хімія": [75, 78]
            },
            "Тарасенко Дмитро Ігорович": {
                "Математика": [80, 82, 84],
                "Python": [60, 62, 65],
                "Алгебра": [70, 72, 74],
                "Хімія": [75]
            }
        },
        "ІТ 41": {
            "Петренко Оксана Володимирівна": {
                "Математика": [88, 90, 92],
                "Python": [85, 87],
                "Фізика": [80, 82]
            },
            "Сергійенко Максим Андрійович": {
               "Математика": [78, 80],
               "Python": [70, 75],
               "Алгебра": [82, 84]
            }
        }
    },
    "Другий курс": {
        "КН 42": {
            "Петров Андрій Олександрович": {
                "Математика": [85, 76, 90],
                "Python": [70, 80, 95, 88],
                "Алгебра": [90, 92],
                "Фізика": [78, 80, 82, 85]
            },
            "Сидоров Іван Миколайович": {
                "Історія": [88, 82],
                "Python": [78, 74, 89],
                "Алгебра": [92, 90, 95],
                "Хімія": [85, 87]
            }
        },
        "СУ 42": {
            "Григорович Анна Олександрівна": {
                "Математика": [92, 94, 90],
                "Python": [85, 88, 91],
                "Алгебра": [93, 94, 95],
                "Біологія": [80, 82]
            },
            "Завадський Олег Васильович": {
                "Математика": [75, 78],
                "Python": [80, 82],
                "Хімія": [72, 75]
            }
        }
    },
    "Третій курс": {
        "ГК 43": {
            "Коваленко Олена Сергіївна": {
                "Біологія": [90, 85, 88],
                "Python": [95, 92, 94],
                "Алгебра": [87, 89, 90],
                "Фізика": [80, 82]
            },
            "Іваненко Наталія Юріївна": {
                "Фізика": [92, 94, 90],
                "Python": [85, 88, 91, 87],
                "Алгебра": [95, 96, 94],
                "Хімія": [88, 90]
            }
        },
        "УН 43": {
            "Кузьменко Анна Олександрівна": {
                "Фізика": [91, 89, 92],
                "Python": [95, 97, 98],
                "Алгебра": [88, 90, 92],
                "Інформатика": [86, 87, 88, 89]
            },
            "Костюк Андрій Петрович": {
                "Математика": [82, 85],
                "Python": [77, 79],
                "Алгебра": [72, 75]
            }
        }
    }
}

#Федорченков Андрій допоміжна функція перевірки на присутність в словнику
def to_be(dictionary, course, group, student, subject):
    if (course in dictionary and group in dictionary[course] and
        student in dictionary[course][group] and
        subject in dictionary[course][group][student]):
        return True
    else:
        print(f"Невірні дані, не знайдено")
        return False

#Федорченков Андрій, додати оцінку
def add_grade(dictionary, course, group, student, subject, grade):
    if (to_be(dictionary, course, group, student, subject)):
        dictionary[course][group][student][subject].append(grade)
        print(f"Оцінка {grade} додана до предмету {subject} для студента {student}")

#Федорченков Андрій, допоміжна функція виводу
def print_grades(dictionary, course, group, student, subject):
    if (to_be(dictionary, course, group, student, subject)):
        grades = dictionary[course][group][student][subject]
        print(f"Курс: {course}, група: {group}, студент: {student}, предмет: {subject}, оцінки: {grades}")

#Попов Максим, виведення рейтингу студентів курсу на основі середнього балу
def rating(dictionary, course):
    if course not in dictionary:
        print("Такого курсу немає!")
        return
    students = []
    for group in dictionary[course]:
        for student in dictionary[course][group]:
            average = 0
            for subject in dictionary[course][group][student]:
                average += sum(dictionary[course][group][student][subject])/len(dictionary[course][group][student][subject])
            average /= len(dictionary[course][group][student])
            students.append((student, group, average))
    students.sort(key=lambda value: -value[2])
    print(course, "рейтинг")
    i=1
    for student in students:
        print(str(i)+". ПІБ:", student[0], "\t\tГрупа:", student[1], "\t\tСередній бал:", student[2])
        i+=1

# Меша Павло, виведення максимальної, мінімальної оцінки та кількості оцінок студента заданого курсу ,
# якщо є оцінка менше 60 балів, видалення оцінок за заданим предметом
def max_grade_student(dictionary, course, group, student, subject):
    if to_be(dictionary, course, group, student, subject):
        grades = dictionary[course][group][student][subject]
        max_grade = max(grades)
        min_grade = min(grades)
        if min_grade < 60:
            del dictionary[course][group][student][subject]
            print(f"Видалено {student} предмет {subject}: {min_grade}")
        else:
            kol = len(grades)
            print(f" {student}")
            print(f"Кількість оцінок з предмету {subject}: {kol}")
            print(f"Максимальна оцінка з предмету {subject}: {max_grade}")
            print(f"Мінімальна оцінка з предмету {subject}: {min_grade}")

max_grade_student(student_info, "Перший курс", "ІВ 41", "Мельник Олег Васильович", "Python")
print_grades(student_info, "Третій курс", "УН 43", "Костюк Андрій Петрович", "Алгебра")
add_grade(student_info, "Третій курс", "УН 43", "Костюк Андрій Петрович", "Алгебра", 80)
print_grades(student_info, "Третій курс", "УН 43", "Костюк Андрій Петрович", "Алгебра")

rating(student_info, "Перший курс")