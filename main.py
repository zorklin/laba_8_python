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

print_grades(student_info, "Третій курс", "УН 43", "Костюк Андрій Петрович", "Алгебра")
add_grade(student_info, "Третій курс", "УН 43", "Костюк Андрій Петрович", "Алгебра", 80)
print_grades(student_info, "Третій курс", "УН 43", "Костюк Андрій Петрович", "Алгебра")



# Плутенко Олексій. Існуюча структура словника є ієрархічною, що дозволяє ефективно зберігати оцінки
# студентів за курсами та групами. Цей підхід забезпечує швидкий доступ до інформації про конкретних
# студентів, роблячи його інтуїтивно зрозумілим. Також було б корисно додати функції для отримання
# всіх предметів учнів, а також для обчислення середнього значення оцінок по кожному з предметів. Крім того,
# реалізація меню дозволить користувачам легше взаємодіяти з системою, роблячи її більш зручною та зрозумілою.

# Функція для отримання усіх предметів студента
def get_studen_subjects(dictionary, course, group, student):
    if course in dictionary and group in dictionary[course] and student in dictionary[course][group]:
        subjects = dictionary[course][group][student]
        print(f"Предмети для студента {student}:")
        for subject in subjects:
            print(f"{subject}: {subjects[subject]}")
    else:
        print(f"Студента {student} не знайдено в курсі {course}, групі {group}.")

get_studen_subjects(student_info, "Третій курс", "УН 43", "Костюк Андрій Петрович")


# Функція для обчислення середньої оцінки
def calculate_average_grade(dictionary, course, group, student, subject):
    if to_be(dictionary, course, group, student, subject):
        grades = dictionary[course][group][student][subject]
        average = sum(grades) / len(grades) if grades else None
        print(f"Середня оцінка для {student} з предмету {subject}: {average:.2f}")

calculate_average_grade(student_info, "Третій курс", "УН 43", "Костюк Андрій Петрович", "Алгебра")


# Плутенко Олексій, функція меню для взаємодії з користувачем
def menu():
    while True:
        print("\nМеню:")
        print("1. Вивести оцінки студента")
        print("2. Додати оцінку")
        print("3. Отримати всі предмети студента")
        print("4. Обчислити середню оцінку")
        print("5. Вихід")

        choice = input("Виберіть опцію (1-5): ")

        if choice == '1':
            course = input("Введіть курс: ")
            group = input("Введіть групу: ")
            student = input("Введіть ім'я студента: ")
            subject = input("Введіть предмет: ")
            print_grades(student_info, course, group, student, subject)

        elif choice == '2':
            course = input("Введіть курс: ")
            group = input("Введіть групу: ")
            student = input("Введіть ім'я студента: ")
            subject = input("Введіть предмет: ")
            grade = int(input("Введіть оцінку: "))
            add_grade(student_info, course, group, student, subject, grade)

        elif choice == '3':
            course = input("Введіть курс: ")
            group = input("Введіть групу: ")
            student = input("Введіть ім'я студента: ")
            get_studen_subjects(student_info, course, group, student)

        elif choice == '4':
            course = input("Введіть курс: ")
            group = input("Введіть групу: ")
            student = input("Введіть ім'я студента: ")
            subject = input("Введіть предмет: ")
            calculate_average_grade(student_info, course, group, student, subject)

        elif choice == '5':
            print("Вихід з програми.")
            break

        else:
            print("Невірний вибір, спробуйте ще раз.")

menu()