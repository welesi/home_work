from random import choice

student = input('Представьтесь, пожалуйста: ')
try:
    level = int(input('Выберите уровень сложности 1 - Контрольная: '))
except:
    level = 1
    print('Установлен первый уровень сложности.')
if level < 1 or level > 3:
    level = 1
    print('Установлен первый уровень сложности. ')

print(f'Хорошо, {student}. Тебе викторина по географии!')

questions = {
    1: [("Столица России?", "Москва"), ("Столица Франции?", "Париж"), ("Столица Италии?", "Рим")],
    2: [("Какая самая большая страна по площади?", "Россия"), ("На каком материке находится Австралия?", "Австралия"), ("Какая река самая длинная?", "Амазонка")],
    3: [("Какое море самое соленое?", "Мертвое море"), ("Какая страна самая густонаселенная?", "Китай"),
        ("Какая пустыня самая большая?", "Сахара")]}

points = 0
for i in range(3):
    question, correct_answer = choice(questions[level])
    print(f'{student}, {question}', end='')
    student_answer = input().strip(). lower()
    if student_answer == correct_answer.lower():
        points += 1
        print(f'Правильно!')
else:
    print(f'Не правильно. Правильный ответ {correct_answer}!')

if points == 3:
    print(f'Ты настоящий знаток географии, {student}!')
elif points == 2:
    print(f'Хорошо, {student}, но можно лучше.')
else:
    print(f'Нужно подтянуть географию, {student}.')
